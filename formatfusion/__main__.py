import typing as t

import docopt

from formatfusion import main


def __main__(argv: t.Optional[t.Any] = None) -> None:
    main.main(docopt.docopt(main.__doc__, argv=argv, options_first=True))


if __name__ == "__main__":
    __main__()
