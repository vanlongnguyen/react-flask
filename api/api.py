import string
import random
import sys
from .src.readFile import Reader
from .src.randomGenerator import Generator
import os
import re
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    random_generator = Generator.write_to_file()
    return random_generator

@app.route('/readFile', methods=['GET'])
def read():
    reader = Reader.findTypes(Reader.read_file())
    return reader
