import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# Page configuration
st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="centered"
)


# Title
st.title("🎓 Student Score Predictor")
st.write("Predict a student's math score based on academic and demographic information.")


# Input section
st.subheader("Enter Student Information")

gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

race_ethnicity = st.selectbox(
    "Race / Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)

lunch = st.selectbox(
    "Lunch",
    ["standard", "free/reduced"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading_score = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    value=70
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    value=70
)


# Prediction button
if st.button("Predict Math Score"):

    try:
        # Create input data
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        # Convert to dataframe
        pred_df = data.get_data_as_data_frame()

        # Prediction pipeline
        predict_pipeline = PredictPipeline()

        results = predict_pipeline.predict(pred_df)

        # Display result
        st.success(
            f"Predicted Math Score: {results[0]:.2f}"
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")