import sys
import click
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
from registry import check_registry
import checks.network_check  # Ensure all checks are imported
import checks.cert_check
import checks.database_mysql_check
import checks.database_postgre_check
import checks.echo_check

def load_dependencies(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data.get('dependencies', [])

def check_dependencies(dependencies):
    results = {}
    for dep in dependencies:
        check_class = check_registry.get(dep['type'])
        if check_class:
            if dep['type'] == 'database':
                db_type = dep.get('db_type')
                check_class = check_registry.get(f"{dep['type']}_{db_type}")
                description = f"{dep['type'].capitalize()}-{db_type}"
            else:
                description = f"{dep['type'].capitalize()}"
            check_instance = check_class(**dep)
            status, result = check_instance.check()
            if status > 0:
                results[description] = result
        else:
            results[f"Unknown {dep['type']}"] = "No check available"
    return results

@click.command()
@click.option('--file', '-f', default='deps.yaml', help='Config file of checkers', show_default=True)
@click.option('--parallel', '-p', default=False, help='Execute checkers in parallel', show_default=True)
@click.option('--exit_on_error', '-e', default=False, help='Exit on error', show_default=True)
def check(file, parallel, exit_on_error):
    results = []
    dependencies = load_dependencies(file)
    if parallel:
        print('executing in parallel mode')
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for dep in dependencies:
                check_instance = get_check_instance(dep)
                futures.append(executor.submit(check_instance.check))
            for future in as_completed(futures):
                status, msg = future.result()
                results.append(status)
    else:
        print('executing in sync mode')
        for dep in dependencies:
            check_instance = get_check_instance(dep)
            status, result = check_instance.check()
            if status > 0 and exit_on_error:
                sys.exit(1)
            else:
                results.append(status)
    sys.exit(sum(results))

def get_check_instance(dep):
    check_class = check_registry.get(dep['type'])
    if not check_class:
        if dep['type'] == 'database':
            db_type = dep.get('name')
            check_class = check_registry.get(f"{dep['type']}_{db_type}")
    return check_class(**dep)

if __name__ == '__main__':
    check()