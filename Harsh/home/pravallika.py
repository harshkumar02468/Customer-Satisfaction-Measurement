def predict_sentiment(user_input):
    import pandas as pd
    import string
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from nltk.sentiment import SentimentIntensityAnalyzer
    from sklearn.pipeline import make_pipeline
    
    import pickle

    # Initialize the VADER sentiment analyzer
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()

    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

    # Preprocessing function
    def preprocess_text(text):
        # Handle missing values
        if pd.isnull(text):
            text = ""
        
        text = text.lower()
        
        text = text.translate(str.maketrans("", "", string.punctuation))
        
        # Tokenization and Lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text)
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        
        # Removing stopwords
        stop_words = set(stopwords.words("english"))
        filtered_tokens = [token for token in lemmatized_tokens if token not in stop_words]
        
        # Joining tokens back to text
        processed_text = " ".join(filtered_tokens)
        
        return processed_text

    # Create a pipeline for feature extraction and Naive Bayes classification
    pipeline = make_pipeline(
        TfidfVectorizer(),
        MultinomialNB()
    )

    def perform_sentiment_analysis(input_text):
        input_processed = preprocess_text(input_text)

        # Load the trained model from the file
        with open(r'C:\Users\Harsh kumar\Desktop\trained model\trained_file.pkl', 'rb') as file:
            pipeline = pickle.load(file)

        sentiment = pipeline.predict([input_processed])[0]

        sentiment_scores = analyzer.polarity_scores(input_processed)
        sentiment_score = sentiment_scores['compound']

        return sentiment, sentiment_score

    predicted_sentiment, sentiment_score = perform_sentiment_analysis(user_input)

    return predicted_sentiment, sentiment_score
