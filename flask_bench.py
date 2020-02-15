import flask

app = flask.Flask(__name__)


@app.route('/json')
def test_json():
    return flask.jsonify(message="Hello, world!")
