from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    print(f"Primit comanda: {data}")
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
