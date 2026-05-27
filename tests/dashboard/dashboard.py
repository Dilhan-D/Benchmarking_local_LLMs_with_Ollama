#!/usr/bin/env python3
"""
Dashboard Streamlit - Ollama Granite Test Series
Visualise les résultats des comparaisons RPGLE / CLLE / COBOL
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

@st.cache_data
def charger_donnees():
    frames = []
    for langage, path in SOURCES.items():
        if path.exists():
            try:
                df = pd.read_csv(path, sep=';')
            except Exception:
                df = pd.read_csv(path, sep=',')
            frames.append(df)
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
    st.error("Aucun CSV trouvé. Lance d'abord les scripts de comparaison.")
    st.stop()

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

# Bouton refresh cache
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
    diff_sum = df_filtre[["langage", "modifiees", "ajoutees", "supprimees"]].groupby("langage").sum().reset_index()
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

df_display = df_filtre[[
    "execution", "date", "langage", "test",
    "similarite", "total_diff",
    "modifiees", "ajoutees", "supprimees",
    "lignes_entree", "lignes_sortie"
]].sort_values(["langage", "test"])

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
    }
)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption(f"📁 Source : {RESULTS_DIR.resolve()} | 🔄 Utilise le bouton sidebar pour actualiser")