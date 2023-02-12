import argparse
import json
import sys
import inspect

import yaml

import pyDeco.utils as util

sys.path.insert(0, "../../")

logger = util.init_logger(__name__)

# Override argparse.ArgumentParser
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        logger.error(
            f"\n{util.bcolors.FAIL}Traceback: {message}.\n    See below for help.{util.bcolors.ENDC}\n\n[USAGE]"
        )
        self.print_help()
        print()
        self.exit(0)


# add --json to argparse for cli
def add_json_arguments(parser):
    parser.add_argument("--json", type=str, required=True, help="/path/to/file.json")


# read cli input parameters from json file
def cli_json(arg_parser_func: callable = add_json_arguments):
    parser = ArgumentParser()
    arg_parser_func(parser)
    parsed_args = parser.parse_args()
    json_path = parsed_args.json

    def read_json(func: callable, json_path: str = json_path):
        def wrapper(*args, **kwargs):
            with open(json_path, "rb") as f:
                params = json.load(f)

            sig = inspect.signature(func)
            func_args = sig.parameters

            if len(func_args) != len(params.keys()):
                logger.error(
                    f"\n{util.bcolors.FAIL}Traceback:\n    File '{inspect.stack()[1][1]}', line {inspect.stack()[1][2]}, in {func.__name__}: \nParameters do not match. Expected {[arg for arg in func_args.keys()]} but got {[arg for arg in params.keys()]}{util.bcolors.ENDC}"
                )
                exit()

            return func(**params)

        return wrapper

    return read_json


# add --yaml to argparse for cli
def add_yaml_arguments(parser):
    parser.add_argument("--yaml", type=str, required=True, help="/path/to/file.yaml")


# read cli input parameters from yaml file
def cli_yaml(arg_parser_func: callable = add_yaml_arguments):
    parser = ArgumentParser()
    arg_parser_func(parser)
    parsed_args = parser.parse_args()
    json_path = parsed_args.yaml

    def read_yaml(func: callable, json_path: str = json_path):
        def wrapper(*args, **kwargs):
            with open(json_path, "r") as f:
                params = yaml.safe_load(f)

            sig = inspect.signature(func)
            func_args = sig.parameters

            if list(func_args.keys()) != list(params.keys()):
                logger.error(
                    f"\n{util.bcolors.FAIL}Traceback:\n    File '{inspect.stack()[1][1]}', line {inspect.stack()[1][2]}, in {func.__name__}: \nParameters do not match. Expected {[arg for arg in func_args.keys()]} but got {[arg for arg in params.keys()]}{util.bcolors.ENDC}"
                )
                exit()

            return func(**params)

        return wrapper

    return read_yaml
