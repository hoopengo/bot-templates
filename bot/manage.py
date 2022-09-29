import os
from pathlib import Path
from sys import argv

base_init = """from .{cog_file_name} import {cog_name}Cog"""

base_cog = """import nextcord
from nextcord.ext import commands


class {cog_name}Cog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.bot = client
"""

string_replacements = {
    "-": "_",
    "&": "",
    "?": "",
    "^": "",
    "%": "",
    "$": "",
    "#": "",
    "№": "",
    "@": "",
    "!": "",
    ";": "",
    "*": "",
    "(": "",
    ")": "",
}


def clear_string(string: str) -> str:
    for replacement_pattern in string_replacements:
        string = string.replace(
            replacement_pattern, string_replacements[replacement_pattern]
        )

    return string


def create_cog(path: str) -> bool:
    cog_path = path.split("/")
    cog_path[-1] = clear_string(cog_path[-1])
    cog_name = "".join(
        [cog_part.title() for cog_part in cog_path[-1].split("_")]
    )
    path = Path(str(Path(__file__).parent.resolve()) + "/cogs/" + "/".join(cog_path)).resolve()

    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"Cog already exist: {path}")
        return
    
    with open(f"{path}/__init__.py", "w", encoding="UTF-8") as f:
        f.write(
            base_init.format(cog_file_name=cog_path[-1], cog_name=cog_name)
        )

    with open(f"{path}/{cog_path[-1]}.py", "w", encoding="UTF-8") as f:
        f.write(base_cog.format(cog_name=cog_name))


def show_version():
    from __init__ import __version__

    print(f"Bot version: {__version__}")


if __name__ == "__main__":
	create_cog(input("Введите название кога: "))
