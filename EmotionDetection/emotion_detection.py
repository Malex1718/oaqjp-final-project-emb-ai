import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detect emotions from text using Watson NLP API
    
    Args:
        text_to_analyze: String containing the text to analyze
    
    Returns:
        Dictionary with emotion scores and dominant emotion
    """
    # Check for blank input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check for 400 status code
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Rest of your existing code...
    response_dict = json.loads(response.text)
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    output = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0)
    }
    
    dominant_emotion = max(output, key=output.get)
    output['dominant_emotion'] = dominant_emotion
    
    return output