
from flask import Flask, jsonify
import os
import platform

app = Flask(__name__)

@app.route('/startgame', methods=['GET'])
def start_game():
    os_name = platform.system().lower()
    if os_name == 'windows':
        os.system('cd windows && python run.py')
    elif os_name == 'linux':
        whoami = os.popen('whoami').read().strip()
        if 'u0' in whoami:
            os.system('cd termux && python3 run.py')
        else:
            os.system('cd linux && python3 run.py')
    else:
        return jsonify({'error': f'Unsupported OS: {os_name}'})
    return jsonify({'status': 'Game started'})

if __name__ == '__main__':
    app.run(port=5000)
