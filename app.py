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
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)




with app.app_context():
	db.create_all()
# ── Routes ─────────────────────────────────────────────────────────────────────

# Main page -- shows the form and lists items from the database
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # your logic goes here when form is submitted
        # example to read what the user typed:
        input_message = request.form.get('entry') #getting input from the index html 
        if input_message:
            #using the class and inside var's to save message and push to the database.
            messages = Message(content=input_message)
            db.session.add(messages)
            db.session.commit()


    return render_template('index.html')


# ── Run ────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    with app.app_context():
        db.create_all()       # creates app.db with your tables
    app.run(debug=True)
