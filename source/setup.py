from setuptools import setup
import sys
import Modules.path as path
sys.path.append(path.module_path)


def get_requires(path):
    try:
        with open(path) as f:
            return [pkg.strip() for pkg in f.readlines()]
    except Exception as e:
        print(e)


if __name__ == "__main__":
    requires = get_requires(path.requirements_path)
    try:
        setup(requires)
        print("正常にセットアップが完了しました.")
    except Exception as e:
        print(e)
