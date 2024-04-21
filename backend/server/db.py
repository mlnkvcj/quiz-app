import sqlite3
import shutil
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    click.echo("Intitalizing db...")
    init_db()
    click.echo('Initialized the database.')

def backup_db(target="bkp.sqlite"):
    shutil.copyfile(current_app.config['DATABASE'], target)

@click.command('bkp-db')
def backup_db_command():
    click.echo("Backing up db...")
    backup_db()
    click.echo("Database backed up!")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(backup_db_command)