"""
oppiniated script to run the codegen on files we own
it encodeds undocumented expectations of this repo to make for easy builds
"""

import sys
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("genenerator")
parser.add_argument("api_namespace", nargs="+")


def run_openapi_codegen(api_namespace: str) -> None:
    sys.exit(
        subprocess.run(
            [
                *("npm", "run", "openapi-compile", "--"),
                *("-i", f"openapi/openapi.{api_namespace}.yaml"),
                f"--package-name=oapi_codegen.{api_namespace}",
            ]
        ).returncode
    )


def run_datamodel_codegen(api_namespace: str) -> None:
    sys.exit(
        subprocess.run(
            [
                "datamodel-codegen",
                f"--input=openapi/openapi.{api_namespace}.yaml",
                "--input-file-type=openapi",
                f"--output=datamodel_codegen/{api_namespace}.py",
                "--output-model-type=pydantic_v2.BaseModel",
            ]
        ).returncode
    )


generators = {
    "openapi": run_openapi_codegen,
    "datamodel": run_datamodel_codegen,
}


if __name__ == "__main__":
    args = parser.parse_args()
    gen = generators[args.genenerator]
    for api in args.api_namespace:
        gen(api)
