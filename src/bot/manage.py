import os
from pathlib import Path

# The base contents of the __init__.py file
INIT_FILE_CONTENTS = """from .{cog_file_name} import {cog_name}Cog"""

# The base contents of the <cog_name>.py file
COG_FILE_CONTENTS = """import nextcord
from nextcord.ext import commands


class {cog_name}Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
"""

# Characters that are not allowed in file names
INVALID_FILENAME_CHARACTERS = r'<>:"/\|?*\''


def create_valid_filename(string: str) -> str:
    """
    Converts a string to a valid filename by replacing any invalid characters with underscores and removing
    any trailing underscores.
    """
    valid_chars = [c if c not in INVALID_FILENAME_CHARACTERS else "_" for c in string]
    return "".join(valid_chars).rstrip("_")


def create_cog() -> None:
    """
    Creates a new cog with the specified name.

    The cog consists of two files: an __init__.py file and a <cog_name>.py file. The __init__.py file simply imports
    the <cog_name>Cog class from the <cog_name>.py file. The <cog_name>.py file contains the actual implementation
    of the cog.

    :param cog_name: The name of the cog to create.
    """
    # Get cog name by asking user
    cog_name = input("Enter cog name: ")

    # Convert the cog name to a valid filename
    cog_filename = create_valid_filename(cog_name)

    # Create the full path to the cog directory
    cog_dir_path = Path(__file__).parent / "cogs" / cog_filename

    try:
        # Create the cog directory
        os.mkdir(cog_dir_path)

        # Create the __init__.py file
        with open(cog_dir_path / "__init__.py", "w", encoding="UTF-8") as f:
            f.write(
                INIT_FILE_CONTENTS.format(cog_file_name=cog_filename, cog_name=cog_name)
            )

        # Create the <cog_name>.py file
        with open(cog_dir_path / f"{cog_filename}.py", "w", encoding="UTF-8") as f:
            f.write(COG_FILE_CONTENTS.format(cog_name=cog_name))

        print(f"Cog created: {cog_dir_path}")

    except FileExistsError:
        print(f"Cog already exists: {cog_dir_path}")

    except OSError as e:
        print(f"Error creating cog directory: {cog_dir_path}. {e}")


if __name__ == "__main__":
    create_cog()
