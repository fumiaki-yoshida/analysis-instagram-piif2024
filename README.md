# Analysis workspace

## Prerequisites

- [Poetry](https://python-poetry.org/): Dependency manager

## Getting started

### Initialize project

This project needs to be initialized before working on. This step is required only when creating a project from this template.

To initialize this project, please run `bin/init-project <project name>`.
Please make sure the initialization finishes successfully. And you will need to commit the changes added by the initialization script.

### Setup

This step is required after checking out this project on each environment.

    $ bin/setup

After setting up on your environment, you can run, for example, Jupyter Lab like this:

    $ poetry run jupyter lab # Open Jupyter Lab on your browser

That's it! 🚀

## Data version control

This project uses DVC as a version control system for data. See details: https://dvc.org/

## Configurations

This project uses [Hydra](https://hydra.cc/) to read & parse config files.

Please put configuration files under the [`conf` directory](./conf/config.yaml).

## Project scripts

To define Python scripts that run as a CLI, extend the `project.cli` package.

You can execute the CLI with this command:

    $ poetry run script

This CLI is implemented to execute a command.
List of commands is defined in [src/project/cli/__init__.py](src/project/cli/__init__.py).

A command to be executed is determined with the `command` config in Hydra configuration files.
`help` is the default value of the `command` config, so `poetry run script` shows a help text.

You can override the `command` config by passing an argument as follows:

    $ poetry run script command=another-command

## Scripts for development

- [`bin/format`](./bin/format): Format Python source code

## Installing a new package

If you want to use any package, you can add it as a dependency:

    $ poetry add <package-name>

Normally, this add some changes to `pyproject.toml` and `poetry.lock` so please don't forget to commit these changes.

## Clearing outputs in notebooks

It is important to clear outputs before adding notebook files to Git to make files smaller and for more readable diffs.

To help this, this project has the `./bin/clear-notebook-output` script.

If you wish clearing outputs on all notebooks, you can run the script with no arguments:

    $ ./bin/clear-notebook-output

Or, you can also specify file names to clear outputs on specific files like this:

    $ ./bin/clear-notebook-output notebook1.ipynb notebook2.ipynb

## Shared tools

This project uses [analysis-workspace-tools](https://github.com/NEWROPE/analysis-workspace-tools) to share the workflow with other analysis workspaces.

You can see the list of the available commands provided by the submodule by executing [./bin/run](./bin/run) with no arguments.

Please refer to the documentation in the project for more details: https://github.com/NEWROPE/analysis-workspace-tools
