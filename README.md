# IBM i / RPGLE Fully Free LLM Test Suite

Repository for testing and fine‑tuning IBM Granite 4.1 8B on **fully‑free RPGLE**, CL and SQL running on IBM i / AS400, via **Ollama + RAG**.

---

## 🎯 Objectif

- Tester la qualité des réponses de `granite4.1:8b` sur du **RPGLE full‑free** (100 % modern ILE RPG), CL et SQL IBM i.  
- Vérifier **avant** tout fine‑tuning :  
  - performances, cohérence, hallucinations.  
  - qualité des réponses générales sur IBM i / AS400 (langages, concepts, bonnes pratiques).  
- Construire un **benchmark propre** (RPGLE full‑free, CL, SQL) basé sur :
  - des tests unitaires RPGLE full‑free,  
  - et du **RAG sur la documentation IBM i** (PDFs officiels, guides, SQL Reference, CL, etc.).  
- Après le fine‑tuning et le nouveau RAG (avec les fichiers utilisés pour le finetuning), refaire **les mêmes tests** et comparer les résultats (diff réponses avant / après) pour mesurer l’amélioration.

---

## 🧪 Méthodologie

1. **Tests pré‑fine‑tuning**  
   - Lancer une série de **tests RPGLE full‑free, CL, SQL** sur le modèle **brut** (ou déjà modifié via `Modelfile`).  
   - RAG : indexation des **PDF IBM i** (RPG guide, SQL reference, CL docs, etc.)  
     → aider le modèle à générer de bonnes réponses sans fine‑tuning lourd.  
   - Stocker les réponses dans `results/*.jsonl` avec un `verdict` (`good` / `partial` / `bad`).

2. **RAG “enrichi” post‑fine‑tuning**  
   - Ajouter dans la base de connaissances RAG :  
     - les **fichiers / extraits** utilisés pour le fine‑tuning (tests RPGLE full‑free, exemples CL/SQL, etc.).  
   - Cela permet au modèle de combiner :
     - le **savoir baked‑in** du fine‑tuning,  
     - et le **contexte explicite** via RAG.

3. **Diffs avant / après fine‑tuning**  
   - Relancer **exactement les mêmes tests** sur le modèle **après** fine‑tuning + RAG enrichi.  
   - Comparer les réponses (avant / après) pour :
     - réduire les hallucinations,  
     - stabiliser le style de réponse IBM i / AS400,  
     - améliorer la précision SQL / RPG / CL.

---

## 📁 Structure du repo

```text
.
├── README.md
├── tests/
│   ├── rpg_free_tests.jsonl         # questions RPGLE full‑free
│   ├── cl_tests.jsonl              # questions CL
│   ├── sql_tests.jsonl             # questions SQL DB2 for i
│   └── prompts/
│       ├── rpg_free_001.rpgle      # exemple de code RPGLE full‑free
│       └── cl_simple_001.cl        # exemple CL simple
├── results/
│   ├── rpg_free_results.jsonl      # réponses Granite RPGLE full‑free AVANT
│   ├── rpg_free_results_ft.jsonl   # réponses Granite APRÈS fine‑tuning
│   ├── rags/
│       └── context_rpg_free_001.txt # extraits RAG + fichiers utilisés pour fine‑tuning
└── notebooks/
    └── benchmark_granite.ipynb     # scripts Python API Ollama + RAG + diffs
```

---

## 🔧 Comment lancer un test

1. Lancer Ollama avec ton modèle Granite 4.1 8B (CPU ou GPU) :

   ```powershell
   ollama run granite4.1-ibmi-8b
   ```

2. Copier‑coller le **prompt de test RPGLE / CL / SQL** dans le terminal Ollama.

3. Copier la réponse Granite dans:

   - `results/rpg_free_results.jsonl` (avant fine‑tuning).  
   - `results/rpg_free_results_ft.jsonl` (après fine‑tuning).

   avec champs `id`, `model`, `response`, `verdict` (`good` / `partial` / `bad`).

---

## 💡 Utilisation pour fine‑tuning

- Les paires `(prompt, réponse correcte)` format **chat** (RPGLE full‑free, CL, SQL)  
  servent à l’**instruction‑tuning** de Granite 4.1 8B (QLoRA / Lora).  
- Les **extraits PDF IBM i** (RPGLE guide, SQL ref, CL docs) sont indexés en **RAG**  
  pour aider Granite à générer de bonnes réponses avant fine‑tuning.

---

## ⚡ Prochaines étapes (conseillées)

- Ajouter **5–10 tests RPGLE full‑free** classiques (boucles, SQL, procs…).  
- Lancer le **benchmark manuel** avec Granite 4.1 8B et annoter `verdict`.  
- Utiliser `results/*.jsonl` pour construire un **dataset d’instruction‑tuning Granite**  
  (format `messages = [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]`).  
- Après fine‑tuning + RAG enrichi, ré‑exécuter le même benchmark et **comparer les réponses** (avant / après).
