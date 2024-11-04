from flask import Flask, request
from flask_resful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)


api = Api(app)

CORS(app)

identitas = {}

class ContohResource(Resource):
    def get(self):
        #response {"msg" : "Hallo Dunia"}
        return response
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umut"] = umurresponse = {"msg" : "Data berhasil masuk"}
        return response
    
api.add_resource(ContohResource, "/api", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
