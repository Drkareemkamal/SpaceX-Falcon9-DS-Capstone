# SpaceX Falcon 9 Launch Prediction

This project aims to predict the success or failure of SpaceX Falcon 9 launches using various attributes related to the rocket, launch conditions, and mission specifics.

## Project Overview

The dataset includes a variety of features such as the flight number, payload mass, orbit type, and whether the rocket has been reused. The model is designed to predict the likelihood of a successful launch using machine learning techniques.


![alt text](https://github.com/Drkareemkamal/SpaceX-Falcon9-DS-Capstone/blob/main/rocket.gif?raw=true)

## Features

The dataset consists of the following features:

- **FlightNumber**: Unique identifier for each Falcon 9 flight.
- **PayloadMass**: Mass of the payload (in kilograms) that the Falcon 9 rocket is carrying into orbit.
- **Flights**: Number of times this particular rocket has been launched.
- **Block**: Version of the Falcon 9 rocket.
- **ReusedCount**: Number of times a particular booster has been reused.
- **Orbit**: Target orbit for the payload (e.g., LEO, GEO, GTO, etc.).
- **LaunchSite**: Location from which the Falcon 9 rocket is launched (e.g., KSC LC 39A).
- **LandingPad**: Specific landing pad where the Falcon 9 booster is intended to land.
- **Serial**: Serial number of the Falcon 9 rocket booster.
- **GridFins**: Indicates whether the rocket is equipped with grid fins.
- **Reused**: Indicates whether the rocket booster has been reused from a previous flight.
- **Legs**: Indicates whether the rocket is equipped with landing legs for vertical landing.

![alt text](https://github.com/Drkareemkamal/SpaceX-Falcon9-DS-Capstone/blob/main/orbit.png?raw=true)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SpaceX-Falcon9-DS-Capstone.git
    ```
2. Navigate to the project directory:
    ```bash
    cd SpaceX-Falcon9-DS-Capstone
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open the app in your browser and input the parameters to get the prediction.

## Prediction Model

The model uses the `StandardScaler` from `scikit-learn` to standardize the numerical features and `OneHotEncoder` for categorical features. The model is trained to predict the likelihood of a successful launch.

### Example of User Input

```python
data = {
    'FlightNumber': [1],
    'PayloadMass': [5000],
    'Flights': [2],
    'Block': [1],
    'ReusedCount': [0],
    'Orbit': ['LEO'],
    'LaunchSite': ['CCAFS SLC 40'],
    'LandingPad': ['5e9e3032383ecb761634e7cb'],
    'Serial': ['B1003'],
    'GridFins': [True],
    'Reused': [False],
    'Legs': [True]
}

features = pd.DataFrame(data)
```


### Successfull Prediction Example

```python
data = {
    'FlightNumber': [100],
    'PayloadMass': [6000],
    'Flights': [3],
    'Block': [5],
    'ReusedCount': [1],
    'Orbit': ['GTO'],
    'LaunchSite': ['KSC LC 39A'],
    'LandingPad': ['5e9e3032383ecb761634e7cb'],
    'Serial': ['B1049'],
    'GridFins': [True],
    'Reused': [True],
    'Legs': [True]
}
features = pd.DataFrame(data)

Prediction: Success
Probability of Failure: 10.45%
Probability of Success: 89.55%
```

### Failed Prediction Example

```python
data = {
    'FlightNumber': [10],
    'PayloadMass': [7000],
    'Flights': [1],
    'Block': [2],
    'ReusedCount': [0],
    'Orbit': ['LEO'],
    'LaunchSite': ['CCAFS SLC 40'],
    'LandingPad': ['5e9e3032383ecb6bb234e7ca'],
    'Serial': ['B0005'],
    'GridFins': [False],
    'Reused': [False],
    'Legs': [False]
}
features = pd.DataFrame(data)

Prediction: Failed
Probability of Failure: 85.75%
Probability of Success: 14.25%
```


