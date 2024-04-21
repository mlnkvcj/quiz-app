from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

import sqlite3

from server.db import get_db

bp = Blueprint('submit', __name__)

# Route to display the form for question submission
@bp.route('/submit_question', methods=['GET'])
def show_question_form():
    return render_template('question_input/submit_question.html')

# Route to handle form submission and insert question into the database
@bp.route('/submit_question', methods=['POST'])
def submit_question():
    question = request.form['question']
    option1 = request.form['option1']
    option2 = request.form['option2']
    option3 = request.form['option3']
    option4 = request.form['option4']
    answer = request.form['answer']

    insert_question_into_db(question, option1, option2, option3, option4, answer)

    return redirect(url_for('submit.show_question_form'))  # Redirect to the form page after submission

# Function to insert the question into the database
def insert_question_into_db(question, option1, option2, option3, option4, answer):
    db = get_db()
    db.execute("INSERT INTO questions (question, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?)",
                (question, option1, option2, option3, option4, answer))
    db.commit()