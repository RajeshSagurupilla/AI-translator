from flask import Flask, render_template, request, jsonify
from services.translator_service import translate_text
from controllers.translator_controller import translate_route

app = Flask(__name__)

app.register_blueprint(translate_route)

if __name__ == "__main__":
    app.run(debug=True)
