"""
Flask server for Emotion Detection application
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Analyze emotion from the provided text
    """
    text = request.form.get('textToAnalyze')
    
    response = emotion_detector(text)
    
    # Format the response as requested
    result = f"For the given statement, the system response is "
    result += f"'anger': {response['anger']}, "
    result += f"'disgust': {response['disgust']}, "
    result += f"'fear': {response['fear']}, "
    result += f"'joy': {response['joy']} and "
    result += f"'sadness': {response['sadness']}. "
    result += f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)