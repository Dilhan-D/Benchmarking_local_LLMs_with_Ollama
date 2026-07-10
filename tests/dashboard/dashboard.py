#!/usr/bin/env python3
"""
Dashboard Streamlit - Ollama Granite Test Series
Visualise les résultats des comparaisons RPGLE / CLLE / COBOL

v2 : lecture CSV robuste (gère les schémas désynchronisés / colonnes manquantes)
"""


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path



# ============================================================
# CONFIG PAGE
# ============================================================
st.set_page_config(
    page_title = "Granite Test Series",
    page_icon  = "🤖",
    layout     = "wide"
)



# ============================================================
# CHARGEMENT CSV
# ============================================================
RESULTS_DIR = Path(__file__).parent.parent / "results"


SOURCES = {
    "rpgle" : RESULTS_DIR / "rpgle_test_before_finetune" / "synthese_comparaison.csv",
    "clle"  : RESULTS_DIR / "clle_test_before_finetune"  / "synthese_comparaison.csv",
    "cobol" : RESULTS_DIR / "cobol_test_before_finetune" / "synthese_comparaison.csv",
}


# Colonnes minimales attendues par le dashboard. Toute colonne manquante
# (ex: extraction_bloc_md absent d'un ancien CSV) sera ajoutée avec une valeur par défaut.
COLONNES_ATTENDUES = {
    "execution"         : 0,
    "date"              : "",
    "langage"           : "",
    "test"              : "",
    "fichier_entree"    : "",
    "fichier_reponse"   : "",
    "lignes_entree"     : 0,
    "lignes_sortie"     : 0,
    "identiques"        : 0,
    "modifiees"         : 0,
    "ajoutees"          : 0,
    "supprimees"        : 0,
    "total_diff"        : 0,
    "similarite"        : 0.0,
    "extraction_bloc_md": False,
}


@st.cache_data
def charger_donnees():
    frames  = []
    erreurs = []

    for langage, path in SOURCES.items():
        if not path.exists():
            continue

        try:
            # Séparateur fixe (le comparateur écrit toujours en ';'), plus robuste
            # que l'auto-détection en cas de champs contenant des virgules.
            df = pd.read_csv(path, sep=';', engine='python', on_bad_lines='skip')
        except Exception as e:
            erreurs.append(f"{langage} ({path.name}) : {e}")
            continue

        # Complète les colonnes manquantes avec des valeurs par défaut
        # pour rester compatible avec les anciens CSV générés avant ajout
        # de nouvelles colonnes (ex: extraction_bloc_md).
        for col, defaut in COLONNES_ATTENDUES.items():
            if col not in df.columns:
                df[col] = defaut

        df["langage"] = langage
        frames.append(df)

    if erreurs:
        for msg in erreurs:
            st.warning(f"⚠️ CSV ignoré (erreur de lecture) — {msg}")

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)



df = charger_donnees()



# ============================================================
# HEADER
# ============================================================
st.title("🤖 Ollama Granite — Test Series Dashboard")
st.caption("Comparaison des réponses Granite avant fine-tuning")


if df.empty:
    st.error("Aucun CSV trouvé ou tous les CSV sont invalides. Lance d'abord les scripts de comparaison.")
    st.stop()


# Nettoyage défensif
df["langage"]    = df["langage"].astype(str).str.strip()
df["similarite"] = pd.to_numeric(df["similarite"], errors="coerce").fillna(0.0)
df["execution"]  = pd.to_numeric(df["execution"],  errors="coerce").fillna(0).astype(int)
df["total_diff"] = pd.to_numeric(df["total_diff"], errors="coerce").fillna(0).astype(int)



# ============================================================
# SIDEBAR — FILTRES
# ============================================================
st.sidebar.header("🔧 Filtres")


langages_dispo = sorted(df["langage"].unique().tolist())
langages_sel   = st.sidebar.multiselect(
    "Langages",
    options = langages_dispo,
    default = langages_dispo
)


runs_dispo = sorted(df["execution"].unique().tolist())
runs_sel   = st.sidebar.multiselect(
    "Exécutions",
    options = runs_dispo,
    default = runs_dispo
)


seuil_similarite = st.sidebar.slider(
    "Seuil similarité minimum (%)",
    min_value = 0,
    max_value = 100,
    value     = 0
)


if st.sidebar.button("🔄 Actualiser les données"):
    st.cache_data.clear()
    st.rerun()


# Filtrage
df_filtre = df[
    (df["langage"].isin(langages_sel)) &
    (df["execution"].isin(runs_sel)) &
    (df["similarite"] >= seuil_similarite)
]


if df_filtre.empty:
    st.warning("Aucun résultat avec ces filtres.")
    st.stop()



# ============================================================
# KPI — MÉTRIQUES GLOBALES
# ============================================================
st.markdown("---")
st.subheader("📊 Métriques globales")


col1, col2, col3, col4, col5 = st.columns(5)


col1.metric("Tests total",        len(df_filtre))
col2.metric("Similarité moyenne", f"{df_filtre['similarite'].mean():.1f}%")
col3.metric("Similarité max",     f"{df_filtre['similarite'].max():.1f}%")
col4.metric("Similarité min",     f"{df_filtre['similarite'].min():.1f}%")
col5.metric("Total différences",  int(df_filtre["total_diff"].sum()))



