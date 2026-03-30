def init_app(app):
    app.config['SECRET_KEY'] = 'dev-key'
    app.config['DEBUG'] = 1

    if app.debug:
        app.config['DEBUG_TB_TEMPLETE_EDITOR_ENABLED']=True
        app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False