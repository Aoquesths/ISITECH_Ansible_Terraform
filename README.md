# Infrastructure Ansible TP2

Ce dépôt contient l’implémentation du TP2 : introduction aux rôles et déploiement d’une base de données MySQL avec Ansible.

## Structure
- `docker-compose.yml` : lab avec hôtes applicatifs et base de données
- `inventory` : inventaire de test
- `playbooks/mysql.yml` : playbook principal pour MySQL
- `roles/mysql` : rôle dédié à l’installation et configuration MySQL
- `requirements.yml` : dépendances éventuelles de rôles externes

## Démarrage du lab
```bash
docker compose up -d
ansible -i inventory all -m ping
```

## Exécution
```bash
ansible-playbook -i inventory playbooks/mysql.yml
```

## Fonctionnalités
- Installation de MySQL dans un conteneur
- Configuration initiale du serveur
- Création de bases de données et d’utilisateurs
- Introduction à la structuration par rôles

## Nettoyage
```bash
docker compose down -v
```
