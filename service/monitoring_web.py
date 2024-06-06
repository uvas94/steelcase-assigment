from flask import Flask, jsonify
import requests
import psutil

app = Flask(__name__)

# Endpoint to check the status of the web app
@app.route('/status', methods=['GET'])
def check_status():
    url = 'http://127.0.0.1:5000'  # Replace with your web app URL
    try:
        response = requests.get(url)
        status = 'up' if response.status_code == 200 else 'down'
        return jsonify({'status': status, 'status_code': response.status_code})
    except requests.ConnectionError:
        return jsonify({'status': 'down', 'status_code': None})
        
# Endpoint to check system resource usage
@app.route('/resources', methods=['GET'])
def check_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    return jsonify({
    'cpu_usage': cpu_usage,
    'memory_usage': memory_usage,
    'disk_usage': disk_usage
    })
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)