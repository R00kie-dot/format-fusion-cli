"""
Usage:
  format-fusion [options...] <command> [<args>...]
  format-fusion (-h | --help)

Global options:
    -h --help                Show helps.

Commands:
    yaml                    Converting JSON to YAML.
    image                   Converting image to Base64.
"""
import json
import logging

from docopt import docopt

from formatfusion import commands

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


def run_command(opts):
    command_name = opts["<command>"]
    match command_name:
        case "yaml":
            cmd_module = commands.cmd_yaml
        case "image":
            cmd_module = commands.cmd_image
        case _:
            raise RuntimeError(f"Invalid command <{command_name}>")

    cmd_options = docopt(cmd_module.__doc__, argv=[command_name] + opts["<args>"])
    logger.debug(
        "Run command <%s> with options: %s", command_name, json.dumps(cmd_options)
    )

    return cmd_module.run(cmd_options)


def main(opts):
    logger.debug("Run app with options: %s", json.dumps(opts))

    try:
        run_command(opts)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main(docopt(__doc__, options_first=True))
