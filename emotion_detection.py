import requests


def emotion_detector(text_to_analyze):
    """Analyzes the input text to detect emotions.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        str: The raw text response from the emotion detection service.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": text_to_analyze }
    header = { "grpc-metadata-mm-model-name": "emotion_aggregated-workflow_lang_en_stock" }
    response = requests.post(url, json = myobj, headers=header)
    return response.text
    