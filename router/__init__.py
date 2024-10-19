def init_routes(app):
    @app.route("/user/<username>")
    def show_username(username):
        return f'User {username}'
