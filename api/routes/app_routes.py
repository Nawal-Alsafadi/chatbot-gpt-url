from api.routes.chat_emix_bp import chat_emix_bp


def app_routes(app):
    app.register_blueprint(chat_emix_bp, url_prefix='/api')

