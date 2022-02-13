from flask import Flask, request
 
app = Flask(__name__)
 
 
@app.route('/')
def hello_world():
    return 'hello world'
 
 
@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    print(request.stream.read())
    return 'welcome'
 
 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
