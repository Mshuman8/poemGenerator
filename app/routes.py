from app import app
from flask import render_template, request
from app.models import model, formopener
import requests, random

@app.route('/poem', methods=['POST'])

def get_poem_data():
    input_word = request.form["input_word"]
    # next three lines are declaring that we will find a rhyme as the parameter and calling the API to look for that.
    line1, line2 = model.generate_lines(input_word)
    return render_template('index.html', input_word = line1, output_word=line2)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

