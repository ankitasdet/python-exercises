from flask import Flask
app = Flask('app')

@app.route('/home')
def hello():
    return 'Hello KARTEEK!'

if __name__ == '__main__':
    app.run(debug=True)