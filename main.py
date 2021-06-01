from flask import Flask, jsonify
from flask_restful import Resource, Api,reqparse
import os
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
# CORs added
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('code')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Code(Resource):
    outputFile = 'output.txt'

    def get(self):
        resp = ''
        with open(Code.outputFile,'r+') as fp:
            resp = fp.read()
        return jsonify({'Code Response':resp})


    def post(self):
        args = parser.parse_args()
        code = args['code']
        with open('tempCode.py','w+') as fp:
            fp.write(code)
        # eval(input_json['code'])
        outputFile = 'output.txt'
        os.system('python tempCode.py > %s'%outputFile) 
        resp = ''
        with open(outputFile,'r+') as fp:
            resp  = fp.read()
        dictToReturn = {
            'code':code,
            'Code Output':resp
        }
        return jsonify(dictToReturn)



api.add_resource(HelloWorld, '/')
api.add_resource(Code,'/post')


if __name__ == '__main__':
    app.run(debug=True)