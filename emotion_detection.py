import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    # Extraer emociones y puntuaciones
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    formatted_emotions = {emotion: round(score, 4) for emotion, score in emotions.items()}
    # Encontrar la emoción dominante
    dominant_emotion = max(emotions, key=emotions.get)
    # Agregar la emoción dominante al resultado
    formatted_emotions['dominant_emotion'] = dominant_emotion
    
    return formatted_emotions