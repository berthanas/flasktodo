from flask import Flask,render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "23fwsm22lkfşlk3r1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/berka/Documents/PyProjeler/ToDo/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = ToDo.query.all()
    return render_template("index.html", todos = todos)

@app.route("/add",methods = ["POST"])
def add():
    title = request.form.get("title")
    todo = ToDo(title = title, complete = False)
    db.session.add(todo)
    db.session.commit()
    flash("ToDo Eklendi","success")
    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def complete(id):
    todo = ToDo.query.filter_by(id = id).first()
    todo.complete = not todo.complete
    db.session.commit()
    flash("ToDo Güncellendi", "success")
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    todo = ToDo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    flash("ToDo Silindi","success")
    return redirect(url_for("index"))

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
