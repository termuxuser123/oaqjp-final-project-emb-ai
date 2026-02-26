import requests
import json

def emotion_detector(text_to_analyze):
    """Emotion detection using Watson NLP - returns formatted dictionary (Task 3)"""
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Task 3 Step 1: Convert response text to dictionary
    response_dict = json.loads(response.text)
    
    # Task 3 Step 2: Extract the emotions
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Task 3 Step 3: Find dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Task 3 Step 4: Return exact required format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }