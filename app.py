import logging
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    if app.debug:
        app.logger.setLevel(logging.DEBUG)

    from delivery.ext.config import init_app as init_config
    init_config(app)
    
    if test_config:
        app.config.update(test_config)

    if not app.config.get("TESTING"):
        from delivery.ext.wtf import init_app as init_wtf
        init_wtf(app)

    from delivery.ext.debugtoolbar import init_app as init_toolbar
    init_toolbar(app)

    from delivery.views import init_app as init_site
    init_site(app)
    
    return app

# py .\make_env.py
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
