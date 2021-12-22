import argparse
from pathlib import Path

def create_parser():
    class ConfigExistsAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string) -> None:
            if Path(values).exists():
                setattr(namespace, self.dest, values)
            else:
                raise argparse.ArgumentError(self, "Config not found at specified path")

    parser = argparse.ArgumentParser()

    parser.add_argument("--running-config", action=ConfigExistsAction, required=True)
    parser.add_argument("--controlled-config", action=ConfigExistsAction, required=True)
    parser.add_argument("--verbose", action="store_true")

    return parser