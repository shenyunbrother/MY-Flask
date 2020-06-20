from app import create_app, db,create_log
from flask_script import Manager, Server
from waitress import serve



app = create_app()
manager = Manager(app)

manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='127.0.0.1',
    port=80))

def db_init():
    db.create_all(app = create_app())

if __name__ == "__main__":
    app.run()
    # manager.run()
    # serve(app,host='127.0.0.1', port=80)