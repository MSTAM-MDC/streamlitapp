import streamlit as st
import pickle

# Define a function to load the model and apply the st.cache decorator
@st.cache(allow_output_mutation=True)
def load_model():
    with open('nlp.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load the pickled model
with open('nlp.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('NLP Sentiment Analysis')

# User input
user_input = st.text_area("Enter Text", "")

# Predict and display the result
if st.button('Predict Sentiment'):
    prediction = model.predict([user_input])[0]
    if prediction == 1:
        st.write('Positive Sentiment')
    else:
        st.write('Negative Sentiment')
tab1, tab2 = st.tabs(["About", "Why"])
tab1.write("Sentiment analysis, also known as opinion mining, is the process of determining the sentiment or emotion expressed in a piece of text. It involves using natural language processing (NLP) techniques to analyze and classify subjective information as positive, negative, or neutral.")
tab1.write("In summary, sentiment analysis empowers businesses to make informed decisions, enhance customer experiences, and safeguard their brand reputation.")
