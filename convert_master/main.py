"""
Usage:
  main.py run <input_file> [--output=<output_file>]

Options:
  -h --help                Show helps.
  --output=<output_file>   Output YAML file [default: output.yaml].
"""
import logging

from docopt import docopt
from converting import Converting, logger

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("../app.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


def main():
    arguments = docopt(__doc__)
    input_file = arguments['<input_file>']
    output_file = arguments['--output']

    convert = Converting(input_file, output_file)
    logging.info("The conversion has started...")
    try:
        convert.run()
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
