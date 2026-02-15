# Règles de Bonne Conduite - Projet ProWeb

## 1. Principes de Code

- **Langue** : Commenter le code en français, de façon simple et concise.
- **Modernité** : Utiliser les syntaxes les plus modernes (Optional Chaining, Type Hinting strict en Python, Methodes fonctionnelles .map/.filter).
- **Simplicité** : Éviter l'Over-engineering. Préférer les structures simples et robustes.
- **Efficacité** : Utiliser des `early returns` pour éviter l'imbrication profonde. Pas de code boilerplate inutile.

## 2. Nommage et Clarté

- **Intention métier** : Utiliser des noms qui décrivent l'intention (ex: `validatedUserEmail` au lieu de `data`).
- **Focus sur le "Pourquoi"** : Ne pas commenter ce que fait le code si c'est explicite. Expliquer les raisons des choix techniques ou les cas complexes.
- **Minimalisme** : Pas de JSDoc ou Docstrings pour des fonctions triviales.

## 3. Travail Collaboratif (CRITIQUE)

- **Migrations** : Ne jamais créer ou modifier des migrations qui impactent les autres sans coordination. Utiliser les migrations existantes si possible.
- **Configuration** : Respecter scrupuleusement le `GUIDE_CONFIGURATION.md`. Utiliser le fichier `.env` pour les variables locales.
- **Git** : Maintenir un historique propre. Vérifier le `.gitignore` avant de commiter.
- **Partage** : Toujours faire un `git pull` avant de commencer à travailler pour éviter les conflits.

## 4. Sécurité

- Ne jamais versionner de secrets (clés API, mots de passe).
- Vérifier que le fichier `.env` est bien listé dans le `.gitignore`.
