import os

from __init__ import create_app


app = create_app(os.getenv("FLASK_CONFIG", default="config.ProdConfig"))