# ============================================================
# ROW 1 — SIMILARITÉ PAR LANGAGE + DISTRIBUTION
# ============================================================
st.markdown("---")
col_a, col_b = st.columns(2)


with col_a:
    st.subheader("🏆 Similarité moyenne par langage")
    stats = df_filtre.groupby("langage")["similarite"].mean().reset_index()
    stats.columns = ["Langage", "Similarité (%)"]
    stats["Similarité (%)"] = stats["Similarité (%)"].round(2)


    fig_bar = px.bar(
        stats,
        x       = "Langage",
        y       = "Similarité (%)",
        color   = "Langage",
        text    = "Similarité (%)",
        range_y = [0, 100],
        color_discrete_sequence = px.colors.qualitative.Set2
    )
    fig_bar.update_traces(textposition="outside")
    fig_bar.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig_bar, use_container_width=True)


with col_b:
    st.subheader("📦 Distribution des similarités")
    fig_box = px.box(
        df_filtre,
        x      = "langage",
        y      = "similarite",
        color  = "langage",
        points = "all",
        color_discrete_sequence = px.colors.qualitative.Set2
    )
    fig_box.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig_box, use_container_width=True)



# ============================================================
# ROW 2 — ÉVOLUTION PAR RUN + RÉPARTITION DIFFÉRENCES
# ============================================================
st.markdown("---")
col_c, col_d = st.columns(2)


with col_c:
    st.subheader("📈 Évolution similarité par run")
    evo = df_filtre.groupby(["execution", "langage"])["similarite"].mean().reset_index()
    fig_line = px.line(
        evo,
        x       = "execution",
        y       = "similarite",
        color   = "langage",
        markers = True,
        color_discrete_sequence = px.colors.qualitative.Set2
    )
    fig_line.update_layout(height=350, yaxis_range=[0, 100])
    st.plotly_chart(fig_line, use_container_width=True)


with col_d:
    st.subheader("🔍 Répartition des différences")
    diff_cols = ["modifiees", "ajoutees", "supprimees"]
    for col in diff_cols:
        df_filtre[col] = pd.to_numeric(df_filtre[col], errors="coerce").fillna(0).astype(int)


    diff_sum = df_filtre[["langage"] + diff_cols].groupby("langage").sum().reset_index()
    fig_stack = go.Figure()
    fig_stack.add_trace(go.Bar(name="Modifiées",  x=diff_sum["langage"], y=diff_sum["modifiees"],  marker_color="#636EFA"))
    fig_stack.add_trace(go.Bar(name="Ajoutées",   x=diff_sum["langage"], y=diff_sum["ajoutees"],   marker_color="#00CC96"))
    fig_stack.add_trace(go.Bar(name="Supprimées", x=diff_sum["langage"], y=diff_sum["supprimees"], marker_color="#EF553B"))
    fig_stack.update_layout(barmode="stack", height=350)
    st.plotly_chart(fig_stack, use_container_width=True)



# ============================================================
# ROW 3 — DÉTAIL PAR TEST
# ============================================================
st.markdown("---")
st.subheader("🔎 Détail par test")


col_e, col_f = st.columns([1, 3])


with col_e:
    langage_detail = st.selectbox("Langage", options=langages_sel)


df_detail = df_filtre[df_filtre["langage"] == langage_detail].sort_values("test")


with col_f:
    if not df_detail.empty:
        fig_detail = px.bar(
            df_detail,
            x       = "test",
            y       = "similarite",
            color   = "similarite",
            text    = "similarite",
            range_y = [0, 100],
            color_continuous_scale    = "RdYlGn",
            color_continuous_midpoint = 50
        )
        fig_detail.update_traces(textposition="outside")
        fig_detail.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_detail, use_container_width=True)
    else:
        st.info("Aucun test disponible pour ce langage.")



# ============================================================
# TABLE COMPLÈTE
# ============================================================
st.markdown("---")
st.subheader("📋 Tableau complet")


colonnes_table = [
    "execution", "date", "langage", "test",
    "similarite", "total_diff",
    "modifiees", "ajoutees", "supprimees",
    "lignes_entree", "lignes_sortie"
]
if "extraction_bloc_md" in df_filtre.columns:
    colonnes_table.append("extraction_bloc_md")

df_display = df_filtre[colonnes_table].sort_values(["langage", "test"])


st.dataframe(
    df_display,
    use_container_width = True,
    hide_index          = True,
    column_config       = {
        "similarite" : st.column_config.ProgressColumn("Similarité %", min_value=0, max_value=100),
        "total_diff" : st.column_config.NumberColumn("Total diff", format="%d"),
        "modifiees"  : st.column_config.NumberColumn("Modif",      format="%d"),
        "ajoutees"   : st.column_config.NumberColumn("Ajout",      format="%d"),
        "supprimees" : st.column_config.NumberColumn("Suppr",      format="%d"),
        "extraction_bloc_md": st.column_config.CheckboxColumn("Extrait via bloc MD"),
    }
)



# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption(f"📁 Source : {RESULTS_DIR.resolve()} | 🔄 Utilise le bouton sidebar pour actualiser")
