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
# Install deps
pip install click pyyaml mysql-connector-python psycopg2-binary

# Run checkers
python3 checkers.py

# Specify a config
python3 checkers.py -f dependencies.yaml

# Run in parallel mode
python3 checkers.py -p true

# Exit on errors
python3 checkers.py -e true
```


