import os
from types import SimpleNamespace

import pytest

from alembic.command import downgrade, upgrade
from alembic.config import Config
from alembic.script import Script, ScriptDirectory


def make_alembic_config(cmd_opts, base_path: str = ".") -> Config:
    """
    Create an Alembic configuration object based on command-line arguments.
    Replace relative paths with absolute ones.

    Args:
        cmd_opts (argparse.Namespace): Command-line arguments.
        base_path (str): Base path to prepend to relative paths.

    Returns:
        Config: Alembic configuration object.
    """
    if not os.path.isabs(cmd_opts.config):
        cmd_opts.config = os.path.join(base_path, cmd_opts.config)

    config = Config(file_=cmd_opts.config, ini_section=cmd_opts.name, cmd_opts=cmd_opts)

    alembic_location = config.get_main_option("script_location")
    if not os.path.isabs(alembic_location):
        config.set_main_option(
            "script_location", os.path.join(base_path, alembic_location)
        )
    if cmd_opts.pg_url:
        config.set_main_option("sqlalchemy.url", cmd_opts.pg_url)

    return config


def get_revisions() -> list[Script]:
    """
    Retrieve a list of migration revisions.
    The list is in reverse chronological order, from the most recent to the oldest.

    Returns:
        list[Script]: List of migration revisions.
    """
    options = SimpleNamespace(
        config="alembic.ini", pg_url=None, name="alembic", raiseerr=False, x=None
    )
    config = make_alembic_config(options)

    revisions_dir = ScriptDirectory.from_config(config)
    revisions = list(revisions_dir.walk_revisions("base", "heads"))
    revisions.reverse()

    return revisions


@pytest.mark.parametrize("revision", get_revisions())
def test_migrations_stairway(alembic_config: Config, revision: Script):
    """
    Test migration revisions in reverse chronological order, from the most recent to the oldest.

    Args:
        alembic_config (Config): Alembic configuration object.
        revision (Script): Migration revision script.

    Raises:
        AssertionError: If an error occurs during the upgrade/downgrade process.
    """
    upgrade(alembic_config, revision.revision)
    downgrade(alembic_config, revision.down_revision or "-1")
    upgrade(alembic_config, revision.revision)
