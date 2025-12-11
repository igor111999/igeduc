from flask import Flask

app = Flask(__name__)

from igedu import routes
from igedu import routes_fisica
from igedu import routes_jogos

