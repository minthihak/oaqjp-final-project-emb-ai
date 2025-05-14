"""Flask application for emotion detection.

This application provides a web interface to analyze text and detect emotions.
"""
from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main page of the application.

    Returns:
        str: The rendered HTML content for the index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    """Analyzes the provided text for emotions and returns the results.

    The text to analyze is passed as a query parameter named 'text_to_analyze'.

    Args:
        text_to_analyze (str): The text string to be analyzed for emotions (obtained from request arguments).

    Returns:
        str: A string describing the detected emotions and the dominant emotion.
    """
    text = request.args.get('textToAnalyze')
    emotion = emotion_detector(text)
    return "For the given statement, the system response is {}. The dominant emotion is {}".format(emotion, emotion['dominant_emotion'])

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
