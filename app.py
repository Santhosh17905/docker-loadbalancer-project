from flask import Flask, render_template
import os

app = Flask(__name__)

# Global request counter
request_count = 0

@app.route("/")
def home():
    global request_count
    request_count += 1
    
    container = os.environ.get("APP_NAME", "Unknown Container")

    return render_template(
        "index.html",
        container=container,
        requests=request_count
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)