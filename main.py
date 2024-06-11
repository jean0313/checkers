import sys
from cert import CertDependency
from database_mysql import MySQLDependency
from database_pg import PostgreSQLDependency
from network import NetworkDependency
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml


def load_dependencies(yaml_file):
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)['dependencies']

# Factory to create dependency objects
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

def main(yaml_file):
    dependencies = load_dependencies(yaml_file)
    results = []
    # for item in dependencies:
    #     dependency = dependency_factory(item)
    #     code = dependency.check()
    #     if code != 0:
    #         return code
    # return 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(dependency_factory(item).check) for item in dependencies]
        for future in as_completed(futures):
            results.append(future.result())

    return sum(results)


if __name__ == '__main__':
    try:
        sys.exit(main('deps.yaml'))
    except ValueError:
        sys.exit(1)