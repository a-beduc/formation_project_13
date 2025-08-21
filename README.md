## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/a-beduc/formation_project_13.git`

#### Créer l'environnement virtuel

- `cd /path/to/formation_project_13`
- `python -m venv .venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source .venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Variable d'environnement

Pour que le site fonctionne correctement, vous devez ajouter des variables 
d'environnement.

- `cd /path/to/formation_project_13`
- Créer un fichier `.env` en copiant le contenu du fichier `.env.example`.
- Modifier les valeurs d'environnement.
  - DJANGO_SECRET_KEY: Clé secrète de Django.
  - DJANGO_ALLOWED_HOSTS: Adresses de votre serveur, séparées par des virgules.
  - DEBUG: Pour activer le mode debug `True`.
  - DJANGO_SENTRY_DSN: Le DSN de Sentry pour le suivi des erreurs.

#### Exécuter le site

- `cd /path/to/formation_project_13`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `pip install --requirement requirements.dev.txt`
- `cd /path/to/formation_project_13`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `pip install --requirement requirements.dev.txt`
- `cd /path/to/formation_project_13`
- `source venv/bin/activate`
- `pytest --cov="."`

#### Base de données

Plusieurs bases de données sont disponibles.

- `data/oc-lettings-site.sqlite3`; Pour le lancement en local.
- `data_clean/oc-lettings-site.sqlite3`; Base de donnée vide. 
- `data_demo/oc-lettings-site.sqlite3`; Utilisée pour le build de démo.

Selon la base de donnée, vous pouvez modifier le chemin pour vous connecter.

- `cd /path/to/formation_project_13`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open data/oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Docker

#### Images disponibles

+ `abeduc/oc-lettings`: base de donnée vide.
+ `abeduc/oc-lettings-demo`: base de donnée de démo.

#### Prérequis

+ Créer un `.env` comme précisé en [Variable d'environnement](#variable-denvironnement).
+ En cas de problème, vérifier que le port `8000` est libre.

#### Utiliser Docker Compose (recommandé)

Avec une base de donnée intégrée.
+ Naviguer dans un dossier vide.
+ Dans un nouveau dossier ajouter le .env créé précédement.
+ Télécharger le fichier `docker-compose.demo.yaml`
+ Lancer l'application `docker compose -f docker-compose.demo.yaml up`

Avec une base de donnée vide et un volume persistant.
+ Naviguer dans un dossier vide.
+ Dans un nouveau dossier ajouter le .env créé précédement.
+ Télécharger le fichier `docker-compose.yaml`
+ Créer un volume vide `docker volume create empty-volume`
+ Lancer l'application `docker compose -f docker-compose.yaml up`

#### Construire une nouvelle image

- `cd /path/to/put/project/in`
- `git clone https://github.com/a-beduc/formation_project_13.git`
- `cd /formation_project_13`
- Ajouter le .env créé précédement.
- Construire l'image "clean" ou de démo
  - clean: `docker build -f Dockerfile -t <docker-username>/oc-lettings:local
  - demo: `docker build -f Dockerfile.demo -t <docker-username>/oc-lettings:local
- Lancer l'image
  - clean: `docker run --env-file .env -p 8000:8000 --name oclettings abeduc/oc-lettings:local`
  - demo: `docker run --env-file .env -p 8000:8000 --name oclettings-demo abeduc/oc-lettings-demo:local`

### Deployment

Le déploiement se fait sur Render à partir de l'image construite par GitHub Actions.

Pipeline CI/CD (branche `master`)
- Execution du lint (Ruff).
- Execution des tests (Pytest).
- Build des images Docker (clean & demo).
- Push sur Docker Hub.
- Déclenchement du redeploy sur Render (Deploy Hook).

Prérequis:
- Avoir un compte GitHub avec les permissions nécessaires sur le dépôt.
- Un compte Docker Hub.
- Les variables et secrets d'environnements configurés pour GitHub.
  - Secrets:
    - DJANGO_SECRET_KEY: La clé secrète Django.
    - DJANGO_SENTRY_DSN: Le DSN de Sentry pour le suivi des erreurs.
    - DOCKERHUB_TOKEN: Un token d'authentification pour docjer.
  - Variables d'environnement:
    - DOCKERHUB_IMAGE_CLEAN: Le nom de l'image sans donnée (oc-lettings).
    - DOCKERHUB_IMAGE_DEMO: Le nom de l'image avec des données (oc-lettings-demo).
    - DOCKERHUB_REPO: Le nom du dépôt dockerhub (souvent le nom d'utilisateur du compte DockerHub).
    - DOCKERHUB_USERNAME: Le nom d'utilisateur pour le compte DockerHub
    - RENDER_DEPLOY_HOOK: URL fournie par Render pour déclencher un redéploiement.


### Documentation

La documentation est publiée sur Read the Docs: [Documentation](https://formation-project-13.readthedocs.io/en/latest/)
