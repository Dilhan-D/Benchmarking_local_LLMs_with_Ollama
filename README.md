# Projet Personnel: Fine-Tuning et Tests sur Granite 4.1:8b avec LLM IBM

## A propos

Ce dépôt contient le code, les scripts et les documents nécessaires pour réaliser un projet personnel visant à explorer la fine-tuning et l'interrogation de recherche assistée par contenu (RAG) sur le moteur Granite 4.1:8b fourni par IBM. Le but principal est d'évaluer les performances et les capacités du modèle dans un écosystème IBM i, avec une perspective future sur son utilisation.

Dans un second temps, essayer de lui passer des instructions afin de lui donner du contexte sur son rôles et évaluer son comportement et ses réponses.

## Contexte

- **École**: Epitech (Alternance)
- **Projet**: Fine-tuning et tests sur Granite 4.1:8b
- **Raison de choisir IBM**: Initialement pour des tests dans un écosystème IBM i, avec une perspective future.
- **Moteur Utilisé**: Granite 4.1:8b

## Structure du Dépôt

```
README.md                # Ce document
fine_tuning/            # Scripts et configurations pour le fine-tuning
tests/                  # Scripts et rapports des tests avant et après fine-tuning
rag/                    # Implémentation de la recherche assistée par contenu (RAG)
docs/                   # Documentation PDFs et autres ressources
generel_questions/      # Répertoire pour les questions générales
rpgle_questions_before_finetune # Question rpgle avant d'entrainer le modèle
   - answers_before_finetune 
   - questions_before_finetune
questions_and_answers/  # Répertoire pour les questions techniques et leurs réponses
```

## Contenu

### `fine_tuning/`
Ce répertoire contient tous les scripts nécessaires pour le processus de fine-tuning du modèle Granite 4.1:8b.
- **`setup.py`**: Script pour initialiser l'environnement de fine-tuning.
- **`train_model.py`**: Script principal pour effectuer le fine-tuning.
- **`config.json`**: Fichier de configuration pour ajuster les paramètres de training.

### `tests/`
Ici, vous trouverez les scripts et rapports des tests réalisés avant et après la phase de fine-tuning.
- **`pre_finetune_tests.py`**: Scripts pour évaluer les performances du modèle avant le fine-tuning.
- **`post_finetune_tests.py`**: Scripts pour évaluer les performances post-fine-tuning.
- **`test_reports/`**: Répertoire contenant les rapports des tests.

### `rag/`
Ce dossier implémente la recherche assistée par contenu (RAG) sur le modèle fine-tuned.
- **`rag_setup.py`**: Script pour configurer l'implémentation de RAG.
- **`query_processor.py`**: Script principal pour traiter les requêtes via RAG.

### `docs/`
Ce répertoire contient tous les documents PDF et autres ressources nécessaires pour comprendre le projet et les tests effectués.
- **`project_overview.pdf`**: Vue d'ensemble du projet.
- **`test_data.pdf`**: Description des données utilisées pour les tests.
- **`results_analysis.pdf`**: Analyse des résultats avant et après fine-tuning.

### `generel_questions/`
Ce répertoire est dédié aux questions générales

### `questions_and_answers/`
Ce répertoire contient les questions et réponses techniques liées au projet.

## Méthodologie

1. **Préparation Initiale**:
   - Installer l'environnement requis pour Granite 4.1:8b sur un système IBM i.
   - Rassembler les données d'entraînement pertinentes pour le fine-tuning.

2. **Fine-Tuning**:
   - Exécuter `train_model.py` avec la configuration spécifiée dans `config.json`.
   - Surveiller le processus de training et ajuster les paramètres si nécessaire.

3. **Tests Initiaux**:
   - Utiliser `pre_finetune_tests.py` pour évaluer les performances du modèle avant le fine-tuning.
   - Documenter les résultats dans `test_reports/`.

4. **RAG Implémentation**:
   - Configurer et exécuter l'implémentation de RAG via `rag_setup.py`.
   - Tester la capacité du modèle à fournir des réponses contextuelles.

5. **Tests Post-Fine-Tuning**:
   - Utiliser `post_finetune_tests.py` pour évaluer les performances post-fine-tuning.
   - Comparer avec les résultats initiaux et documenter les améliorations ou dégradations.

6. **Analyse des Résultats**:
   - Analyser les données collectées dans `test_reports/`.
   - Identifier les points forts et faibles des langages IBM dans ce contexte.

## Transparence

Ce dépôt sera maintenu aussi transparent que possible, avec une documentation détaillée de chaque étape du processus. Tous les scripts et configurations seront open-sourced pour permettre une réutilisation et un examen par la communauté.

## Contribuer

Si vous souhaitez contribuer ou avoir des questions sur ce projet, n'hésitez pas à créer une issue ou à envoyer un pull request. Vos retours seront grandement appréciés!

---

*Remarque: Ce README est généré en fonction des réponses du modèle et sera mis à jour après chaque étape de test et de fine-tuning pour maintenir la transparence et l'exactitude.*
