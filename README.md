# Classifying-the-Audio-Genres-Spotify

## Aim:
To classify Spotify tracks spanning 125 diverse genres based on their audio characteristics using machine learning techniques.

*Dataset:**

The data used in this project was collected and cleaned from Spotify's Web API using Python. The dataset includes the following features:
**track_id:** Unique Spotify identifier for each track.
**artists:** Names of artists, separated by ; for multiple artists.
**album_name:** Album title.
**track_name:** Track title.
**popularity:** Score from 0 to 100, indicating the track's popularity based on play count and recency.
**duration_ms:** Track duration in milliseconds.
**explicit:** Indicates explicit content (true/false).
**danceability:** Measures how suitable the track is for dancing (0.0 to 1.0).
**energy:** Tracks intensity and activity (0.0 to 1.0).
**key:** Musical key (integer representation).
**loudness:** Average loudness in dB.
**mode:** Modality (1 for major, 0 for minor).
**speechiness:** Detects the presence of spoken words.
**acousticness:** Likelihood of the track being acoustic (0.0 to 1.0).
**instrumentalness:** Probability of no vocals (0.0 to 1.0).
**liveness:** Indicates a live performance probability.
**valence:** Emotional tone (0.0 to 1.0).
**tempo:** Track tempo in beats per minute (BPM).
**time_signature:** Time signature of the track.
**track_genre:** Genre classification of the track.

**Detailed Workflow**

**A. Data Cleaning and Preprocessing**

**Missing Value Treatment**: Cleaned any missing values to ensure data consistency.
**Data Transformation**: Converted data into numerical formats and handled categorical data using encoding techniques.

**B. Exploratory Data Analysis (EDA)**

**Statistical Summaries:** Explored each feature to understand distributions and key trends.
**Correlation Analysis:** Analyzed the correlation matrix to identify relationships among features. 
**Visualization:** Created visualizations to better understand feature distributions and relationships with track genre. Analyze the distribution of various audio features across different genres.
**Feature Engineering:** Extract relevant features such as track_id, artists, album_name, track_name, popularity, duration_ms, explicit, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature, and track_genre.Created additional features if needed to improve model performance.
**Scaling and Normalization:** Normalize and scale the data to standardize the range of independent variables.
**Dimensionality Reduction:** Applied Principal Component Analysis (PCA) to reduce the feature space while retaining essential information.

**C. Model Training and Evaluation**

Train multiple machine learning classification models (e.g., Random Forest, SVM, KNN, Logistic Regression, Decision Tree and Gradient Bossting) on the processed dataset.
Evaluate model performance using appropriate metrics such as accuracy, precision, recall, and F1-score.
Compare the performance of different models to identify the best-performing one.
Since the outliers are not handled, performed hyperparameter tuning and cross validation.
Again the performance of different models is compared and found out the best among them.
The optimized model is saved as a pickle file for pipeline.
The pickle file of pipeline is used for deployment application.

**D. Deployment**

A Streamlit application was developed to allow users to interactively predict the genre of the track. This interface serves as a practical application of the model for real-time decision-making.


<img width="960" alt="image" src="https://github.com/user-attachments/assets/fdb41477-fd98-44af-ba91-1438247aaf1d">
