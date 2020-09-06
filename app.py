import ffmpeg
from flask import Flask
from flask_restful import Resource, Api

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
        return {
            "status": 200,
            "message": "Success"
        }

api.add_resource(Home, "/")
api.add_resource(Convert, "/convert")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


# stream = ffmpeg.input('input.mp4')
# stream = ffmpeg.output(stream, 'output.mp4')
# ffmpeg.run(stream)