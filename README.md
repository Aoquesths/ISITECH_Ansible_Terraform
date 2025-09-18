# Infrastructure Ansible TP1

Ce dépôt contient l’implémentation du TP1 : mise en place d’un laboratoire Ansible simple avec Docker et déploiement initial d’un service web.

## Structure
- `docker-compose.yml` : création des conteneurs de lab (nœuds de test)
- `inventory` : inventaire de base pour cibler les hôtes
- `playbooks/` : premiers playbooks (ping, installation Nginx)

## Démarrage du lab
```bash
docker compose up -d
ansible -i inventory all -m ping
```

## Exécution
```bash
ansible-playbook -i inventory playbooks/nginx.yml
```

## Fonctionnalités
- Vérification de la connectivité avec le module `ping`
- Installation d’un Nginx minimal
- Premiers tests de communication entre Ansible et les conteneurs

## Nettoyage
```bash
docker compose down -v
```
