from flask import Flask, redirect, url_for
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)