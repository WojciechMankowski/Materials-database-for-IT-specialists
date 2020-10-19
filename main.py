from dotenv import load_dotenv
from commands import *

load_dotenv()

cli.add_command(settup)
cli.add_command(add)
cli.add_command(index)
cli.add_command(category)


if __name__ == "__main__":
    cli()
