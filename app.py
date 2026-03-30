from flask import Flask

def create_app():
    app = Flask(__name__)

    from delivery.ext.config import init_app as init_config
    init_config(app)

    from delivery.ext.debugtoolbar import init_app as init_toolbar
    init_toolbar(app)

    from delivery.views import init_app as init_main
    init_main(app)

    return app


# py .\make_env.pys
# .\venv\Scripts\activate
# invoke install
# $env:FLASK_DEBUG=1
# $env:FLASK_ENV='development'
# $env:FLASK_APP='app.py'
# invoke run

# one dark pro
# vs code icons
# jinja
# jinja snippets
#python