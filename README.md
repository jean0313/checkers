### Checkers for pre-deployment


### Help
```
Usage: checkers.py [OPTIONS]

Options:
  -f, --file TEXT              Config file of checkers  [default: deps.yaml]
  -p, --parallel BOOLEAN       Execute checkers in parallel  [default: False]
  -e, --exit_on_error BOOLEAN  Exit on error  [default: False]
  --help                       Show this message and exit.
```

### Run
```shell
# install deps
pip install click pyyaml mysql-connector-python psycopg2-binary

# run checkers
python3 checkers.py
```


