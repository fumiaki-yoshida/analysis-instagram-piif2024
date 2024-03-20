import hydra

from project.cli.help import run_help

COMMANDS = {
    "help": run_help,
}


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def start(cfg):
    if cfg.command not in COMMANDS:
        raise Exception(f"Unknown command: {cfg.command}")
    COMMANDS[cfg.command](cfg)
