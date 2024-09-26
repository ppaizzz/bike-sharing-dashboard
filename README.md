# Bike Sharing Dashboard

This project is a Streamlit dashboard that provides insights into bike-sharing data. It uses two datasets: `day.csv` (daily data) and `hour.csv` (hourly data) to explore patterns and trends in bike-sharing behavior.

## Features

- **Daily Dataset Analysis (day.csv):**
  - Analyze the relationship between temperature and bike rentals.
  - Visualize bike rentals by day of the week.
  
- **Hourly Dataset Analysis (hour.csv):**
  - Explore bike rentals by hour of the day.
  - Compare rental patterns at different times of the day.

## How to Run the Project

1. **Install the required libraries**:
   - Install the dependencies by running the following command:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Streamlit App**:
   - Use the command below to start the app:
     ```bash
     streamlit run bike_sharing_dashboard.py
     ```

3. **Deploy on Streamlit Cloud**:
   - The dashboard is also deployed on Streamlit Cloud. You can access the deployed app [here](https://share.streamlit.io/username/repository-name/main/bike_sharing_dashboard.py).

## Files

- `bike_sharing_dashboard.py`: Main code for the Streamlit dashboard.
- `day.csv`: Daily bike-sharing data.
- `hour.csv`: Hourly bike-sharing data.
- `requirements.txt`: Required dependencies for the project.

## Dataset Information

- **day.csv**: Contains daily information about bike rentals including weather conditions, holidays, and number of users.
- **hour.csv**: Contains hourly data on bike rentals including weather, time of day, and number of users.


