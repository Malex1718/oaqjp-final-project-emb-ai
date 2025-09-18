import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detect emotions from text using Watson NLP API
    
    Args:
        text_to_analyze: String containing the text to analyze
    
    Returns:
        String containing the response from Watson NLP API
    """
    # Watson NLP API configuration
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Make POST request to Watson NLP
    response = requests.post(url, json=input_json, headers=headers)
    
    # Return the text attribute of the response
    return response.text