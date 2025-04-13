from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metric
green_counter = Counter('green_requests_total', 'Total number of requests to the green app')

@app.route('/')
def home():
    green_counter.inc()
    return "Hello from the green App!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(port=5001)

