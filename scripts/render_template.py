#!/usr/bin/env python3
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

root = Path(__file__).resolve().parents[1]
tpl_dir = root / 'roles' / 'common' / 'templates'
out_dir = root / 'web' / 'dist'
out_dir.mkdir(parents=True, exist_ok=True)

env = Environment(loader=FileSystemLoader(str(tpl_dir)))
tpl = env.get_template('fancy_index.html.j2')

# Provide defaults akin to Ansible vars/facts to keep the page consistent
context = {
    'env_name': os.environ.get('ENV_NAME', 'dev'),
    'inventory_hostname': os.environ.get('HOSTNAME', 'web1'),
    'primary_domain': os.environ.get('PRIMARY_DOMAIN', 'local'),
    'ansible_distribution': os.environ.get('DISTRO', 'GNU/Linux'),
    'ansible_distribution_version': os.environ.get('DISTRO_VERSION', ''),
    'ansible_kernel': os.environ.get('KERNEL', ''),
    'ansible_default_ipv4': {
        'address': os.environ.get('IP', '127.0.0.1')
    },
}

html = tpl.render(**context)
(out_dir / 'index.html').write_text(html, encoding='utf-8')
print(f"Rendered to {out_dir / 'index.html'}")
