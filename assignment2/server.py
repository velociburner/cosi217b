from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
from ner import SpacyDocument


app = Flask(__name__)
# don't use as a real server, just hardcode the key
app.config['SECRET_KEY'] = '8a2afc2205a15bcb2cec06a1a7268b80'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_entities.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    count = db.Column(db.Integer, default=1, nullable=False)

    def __repr__(self):
        return f"{self.name}: {self.count}"


def create_all():
    with app.app_context():
        db.create_all()


create_all()


@app.route("/")
def index():
    return render_template("home.html")


@app.post("/")
def submit():
    if request.form['button'] == "Submit":
        doc = SpacyDocument(request.form['box'])
        entities = doc.get_entities_with_markup()
        parser = BeautifulSoup(entities, "xml")

        for entity in parser.find_all("entity"):
            entry = Entity.query.filter_by(name=entity.text).first()
            if entry is not None:
                entry.count += 1
            else:
                db.session.add(Entity(name=entity.text))

        db.session.commit()

        return render_template("home.html", entities=entities)


@app.get("/list")
def list():
    entities = Entity.query.all()
    print(entities)
    return render_template("list.html", entities=entities)


if __name__ == "__main__":
    app.run(debug=True)
