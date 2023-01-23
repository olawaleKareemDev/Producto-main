from main import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask.cli import FlaskGroup

migrate = Migrate(app, db) 

# cli = FlaskGroup(app)
# @click.argument(db, default=’test*)

manager = Manager(app) # flask script is no longer supported
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
#     cli()