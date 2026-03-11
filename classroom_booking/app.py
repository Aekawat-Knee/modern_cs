from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret123"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# -----------------
# Models
# -----------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

class Booking(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(100))
    date = db.Column(db.String(50))
    student = db.Column(db.String(100))

# -----------------
# Routes
# -----------------

@app.route("/")
def home():
    return redirect("/login")

# LOGIN
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username,password=password).first()

        if user:
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# REGISTER
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        new_user = User(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

# DASHBOARD
@app.route("/dashboard")
def dashboard():

    bookings = Booking.query.all()
    return render_template("dashboard.html", bookings=bookings)

# BOOK ROOM
@app.route("/book", methods=["GET","POST"])
def book():

    room = request.args.get("room")

    if request.method == "POST":

        room = request.form["room"]
        date = request.form["date"]
        student = request.form["student"]

        existing = Booking.query.filter_by(room=room, date=date).first()

        if existing:

            return render_template(
                "book.html",
                room=room,
                date=date,
                student=student,
                error="❌ This room is already booked on this date"
            )

        booking = Booking(room=room, date=date, student=student)

        db.session.add(booking)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("book.html", room=room)

@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login")

    username = session["user"]

    my_bookings = Booking.query.filter_by(student=username).all()

    return render_template("profile.html",
                           bookings=my_bookings,
                           username=username)

# RUN
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)