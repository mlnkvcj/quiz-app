import functools
import json
from flask_cors import cross_origin

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import json
from werkzeug.security import check_password_hash, generate_password_hash

from server.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@cross_origin()

@bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        print(data)
        username = data['username']
        password = data["password"]
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
    return "OK", 200

@bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        username = data['username']
        password = data["password"]
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return "OK", 200

@bp.route("/check-session", methods=["GET"])
def check_session():
    if "user_id" in session:
        return "OK", 200
    return "Unauthorized", 403

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('./frontend/src/routes/+page.svelte'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view