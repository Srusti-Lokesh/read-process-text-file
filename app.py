from flask import Flask, render_template, request
from werkzeug.exceptions import RequestEntityTooLarge

from text_stats import process_uploaded_file

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB


@app.get("/")
def index():
    return render_template("index.html", result=None, error=None)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze():
    uploaded_file = request.files.get("file")

    if uploaded_file is None or not uploaded_file.filename:
        return render_template(
            "index.html",
            result=None,
            error="Please choose a .txt file before submitting.",
        ), 400

    if not uploaded_file.filename.lower().endswith(".txt"):
        return render_template(
            "index.html",
            result=None,
            error="Only .txt files are supported.",
        ), 400

    try:
        result = process_uploaded_file(uploaded_file.stream)
        result["filename"] = uploaded_file.filename
        return render_template("index.html", result=result, error=None)
    except UnicodeDecodeError:
        return render_template(
            "index.html",
            result=None,
            error="The file is not valid UTF-8 text. Please upload a UTF-8 .txt file.",
        ), 400
    except OSError:
        return render_template(
            "index.html",
            result=None,
            error="The file could not be read. Please try again.",
        ), 400


@app.errorhandler(RequestEntityTooLarge)
def too_large(_error):
    return render_template(
        "index.html",
        result=None,
        error="File is too large. The maximum allowed size is 10 MB.",
    ), 413


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
