from flask import Flask, request, render_template
from flask_restful import Resource, Api
from ner import SpacyDocument


app = Flask(__name__)
api = Api(app)


class NerApi(Resource):

    def get(self):
        return {
            'description': 'GET request to /api returns this message, POST returns the result of processing a text file. Visit http://127.0.0.1:5000/ for web server.',
            'resources': ['/', '/api'],
            'port': 5000
        }

    def post(self):
        text = request.get_data(as_text=True)
        doc = SpacyDocument(text)
        return doc.get_entities()


@app.route("/")
def index():
    return render_template("home.html")


@app.post("/")
def submit():
    if request.form['button'] == "Submit":
        doc = SpacyDocument(request.form['box'])
        entities = doc.get_entities_with_markup()
        return render_template("home.html", entities=entities)


api.add_resource(NerApi, "/api")


if __name__ == "__main__":
    app.run(debug=True)
