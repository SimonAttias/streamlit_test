import streamlit as st
import random
import joblib
import pickle

@st.cache_data
def generate_random_value(x):
    return random.uniform(0, x)

a = generate_random_value(10)
b = generate_random_value(20)

st.write(a)
st.write(b)

# Choose ONE of these methods to load your model:

# Method 1: Using joblib (recommended for scikit-learn models)
loaded_model = joblib.load("model")

# Method 2: Using pickle (if your model was saved with pickle)
# loaded_model = pickle.load(open("model", 'rb'))

# Note: Don't use both methods - choose the one that matches how you saved your model
