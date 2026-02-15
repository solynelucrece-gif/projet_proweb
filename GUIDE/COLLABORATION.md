# Guide de Collaboration et Planification - Projet ProWeb

Ce document définit la répartition des tâches et le workflow pour l'équipe, afin de garantir une collaboration efficace et le respect des délais (16 Février 2026).

## 👥 Équipe et Rôles

*   **Chœurtis** : Resp. Configuration & Backend (Infrastructure, Base de données, Sécurité)
*   **Dédé & Lucrèce** : Resp. Dashboard & Data Science (Vues, Templates, Analyse de données, Machine Learning)

---

## 📅 Roadmap Détaillée

### Phase 1 : Fondation (Déjà quasi-terminée) - **Responsable : Chœurtis**
*   ✅ Configuration de l'environnement (`.env`, `requirements.txt`)
*   ✅ Base de données (MySQL/PostgreSQL) et Migrations
*   ✅ Script d'importation des données (`remplirdb.py`)
*   ✅ Règles de Git et de bonne conduite (`.gitignore`, `.agent/rules.md`)
*   [ ] Création du superutilisateur imposé (`admin` / `AS3admin`)
*   [ ] Configuration des URLs de base (`asproject/urls.py`)

### Phase 2 : Développement du Dashboard - **Responsables : Dédé & Lucrèce**
Cette phase est le cœur du projet. Elle se divise en 3 livrables majeurs :

#### 2.1. Affichage des Données (Le "Read")
*   **Objectif** : Une page listant les données brutes de la base de manière lisible (Tableau paginé).
*   **Tâches** :
    *   Créer la vue `user_list_view` dans `dashboard/views.py`.
    *   Créer le template `user_list.html` (héritant de `base.html`).
    *   Ajouter la pagination (ex: 20 utilisateurs par page).
    *   Ajouter une fonction de recherche/filtrage simple.

#### 2.2. Les Dashboards (Visualisation)
*   **Objectif** : Deux pages de tableaux de bord distincts avec des graphiques pertinents basés sur les données (`data.csv`).
*   **Dashboard 1 (Vue Globale & Démographie)** :
    *   **KPIs** : Nombre total d'utilisateurs (50k), Age moyen, Followers moyens.
    *   **Graphiques** :
        *   Répartition géographique (Top 10 `country`).
        *   Pyramide des âges (`age`).
        *   Répartition par Profession (`employment_status`) et Revenus (`income_level`).
*   **Dashboard 2 (Comportement & Engagement)** :
    *   **KPIs** : Ratio Abonnés/Posts, Heures connectées vs Vie sociale.
    *   **Graphiques** :
        *   Type de contenu préféré (`content_type_preference`: Reels, Photos...).
        *   Thèmes favoris (`preferred_content_theme`).
        *   Corrélation : `posts_created_per_week` vs `followers_count`.
        *   Impact du `privacy_setting_level` sur le nombre d'abonnés.

#### 2.3. Machine Learning / Innovation
*   **Objectif** : Apporter une valeur ajoutée "Intelligente".
*   **Choix Validé** : **Prédiction du Potentiel Premium**
    *   **Problème** : Identifier qui est susceptible de payer un abonnement (`subscription_status`).
    *   **Données** : Utiliser Âge, Revenu, Activité, Followers.
    *   **Algorithme** : Classification (Random Forest).
*   **Tâches** :
    *   Créer un module `ml_utils.py` pour entraîner/charger le modèle.
    *   Créer une vue pour afficher le "Score Premium" d'un utilisateur.

### Phase 3 : Fonctionnalités Transverses - **Collaboration Commune**
*   **Authentification et Profil** (Dédé & Lucrèce avec support Chœurtis) :
    *   Page de Login/Logout (Django Auth).
    *   Page Profil (Modification des infos personnelles + Photo).
*   **Pages Publiques** (Dédé & Lucrèce) :
    *   Page Accueil (Présentation du projet + Membres).
    *   Page Contact (Formulaire d'envoi de mail).
*   **Rapport et Manuel** (Tout le monde) :
    *   Rédaction du manuel utilisateur PDF.
    *   Finalisation du `requirements.txt`.

---

## 🛠 Workflow de Travail

1.  **Git Flow** :
    *   Toujours faire un `git pull` avant de commencer.
    *   Travailler sur des branches si possible (ex: `feature/dashboard-dede`, `feature/config-choeurtis`), sinon communiquer avant de push sur `main`.
    *   Message de commit clair : "Ajout vue liste utilisateurs", "Correction config BD".

2.  **Standards** :
    *   Code en **Français** (Commentaires).
    *   Utiliser "Nous/On" dans les rapports.
    *   Pas de secrets dans le code.

## 🚀 Prochaines Actions Immédiates

1.  **Chœurtis** : Créer l'admin et s'assurer que l'authentification de base fonctionne.
2.  **Dédé & Lucrèce** : Créer les fichiers de base pour le Dashboard (Vues et URLs vides pour commencer) et se répartir les 2 dashboards.
