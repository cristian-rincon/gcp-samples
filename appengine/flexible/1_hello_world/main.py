from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "App Engine Standard", "version": "1.0.0"}


if __name__ == "__main__":
    app.run(debug=True, port=8080)
