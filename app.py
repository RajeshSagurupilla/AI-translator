from flask import Flask, render_template, request, jsonify
from services.translator_service import translate_text

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)
