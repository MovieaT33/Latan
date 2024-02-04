"""
Main function
"""

import os
from dotenv import load_dotenv


load_dotenv("./etc/environment")


def main() -> None:
    """
    Main function
    """

    for path in os.environ["$PATH"].split(":"):
        try:
            with open(
                os.path.join(path, "bash"), "r", encoding="utf-8"
            ) as file:
                try:
                    exec(file.read(), globals())  # pylint:disable=W0122
                except KeyboardInterrupt:
                    ...

            return
        except FileNotFoundError:
            ...

    print(f"{os.path.basename(__file__)}: command not found")


if __name__ == "__main__":
    main()
