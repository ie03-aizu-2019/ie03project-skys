from setuptools import setup, find_packages
import sys
import Modules.path as path
sys.path.append(path.module_path)


def get_requires(path):
    with open(path) as f:
        return [pkg_name.strip() for pkg_name in f.readlines()]


if __name__ == "__main__":
    requires = get_requires(path.requirements_path)
    setup(requires)
