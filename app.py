from flask import Flask, render_template, request
from googletrans import Translator, constants

app = Flask(__name__)

# Initialize the Google API translator
translator = Translator()

# Supported language pairs
supported_languages = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'hi': 'Hindi',
    'ar': 'Arabic',
    'ta': 'Tamil',
}

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = None
    error_message = None
    
    if request.method == "POST":
        source_lang = request.form.get("source_lang")
        target_lang = request.form.get("target_lang")
        text = request.form.get("text")
        
        if text:
            try:
                # Translate the text using Googletrans
                translation = translator.translate(text, src=source_lang, dest=target_lang)
                translated_text = translation.text
            except Exception as e:
                error_message = f"Error: {str(e)}"
        else:
            error_message = "Please enter text to translate"
    
    return render_template("index.html", translated_text=translated_text, error_message=error_message, languages=supported_languages)

if __name__ == "__main__":
    app.run(port=5001)  # Change the port number


