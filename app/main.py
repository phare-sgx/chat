from flask import Flask, request
 
app = Flask(__name__)
 
 
@app.route('/',methods=['POST','GET'])
def hello_world():
    return 'hello world'
 
#  json
@app.route('/register', methods=['POST'])
def register():
    result = request.json['a'] + request.json['b']
    return str(result)
# 无
@app.route('/register2', methods=['POST'])
def register2():
   return request.form
 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
