class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.view import cstore
        app.register_blueprint(cstore.api.blueprint)

        from app.view import product
        app.register_blueprint(product.api.blueprint)
