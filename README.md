# Infrastructure Ansible TP3

Ce dépôt contient l'implémentation du TP3 : déploiement d'une stack web (HAProxy + Nginx + MySQL) avec variables hiérarchiques, templates Jinja2 dynamiques et playbooks avancés.

## Structure
- docker/ : Dockerfile de base pour tous les conteneurs
- docker-compose.yml : Démarrage des hôtes de lab
- inventories/dev : Inventaire et variables d'environnement
- roles/ : Rôles Ansible (common, web, db, haproxy)
- playbooks/ : Playbooks principaux
- scripts/ : Scripts de tests

## Démarrage du lab
```bash
docker compose build
docker compose up -d
ansible -i inventories/dev/hosts.ini all -m ping
```

Rendre le script de test exécutable :
```bash
chmod +x scripts/test_load_balancer.sh
```

## Exécution complète
```bash
ansible-playbook -i inventories/dev/hosts.ini playbooks/site.yml
```

## Tests rapides
```bash
./scripts/test_load_balancer.sh http://localhost:18080 12
```

## Hiérarchie de variables
- group_vars/all.yml : variables globales (env_name, domaine, packages communs)
- group_vars/webservers.yml : tuning et vhosts Nginx
- group_vars/dbservers.yml : paramètres MySQL (databases, users, tuning)
- group_vars/loadbalancers.yml : configuration HAProxy (timeouts, algorithme, stats)
- host_vars/* : différences spécifiques (poids backend, buffer pool, overrides)

## Rôles
- common : paquets de base, utilisateur applicatif, contenu web de démo
- web : installation + configuration Nginx (templates dynamiques + block/rescue)
- db : installation MySQL + sécurisation simple + création DB/users
- haproxy : configuration dynamique basée sur l'inventaire Ansible

## Contrôles et robustesse
- Assertions préflight (OS, mémoire)
- Rolling update Nginx (serial: 1)
- Health checks HTTP et validation backend HAProxy

## Nettoyage de l'environnement
```bash
docker compose down -v
```
