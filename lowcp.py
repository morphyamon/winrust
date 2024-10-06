from flask import Flask
import time
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a low-CPU usage service!"

def run_server():
    app.run(host='0.0.0.0', port=5000)

def cpu_usage_control():
    while True:
        # Sleep to keep CPU usage low
        time.sleep(1)  # Adjust this to control the frequency of checks

if __name__ == "__main__":
    # Start the Flask server in a separate thread
    threading.Thread(target=run_server, daemon=True).start()
    
    # Control CPU usage
    cpu_usage_control()
