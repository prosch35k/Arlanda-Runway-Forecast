from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Render!'})

@app.route('/weather')
def get_weather():
    return jsonify({
        'condition': 'Broken',
        'altitude_ft': 3000
    })

if __name__ == '__main__':
    app.run()
