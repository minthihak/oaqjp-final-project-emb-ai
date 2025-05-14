import requests #import request library
import json # Import json library

# Define function that that take the string input text_to_analyze
def emotion_detector(text_to_analyze):
    """Analyzes the input text to detect emotions.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        str: The raw text response from the emotion detection service.
    """
    # URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Data to be sent in the request body
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Headers for the request, specifying the model to be used
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send a POST request to the API
    response = requests.post(url, json = myobj, headers=header)
    
    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)
    #return formatted_response
    
    # Extract the emotion scores from the response
    # The .get("emotion", {}) ensures that if "emotion" key is not present, it defaults to an empty dictionary
    emotions = {}
    first_prediction = formatted_response['emotionPredictions'][0]
    emotions = first_prediction.get("emotion", {})
    #return emotions
    
    # Determine the dominant emotion by finding the key with the maximum value in the emotions dictionary
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return a dictionary containing individual emotion scores and the dominant emotion
    return {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness"),
        "dominant_emotion": dominant_emotion
    }
