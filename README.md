# Infrastructure Ansible — TP Jour 3

Ce dépôt contient l’implémentation du TP Jour 3 : déploiement d’une webapp via un rôle dédié et gestion des secrets avec Ansible Vault.

## Structure
- `docker-compose.yml` : conteneurs de lab
- `inventory.ini` : inventaire de base
- `roles/webapp` : rôle de déploiement de l’application
- `deploy-webapp.yml` : playbook principal
- `revision-playbook.yml` : scénario de mise à jour
- `secrets.yml` : variables chiffrées avec Vault
- `test-vault.yml` : playbook de test du chiffrement

## Démarrage du lab
```bash
docker compose up -d
ansible -i inventory.ini all -m ping
```

## Exécution
```bash
ansible-playbook -i inventory.ini deploy-webapp.yml --ask-vault-pass
```

## Gestion des secrets
- `ansible-vault view secrets.yml`
- `ansible-vault edit secrets.yml`
- Utilisation de `--ask-vault-pass` pour déchiffrer à l’exécution

## Fonctionnalités
- Déploiement d’une application web via un rôle unique
- Séparation des paramètres sensibles avec Ansible Vault
- Playbook de révision pour rejouer une configuration

## Nettoyage
```bash
docker compose down -v
```
