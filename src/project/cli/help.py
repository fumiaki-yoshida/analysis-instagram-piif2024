def run_help(cfg):
    print(
        """Usage: poetry run script <arguments>
  This script is built with Hydra.
  See details here: https://hydra.cc/docs/intro/

  This project's Hydra config files are stored under `<project>/conf/`.
  You can customize this script's behavior by updating config files."""
    )
