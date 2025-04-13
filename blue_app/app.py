from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metric
blue_counter = Counter('blue_requests_total', 'Total number of requests to the blue app')

@app.route('/')
def home():
    blue_counter.inc()
    return "Hello from the Blue App!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(port=5000)

