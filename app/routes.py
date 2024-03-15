from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Sarma"}
    return (
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home Page - Flask Blog</title>
    </head>
    <body>
        <h1>Hello, """
        + user["username"]
        + """!</h1>
    </body>
    </html>
    """
    )
