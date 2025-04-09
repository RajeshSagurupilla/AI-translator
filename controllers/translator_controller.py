from flask import Blueprint, render_template, request, jsonify
from services.translator_service import translate_text

translate = Blueprint('translate',__name__)


@translate.route("/")
def home():
    return render_template("index.html")

@translate.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")
    target_lang = data.get("target_language")
    model = data.get("model","mixtral")

    if not text or not target_lang:
        return jsonify({"error": "Missing text or target language"}), 400

    translation = translate_text(text, target_lang, model)
    return jsonify({"translated_text": translation})