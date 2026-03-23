from flask import Flask

def create_app():
    app = Flask(__name__)

    from delivery.views import init_app as init_main
    init_main(app)

    return app
