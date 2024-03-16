from flask import Flask
from views import init as init_views

if __name__ == "__main__":
    app = Flask(__name__)

    init_views(app)

    app.run(debug=True)
