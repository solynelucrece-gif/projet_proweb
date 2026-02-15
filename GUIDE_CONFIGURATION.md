# Guide de Configuration du Projet

Ce projet utilise des variables d'environnement pour gérer la configuration de la base de données, permettant à chaque développeur d'utiliser son propre SGBD (MySQL, PostgreSQL, etc.) sans conflit.

## 1. Prérequis

Assurez-vous d'avoir Python installé et votre environnement virtuel activé.

```bash
# Windows
.\venv\Scripts\activate
```

## 2. Configuration de la Base de Données

Créez un fichier nommé `.env` dans le dossier `asproject/` (celui qui contient `manage.py`).

⚠️ **Important** : Ce fichier doit impérativement se trouver à cet emplacement, sinon Django ne pourra pas le charger.

Copiez-y le contenu suivant et adaptez-le à votre configuration :

### Pour MySQL (Utilisateur actuel)

```ini
# Configuration OBLIGATOIRE (pas de valeur par défaut)
DB_ENGINE=django.db.backends.mysql
DB_NAME=proweb_bd
DB_USER=root
DB_PASSWORD=ensea  # Votre mot de passe ici
DB_HOST=localhost
DB_PORT=3306
```

### Pour PostgreSQL (Exemple pour vos collègues)

```ini
DB_ENGINE=django.db.backends.postgresql
DB_NAME=proweb_bd
DB_USER=postgres
DB_PASSWORD=mon_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
```

## 3. Installation des Dépendances

Installez les paquets requis :

```bash
pip install -r requirements.txt
pip install python-dotenv
```

_Note : Si vous utilisez MySQL, installez `mysqlclient`. Si vous utilisez PostgreSQL, installez `psycopg2`._

## 4. Lancement

Une fois configuré :

```bash
python manage.py migrate
python manage.py runserver
```
