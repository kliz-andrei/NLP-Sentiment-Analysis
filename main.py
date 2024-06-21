from flask import Flask, request, jsonify, render_template
from sentiment_analysis import sentiment_analyzer
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze", "")
    if text_to_analyze:
        try:
            result = sentiment_analyzer(text_to_analyze)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "No text provided"}), 400

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
