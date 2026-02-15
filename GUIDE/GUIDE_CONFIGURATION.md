# Guide de Configuration du Projet ProWeb

Dans ce projet, nous utilisons des variables d'environnement pour gérer la configuration de la base de données. Cela nous permet d'utiliser chacun notre propre SGBD (MySQL, PostgreSQL, etc.) sans créer de conflits entre nous.

## 1. Prérequis

Nous devons nous assurer d'avoir Python installé et notre environnement virtuel activé.

```bash
# Windows
.\venv\Scripts\activate
```

## 2. Configuration de la Base de Données

On doit créer un fichier nommé `.env` dans le dossier `asproject/` (celui qui contient `manage.py`).

⚠️ **Important** : Nous devons impérativement placer ce fichier à cet emplacement, sinon Django ne pourra pas le charger.

On y copie le contenu suivant en l'adaptant à notre configuration locale :

### Pour MySQL (Configuration actuelle de l'équipe)

```ini
# Configuration OBLIGATOIRE
DB_ENGINE=django.db.backends.mysql
DB_NAME=proweb_bd
DB_USER=root
DB_PASSWORD=ensea  # On met ici notre mot de passe
DB_HOST=localhost
DB_PORT=3306
```

### Pour PostgreSQL (Si l'un d'entre nous l'utilise)

```ini
DB_ENGINE=django.db.backends.postgresql
DB_NAME=proweb_bd
DB_USER=postgres
DB_PASSWORD=mon_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
```

## 3. Installation des Dépendances

Nous installons les paquets requis pour que nous puissions tous travailler sur la même base :

```bash
pip install -r requirements.txt
```

_Note : Selon le SGBD qu'on choisit, nous devons installer `mysqlclient` ou `psycopg2`._

## 4. Lancement du Projet

Une fois que nous avons tout configuré :

```bash
python manage.py migrate
python manage.py runserver
```

Nous sommes maintenant prêts à développer ensemble ! 🚀
