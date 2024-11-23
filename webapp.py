
import pickle
import pandas as pd
import streamlit as st
import numpy as np

# Streamlit app configuration
icon = "D:\MDE94\FinalProject\Classifying_the_Audio_Genres\spotify_logo.jpg"
st.set_page_config(page_title="Spotify Audio Genre Prediction", page_icon=icon)

# Initialize the session state for page management
if 'page' not in st.session_state:
    st.session_state.page = "welcome"  # Start on the welcome page


# Function to show the main page
def main_page():

    st.title("Spotify Music Genre Predictor")
    st.subheader("Lets Predict Genre of the song!")


    # Custom CSS for labels below the sliders
    st.markdown(
        """
        <style>
        .slider-container {
            position: relative;
            height: 50px;
        }
        .slider-label {
            position: absolute;
            top: 0.03px;
            font-size: 12px;
        }
        .slider-label-low {
            left: 0;
        }
        .slider-label-mid {
            left: 50%;
            transform: translateX(-50%);
        }
        .slider-label-high {
            right: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Load data
    df = pd.read_csv("D:\MDE94\FinalProject\Classifying_the_Audio_Genres\spotify_final.csv")

    # Input song duration using sliders for minutes and seconds
    st.subheader("Enter details of your song")
    minutes = st.slider("Minutes:", 0, 10, 0)
    seconds = st.slider("Seconds:", 0, 59, 0)

    # New input for Tempo
    tempo_value = st.slider("Tempo (0-250 BPM)", 0, 250, 120)


    danceability = st.slider(
        "Choose the danceability of your song:",
        0.0, 10.0, 5.0,
    )

    energy = st.slider(
        "Choose the energy of your song:",
        0.0, 10.0, 5.0,
    )

    valence = st.slider(
        "Choose the emotional tone of your track:",
        0.0, 10.0, 5.0,
    )

    acousticness = st.slider(
        "Choose the acoustiness of your track:",
        0.0, 10.0, 5.0,
    )

    loudness = st.slider(
    "Choose the loudness of your track (-49.000 - 5.000) :",
    -49.000,5.000,-20.000,
    )

    speechiness = st.slider(
        "Choose the speechiness of your song:",
        0.0, 10.0, 5.0,
    )

    liveness = st.slider(
        "Choose the liveness of your song:",
        0.0, 10.0, 5.0,
    )

    instrumentalness = st.slider(
        "Choose the instumentalness of your song:",
        0.0, 10.0, 5.0,
    )

    # Input for Popularity
    popularity = st.slider(
        "Select the popularity of your song (0-100)",
        0, 100, 50,
    )

    # Input for Key
    key = st.slider(
        "Select the key of your song (0-11)",
        0, 11, 0,
    )

    # Input for time_signature
    time_signature = st.slider(
        "Select the time_signature of your song (0-5)",
        0, 5, 0,
    )

    # Input for Explicit
    explicit = st.radio("Choose your song Explicit or not?", ("1", "0"))
    explicit_value = 1 if explicit == "1" else 0

    # Input for Is Mode
    mode = st.radio("What is your song Mode?", ("1", "0"))
    mode_value = 1 if mode == "1" else 0

    # Convert the input duration to milliseconds
    duration_ms = (minutes * 60 + seconds) * 1000
    st.write(f"The song's duration in milliseconds is: {duration_ms} ms")
    st.write(f"Tempo: {tempo_value} BPM")
    st.write(f"Danceability (0-1 scale): {danceability / 10:.1f}")
    st.write(f"Energy (0-1 scale): {energy / 10:.1f}")
    st.write(f"Valence (0-1 scale): {valence / 10:.1f}")
    st.write(f"Acoustiness (0-1 scale): {acousticness / 10:.1f}")   
    st.write(f"Loudness: {loudness}")
    st.write(f"Speechiness (0-1 scale): {speechiness / 10:.1f}")
    st.write(f"Liveness (0-1 scale): {liveness / 10:.1f}")
    st.write(f"Instrumentalness (0-1 scale): {instrumentalness / 10:.1f}")
    st.write(f"Key: {key}")
    st.write(f"Popularity: {popularity}")
    st.write(f"Time Signature: {time_signature}")
    st.write(f"Explicit: {explicit_value}")
    st.write(f"Mode: {mode_value}")


    # Prediction section
    st.markdown("Click below to predict the track genre :")

    if st.button("Predict Genre"):
        # Load the model pipeline
        with open('D:\MDE94\FinalProject\Classifying_the_Audio_Genres\pipeline.pkl', 'rb') as f:
            pipeline = pickle.load(f)

        with open('D:\MDE94\FinalProject\Classifying_the_Audio_Genres\label_encoder.pkl', 'rb') as f:
            label_encoder = pickle.load(f)

        # Prepare the input data for the model
        input_data = pd.DataFrame({
            'popularity': [popularity],
            'duration_ms': [duration_ms],
            'explicit': [explicit_value],
            'danceability': [danceability],
            'energy': [energy],
            'key': [key],
            'loudness': [loudness],
            'mode': [mode_value],
            'speechiness': [speechiness],
            'acousticness': [acousticness],
            'instrumentalness': [instrumentalness],
            'liveness': [liveness],
            'valence': [valence],
            'tempo': [tempo_value],
            'time_signature': [time_signature]
            })
        

        # Predict the price using the pipeline
        prediction = pipeline.predict(input_data)
        # Convert numerical prediction back to original label 
        decoded_prediction = label_encoder.inverse_transform(prediction)

        # Display the prediction result
        #st.markdown(f"The genre of the song is: {prediction[0]}")
        st.markdown(f"The genre of the song is: {decoded_prediction[0]}")




if st.session_state.page == 'welcome':
    st.markdown(
    """
    <div style="text-align: center;">
    <h1>Welcome To Spotify Music Genre Prediction App!</h1>
    <h3>"Check the Genre of your Track!"</h3>
    </div>
    """,
    unsafe_allow_html=True
    )

    #Center the button using Streamlit
    col1, col2, col3 = st.columns([15, 17, 4])
    with col2:
        if st.button("Let's Go"):
            st.session_state.page = 'prediction'
    # Center an image below the button
    col1, col2, col3 = st.columns([10, 10000, 10])
    with col2:
        st.image("D:\MDE94\FinalProject\Classifying_the_Audio_Genres\Spotify_FTR_Header-1920x955.png")
else:
    main_page()
