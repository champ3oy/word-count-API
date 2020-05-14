from flask import Flask

app = Flask(__name__)

@app.route('/count/<string:name>')
def hello(name):
    return str(len(name))

app.run(debug=True, host='0.0.0.0', port=8080)

# USAGE
# http://0.0.0.0:8080/count/yourtexthere