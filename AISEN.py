from flask import Flask, render_template, request
from textblob import TextBlob   #calculates the sentiment polarity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        review_text = request.form.get("review")
        if review_text:
            blob = TextBlob(review_text)
            # You can use sentiment.polarity (-1.0 to 1.0) to determine overall sentiment.
            polarity = blob.sentiment.polarity
            sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
