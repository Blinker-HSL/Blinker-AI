from flask import Flask
from api.eye_analysis import analyze

app = Flask(__name__)

@app.route('/analyze-eyes', methods=['POST'])
def analyze_eyes():
    return analyze()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)