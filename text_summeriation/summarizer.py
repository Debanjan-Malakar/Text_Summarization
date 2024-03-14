from transformers import pipeline

from flask import Flask, render_template, request

# Download and load the summarization model (change if needed)
summarizer = pipeline("summarization", model="t5-base")  # Adjust model name as desired

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def summarize():
    if request.method == "POST":
        text = request.form["text"]
        summary = summarizer(text, max_length=100)
        return render_template("index.html", summary=summary[0]["summary_text"], text=text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)  # Run in debug mode for live reload
