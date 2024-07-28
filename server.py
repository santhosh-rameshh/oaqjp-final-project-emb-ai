"""
This module defines the Flask server for the Emotion Detection application.
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Handle the emotionDetector endpoint.
    """
    response = {}

    if request.method == 'POST':
        statement = request.form['textToAnalyze']
        emotions = emotion_detector(statement)
        dominant_emotion = emotions['dominant_emotion']

        if dominant_emotion is None:
            response = {
                'system_response': emotions,
                'display_response': "Invalid text! Please try again."
            }
        else:
            response = {
                'system_response': emotions,
                'display_response': (
                    f"For the given statement, the system response is {emotions}. "
                    f"The dominant emotion is {dominant_emotion}."
                )
            }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    