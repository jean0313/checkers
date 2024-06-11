# -*- encoding: utf-8 -*-
import sys

import click
from cert import CertDependency
from database_mysql import MySQLDependency
from database_pg import PostgreSQLDependency
from network import NetworkDependency
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml


def load_dependencies(yaml_file):
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)['dependencies']

def dependency_factory(item):
    if item['type'] == 'network':
        return NetworkDependency(item)
    elif item['type'] == 'cert':
        return CertDependency(item)
    elif item['type'] == 'database':
        db_name = item.get('name').lower()
        if db_name == 'mysql':
            return MySQLDependency(item)
        elif db_name == 'postgresql':
            return PostgreSQLDependency(item)
        else:
            raise ValueError(f"Unsupported database type: {item['name']}")
    else:
        raise ValueError(f"Unknown dependency type: {item['type']}")

@click.command()
@click.option('--file', '-f', default='deps.yaml', help='Config file of checkers', show_default=True)
@click.option('--parallel', '-p', default=False, help='Execute checkers in parallel', show_default=True)
@click.option('--exit_on_error', '-e', default=False, help='Exit on error', show_default=True)
def main(file, parallel, exit_on_error):
    dependencies = load_dependencies(file)
    results = []
    if parallel:
        print('executing in parallel mode')
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(dependency_factory(item).check) for item in dependencies]
            for future in as_completed(futures):
                results.append(future.result())
        sys.exit(sum(results))
    else:
        print('executing in sync mode')
        for item in dependencies:
            dependency = dependency_factory(item)
            code = dependency.check()
            if code != 0 and exit_on_error:
                sys.exit(code)
        sys.exit(0)

if __name__ == '__main__':
    main()