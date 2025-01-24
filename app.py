import streamlit as st
import pandas as pd

# Set page config for better layout
st.set_page_config(
    page_title="AQI Prediction Dashboard",
    layout="wide",  # Use wide layout for better visuals
    initial_sidebar_state="expanded"
)

# Add a sidebar for app navigation or description
st.sidebar.title("About")
st.sidebar.info(
    """
    This app provides a 3-day forecast of Air Quality Index (AQI) levels.
    Predictions are generated using a machine learning model trained on historical data.
    Stay informed and take necessary precautions based on air quality predictions.
    """
)

# Application Title and Header
st.title("Air Quality Index (AQI) Prediction Dashboard")
st.markdown(
    """
    ### Forecast for the Next 3 Days
    Stay updated on air quality trends with predicted AQI levels for the upcoming days.
    """
)

# Function to retrieve prediction data
@st.cache_data
def load_predictions():
    """
    Load the AQI prediction results from a file.

    Returns:
        pd.DataFrame: DataFrame containing the predictions.
    """
    predictions = pd.read_pickle("prediction_results.pkl")  # Adjust file path if needed
    return predictions

# Load the prediction data
try:
    predictions = load_predictions()
except FileNotFoundError:
    st.error("Prediction data not found. Please ensure 'prediction_results.pkl' is available.")
    st.stop()

# Split layout into two columns
col1, col2 = st.columns(2)

# Display the prediction table in the first column
with col1:
    st.subheader("📋 Forecasted AQI Levels")
    st.dataframe(
        predictions.style.format({"Predicted_AQI": "{:.2f}"}).highlight_max(
            subset=["Predicted_AQI"], color="lightcoral", axis=0
        )
    )

# Add a visualization in the second column
with col2:
    st.subheader("📈 AQI Forecast Trend")
    st.line_chart(
        data=predictions.set_index("Date")["Predicted_AQI"],
        use_container_width=True
    )

# Add a footer section
st.markdown("---")
st.markdown(
    """
    **Note**: AQI predictions are estimates based on historical trends and model predictions.
    Please check official sources for real-time air quality data.
    """
)
