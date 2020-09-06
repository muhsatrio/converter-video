import ffmpeg
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
import werkzeug
import os
import uuid

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return {
            "status": 200,
            "message": "Connected"
        }

class Convert(Resource):
    def post(self):
        files = request.files['file']
        ext = request.form['extension']
        if (os.path.isfile('files/{}'.format(files.filename)) == True):
            return {
                "status": 400,
                "message": "File has been exist"
            }
        filename = os.path.splitext(files.filename)[0]
        files.save("files/{}".format(files.filename))
        ffmpeg.input("files/{}".format(files.filename)).output("files/{}.{}".format(filename, ext)).run()
        return {
            "status": 200,
            "message": "Success"
        }

api.add_resource(Home, "/")
api.add_resource(Convert, "/convert")

if __name__ == "__main__":
    if (os.path.isdir("files") == False):
        os.umask(0)
        os.makedirs("files", mode=0o777)
    app.run(debug=True, host='0.0.0.0')