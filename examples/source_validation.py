from jsonschema import validate
import pathlib
import yaml

APP_ROOT = pathlib.Path.cwd()

SCHEMA_DIR = APP_ROOT / "schema"
EXAMPLES_DIR = APP_ROOT / "examples"

if __name__ == "__main__":
    with open(SCHEMA_DIR / "experiment.yml") as ysf:
        experiment_schema = yaml.safe_load(ysf)
    with open(EXAMPLES_DIR / "experiment1.yml") as ye1f:
        experiment_record = yaml.safe_load(ye1f)
    validate(experiment_record, experiment_schema)
