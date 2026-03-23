from flask import Blueprint, current_app, render_template
bp_main  = Blueprint('main', __name__)

@bp_main.route("/")
@bp_main.route("/index")
def index():
    user = {'username':'brenno'}
    current_app.logger.info("O endpint 'index' foi acessado")
    return render_template('main/index.html', user=user)