from textblob import TextBlob

def sentiment_analyzer(text):
    """
    Analyzes the sentiment of the provided text.
    Returns a dictionary with the label and confidence score.
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        label = 'POSITIVE'
    elif sentiment < 0:
        label = 'NEGATIVE'
    else:
        label = 'NEUTRAL'
    
    return {
        "label": label,
        "score": sentiment
    }
