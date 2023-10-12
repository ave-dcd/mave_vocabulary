from jsonschema import validate, ValidationError
import pathlib
import yaml

APP_ROOT = pathlib.Path.cwd()

SCHEMA_DIR = APP_ROOT / "schema"
EXAMPLES_DIR = APP_ROOT / "examples"

if __name__ == "__main__":
    with open(SCHEMA_DIR / "experiment.yml") as ysf:
        experiment_schema = yaml.safe_load(ysf)
    for example_file in EXAMPLES_DIR.glob("*.yml"):
        with open(example_file) as ye1f:
            experiment_record = yaml.safe_load(ye1f)
        print("validating", example_file)
        try:
            validate(experiment_record, experiment_schema)
        except ValidationError as e:
            raise("failed to validate:", e.message)
        else:
            print("validation successful")


