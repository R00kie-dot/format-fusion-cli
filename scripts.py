import logging
import pathlib
import sys
import unittest
import coverage

import black

from isort import main as isort_main
from mypy.main import main as mypy_main

top_level_dir = pathlib.Path(__file__).parent

logging.basicConfig(
    level=logging.INFO, format="%(levelname)-7s %(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)


def lint():
    if len(sys.argv) > 1:
        logger.warning("lint not support arguments")
        logger.warning("Ignoring arguments: %s", sys.argv[1:])

    logger.info("Running isort")
    sys.argv = [
        "isort",
        str(top_level_dir / "formatfusion"),
        str(top_level_dir / "tests"),
        "--check-only",
        "--diff",
    ]
    isort_main.main()
    logger.info("Isort check passed")

    logger.info("Running black")
    sys.argv = [
        "black",
        str(top_level_dir / "formatfusion"),
        str(top_level_dir / "tests"),
        "--config",
        str(top_level_dir / "pyproject.toml"),
        "--check",
        "--diff",
        "--color",
    ]
    try:
        black.patched_main()
    except SystemExit as e:
        if e.code != 0:
            raise
    logger.info("Black check passed")

    logger.info("Running mypy")

    mypy_main(
        args=[
            str(top_level_dir / "formatfusion"),
            "--config-file",
            str(top_level_dir / "pyproject.toml"),
        ],
        clean_exit=True,
    )

    logger.info("Mypy check passed")


def format():
    if len(sys.argv) > 1:
        logger.warning("format not support arguments")
        logger.warning("Ignoring arguments: %s", sys.argv[1:])

    sys.argv = [
        "isort",
        str(top_level_dir / "formatfusion"),
        str(top_level_dir / "tests"),
    ]
    isort_main.main()

    sys.argv = [
        "black",
        str(top_level_dir / "formatfusion"),
        str(top_level_dir / "tests"),
        "--config",
        str(top_level_dir / "pyproject.toml"),
    ]
    black.patched_main()


def test():
    logging.disable(logging.INFO)

    cov = coverage.Coverage(
        source=[str(top_level_dir / "formatfusion")],
        omit=[str(top_level_dir / "tests/*")]
    )
    cov.start()

    test_dir = str(top_level_dir / "tests")
    discover_pattern = "test*.py"
    test_suite = unittest.TestLoader().discover(test_dir, pattern=discover_pattern)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    cov.stop()
    cov.save()
    cov.report()

    sys.exit(0 if result.wasSuccessful() else 1)
