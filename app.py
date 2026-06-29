from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# ── App setup ──────────────────────────────────────────────────────────────────
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)


# ── Model (your database table) ────────────────────────────────────────────────
# Add your columns here
class Messages(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    messages       = db.Column(db.String(200), nullable=False)
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # add more columns below this line
    # example: description = db.Column(db.String(500))
    # example: done = db.Column(db.Boolean, default=False)



with app.app_context():
	db.create_all()
# ── Routes ─────────────────────────────────────────────────────────────────────

# Main page -- shows the form and lists items from the database
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # your logic goes here when form is submitted
        # example to read what the user typed:
        messages = request.form['entry']
    db.session.add(messages)
    db.session.commit()

    # your logic to fetch from database goes here
    # example: items = Item.query.all()
  # items = []

    return render_template('index.html')


# Add more routes below this line
# example:
# @app.route('/delete/<int:item_id>')
# def delete(item_id):
#     pass


# ── Run ────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    with app.app_context():
        db.create_all()       # creates app.db with your tables
    app.run(debug=True)
