from flask import Flask, request, jsonify
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello to World"

@app.route('/post',methods=['POST'])
def test():
    input_json = request.get_json(force=True)
    # print(input_json['code'])
    with open('tempCode.py','w+') as fp:
        fp.write(input_json['code'])
    # eval(input_json['code'])
    os.system('python tempCode.py')
    dictToReturn = {'code':input_json['code']}
    return jsonify(dictToReturn)


if __name__ == '__main__':
    app.run(
        debug=True
    )