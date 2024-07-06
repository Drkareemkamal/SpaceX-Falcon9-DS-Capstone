# import streamlit as st
# import pandas as pd
# import joblib

# from sklearn import preprocessing
# from sklearn.model_selection import train_test_split



# st.sidebar.header('User Input Parameters')

# def user_input_features():
#     flight_number = st.number_input("Insert a FlightNumber")
#     payload_mass = st.sidebar.slider('Payload Mass', 350, 30000, 1000)

#     flights = st.sidebar.slider('Flights', 1, 6, 3)

#     block = st.sidebar.slider('Block', 1,5,1 )
#     orbit = st.sidebar.selectbox('Orbit',('LEO', 'ISS', 'PO', 'GTO', 'ES-L1', 'SSO', 'HEO', 'MEO', 'VLEO',
#        'SO', 'GEO'))

#     reused_count = st.number_input('Insert a ReusedCount')
    
#     launch_site = st.sidebar.selectbox('LaunchSite',('CCAFS SLC 40', 'VAFB SLC 4E', 'KSC LC 39A'))
    
#     LandingPad = st.sidebar.selectbox('LandingPad',('5e9e3032383ecb761634e7cb', '5e9e3032383ecb6bb234e7ca',
#        '5e9e3032383ecb267a34e7c7', '5e9e3033383ecbb9e534e7cc',
#        '5e9e3032383ecb554034e7c9'))

#     serial = st.sidebar.selectbox('Serial',('B0003', 'B0005', 'B0007', 'B1003', 'B1004', 'B1005', 'B1006',
#        'B1007', 'B1008', 'B1011', 'B1010', 'B1012', 'B1013', 'B1015',
#        'B1016', 'B1018', 'B1019', 'B1017', 'B1020', 'B1021', 'B1022',
#        'B1023', 'B1025', 'B1026', 'B1028', 'B1029', 'B1031', 'B1030',
#        'B1032', 'B1034', 'B1035', 'B1036', 'B1037', 'B1039', 'B1038',
#        'B1040', 'B1041', 'B1042', 'B1043', 'B1044', 'B1045', 'B1046',
#        'B1047', 'B1048', 'B1049', 'B1050', 'B1054', 'B1051', 'B1056',
#        'B1059', 'B1058', 'B1060', 'B1062'))

#     gridfins = st.sidebar.selectbox('GridFins', (False, True))

#     reused = st.sidebar.selectbox('Reused', (False, True))

#     legs = st.sidebar.selectbox('Legs', (False, True))

    
#     data = {'FlightNumber' : [flight_number] ,
#         'PayloadMass': [payload_mass],
#             'flights' : [flights],
#             'block' : [block] ,
#             'ReusedCount' : [reused_count] , 
#             'Orbit': [orbit],
#             'LaunchSite' : [launch_site] ,
#             'LandingPad' : [LandingPad] ,
#             'Serial' : [serial] ,
#             'GridFins' : [gridfins] ,
#             'Reused' : [reused] ,
#             'Legs' : [legs]
#             }
    
#     features = pd.DataFrame(data)
#     return features

# df = user_input_features()


# # One-hot encode the categorical columns
# categorical_columns = ['Orbit', 'LaunchSite', 'LandingPad', 'Serial', 'GridFins', 'Reused', 'Legs']
# df_encoded = pd.get_dummies(df, columns=categorical_columns)

# # Define the columns of the uploaded CSV file
# csv_columns = ['FlightNumber', 'PayloadMass', 'Flights', 'Block', 'ReusedCount',
#                'Orbit_ES-L1', 'Orbit_GEO', 'Orbit_GTO', 'Orbit_HEO', 'Orbit_ISS',
#                'Orbit_LEO', 'Orbit_MEO', 'Orbit_PO', 'Orbit_SO', 'Orbit_SSO',
#                'Orbit_VLEO', 'LaunchSite_CCAFS SLC 40', 'LaunchSite_KSC LC 39A',
#                'LaunchSite_VAFB SLC 4E', 'LandingPad_5e9e3032383ecb267a34e7c7',
#                'LandingPad_5e9e3032383ecb554034e7c9',
#                'LandingPad_5e9e3032383ecb6bb234e7ca',
#                'LandingPad_5e9e3032383ecb761634e7cb',
#                'LandingPad_5e9e3033383ecbb9e534e7cc', 'Serial_B0003', 'Serial_B0005',
#                'Serial_B0007', 'Serial_B1003', 'Serial_B1004', 'Serial_B1005',
#                'Serial_B1006', 'Serial_B1007', 'Serial_B1008', 'Serial_B1010',
#                'Serial_B1011', 'Serial_B1012', 'Serial_B1013', 'Serial_B1015',
#                'Serial_B1016', 'Serial_B1017', 'Serial_B1018', 'Serial_B1019',
#                'Serial_B1020', 'Serial_B1021', 'Serial_B1022', 'Serial_B1023',
#                'Serial_B1025', 'Serial_B1026', 'Serial_B1028', 'Serial_B1029',
#                'Serial_B1030', 'Serial_B1031', 'Serial_B1032', 'Serial_B1034',
#                'Serial_B1035', 'Serial_B1036', 'Serial_B1037', 'Serial_B1038',
#                'Serial_B1039', 'Serial_B1040', 'Serial_B1041', 'Serial_B1042',
#                'Serial_B1043', 'Serial_B1044', 'Serial_B1045', 'Serial_B1046',
#                'Serial_B1047', 'Serial_B1048', 'Serial_B1049', 'Serial_B1050',
#                'Serial_B1051', 'Serial_B1054', 'Serial_B1056', 'Serial_B1058',
#                'Serial_B1059', 'Serial_B1060', 'Serial_B1062', 'GridFins_False',
#                'GridFins_True', 'Reused_False', 'Reused_True', 'Legs_False',
#                'Legs_True']

# # Align the columns of df_encoded with the columns of the uploaded CSV file
# df_encoded = df_encoded.reindex(columns=csv_columns, fill_value=0)

# st.write(df_encoded)


# transform = preprocessing.StandardScaler()
# X = transform.fit_transform(df_encoded)

# df_scaled = pd.DataFrame(X,columns=df_encoded.columns)
# print(df_scaled)
# st.write(df_scaled)



# model_path = 'decision_tree.joblib'

# model = joblib.load(model_path)

# st.write('Model is loaded successfully')




# st.title("SpaceX Stage 1 Failed Predictor")


# # # Prediction
# if st.button("Submit"):
#     classes = ['Failed','Success']
#     prediction = model.predict(df_scaled)
#     st.write(f"Prediction: {prediction}")

################################################################

# import streamlit as st
# import pandas as pd
# import joblib
# from sklearn import preprocessing
# from sklearn.model_selection import train_test_split

# st.sidebar.header('User Input Parameters')

# def user_input_features():
#     flight_number = st.number_input("Insert a FlightNumber")
#     payload_mass = st.sidebar.slider('Payload Mass', 350, 30000, 1000)
#     flights = st.sidebar.slider('Flights', 1, 6, 3)
#     block = st.sidebar.slider('Block', 1, 5, 1)
#     orbit = st.sidebar.selectbox('Orbit', ('LEO', 'ISS', 'PO', 'GTO', 'ES-L1', 'SSO', 'HEO', 'MEO', 'VLEO', 'SO', 'GEO'))
#     reused_count = st.number_input('Insert a ReusedCount')
#     launch_site = st.sidebar.selectbox('LaunchSite', ('CCAFS SLC 40', 'VAFB SLC 4E', 'KSC LC 39A'))
#     LandingPad = st.sidebar.selectbox('LandingPad', ('5e9e3032383ecb761634e7cb', '5e9e3032383ecb6bb234e7ca',
#                                                      '5e9e3032383ecb267a34e7c7', '5e9e3033383ecbb9e534e7cc',
#                                                      '5e9e3032383ecb554034e7c9'))
#     serial = st.sidebar.selectbox('Serial', ('B0003', 'B0005', 'B0007', 'B1003', 'B1004', 'B1005', 'B1006',
#                                              'B1007', 'B1008', 'B1011', 'B1010', 'B1012', 'B1013', 'B1015',
#                                              'B1016', 'B1018', 'B1019', 'B1017', 'B1020', 'B1021', 'B1022',
#                                              'B1023', 'B1025', 'B1026', 'B1028', 'B1029', 'B1031', 'B1030',
#                                              'B1032', 'B1034', 'B1035', 'B1036', 'B1037', 'B1039', 'B1038',
#                                              'B1040', 'B1041', 'B1042', 'B1043', 'B1044', 'B1045', 'B1046',
#                                              'B1047', 'B1048', 'B1049', 'B1050', 'B1054', 'B1051', 'B1056',
#                                              'B1059', 'B1058', 'B1060', 'B1062'))
#     gridfins = st.sidebar.selectbox('GridFins', (False, True))
#     reused = st.sidebar.selectbox('Reused', (False, True))
#     legs = st.sidebar.selectbox('Legs', (False, True))

#     data = {
#         'FlightNumber': [flight_number],
#         'PayloadMass': [payload_mass],
#         'Flights': [flights],
#         'Block': [block],
#         'ReusedCount': [reused_count],
#         'Orbit': [orbit],
#         'LaunchSite': [launch_site],
#         'LandingPad': [LandingPad],
#         'Serial': [serial],
#         'GridFins': [gridfins],
#         'Reused': [reused],
#         'Legs': [legs]
#     }
    
#     features = pd.DataFrame(data)
#     return features

# df = user_input_features()

# # One-hot encode the categorical columns
# categorical_columns = ['Orbit', 'LaunchSite', 'LandingPad', 'Serial', 'GridFins', 'Reused', 'Legs']
# df_encoded = pd.get_dummies(df, columns=categorical_columns)

# # Define the columns of the uploaded CSV file
# csv_columns = ['FlightNumber', 'PayloadMass', 'Flights', 'Block', 'ReusedCount',
#                'Orbit_ES-L1', 'Orbit_GEO', 'Orbit_GTO', 'Orbit_HEO', 'Orbit_ISS',
#                'Orbit_LEO', 'Orbit_MEO', 'Orbit_PO', 'Orbit_SO', 'Orbit_SSO',
#                'Orbit_VLEO', 'LaunchSite_CCAFS SLC 40', 'LaunchSite_KSC LC 39A',
#                'LaunchSite_VAFB SLC 4E', 'LandingPad_5e9e3032383ecb267a34e7c7',
#                'LandingPad_5e9e3032383ecb554034e7c9',
#                'LandingPad_5e9e3032383ecb6bb234e7ca',
#                'LandingPad_5e9e3032383ecb761634e7cb',
#                'LandingPad_5e9e3033383ecbb9e534e7cc', 'Serial_B0003', 'Serial_B0005',
#                'Serial_B0007', 'Serial_B1003', 'Serial_B1004', 'Serial_B1005',
#                'Serial_B1006', 'Serial_B1007', 'Serial_B1008', 'Serial_B1010',
#                'Serial_B1011', 'Serial_B1012', 'Serial_B1013', 'Serial_B1015',
#                'Serial_B1016', 'Serial_B1017', 'Serial_B1018', 'Serial_B1019',
#                'Serial_B1020', 'Serial_B1021', 'Serial_B1022', 'Serial_B1023',
#                'Serial_B1025', 'Serial_B1026', 'Serial_B1028', 'Serial_B1029',
#                'Serial_B1030', 'Serial_B1031', 'Serial_B1032', 'Serial_B1034',
#                'Serial_B1035', 'Serial_B1036', 'Serial_B1037', 'Serial_B1038',
#                'Serial_B1039', 'Serial_B1040', 'Serial_B1041', 'Serial_B1042',
#                'Serial_B1043', 'Serial_B1044', 'Serial_B1045', 'Serial_B1046',
#                'Serial_B1047', 'Serial_B1048', 'Serial_B1049', 'Serial_B1050',
#                'Serial_B1051', 'Serial_B1054', 'Serial_B1056', 'Serial_B1058',
#                'Serial_B1059', 'Serial_B1060', 'Serial_B1062', 'GridFins_False',
#                'GridFins_True', 'Reused_False', 'Reused_True', 'Legs_False',
#                'Legs_True']

# # Align the columns of df_encoded with the columns of the uploaded CSV file
# df_encoded = df_encoded.reindex(columns=csv_columns, fill_value=0)

# st.write(df_encoded)

# # Apply StandardScaler to numerical columns
# numerical_columns = ['FlightNumber', 'PayloadMass', 'Flights', 'Block', 'ReusedCount']
# scaler = preprocessing.StandardScaler()
# df_encoded[numerical_columns] = scaler.fit_transform(df_encoded[numerical_columns])

# st.write(df_encoded)

# model_path = 'decision_tree.joblib'
# model = joblib.load(model_path)

# st.write('Model is loaded successfully')

# st.title("SpaceX Stage 1 Failed Predictor")

# # Prediction
# if st.button("Submit"):
#     classes = ['Failed', 'Success']
#     prediction = model.predict(df_encoded)
#     st.write(f"Prediction: {classes[prediction[0]]} with the {prediction}")

import streamlit as st
import pandas as pd
import joblib
from sklearn import preprocessing

st.sidebar.header('User Input Parameters')

def user_input_features():
    flight_number = st.number_input("Insert a FlightNumber")
    payload_mass = st.sidebar.slider('Payload Mass', 350, 30000, 1000)
    flights = st.sidebar.slider('Flights', 1, 6, 3)
    block = st.sidebar.slider('Block', 1, 5, 1)
    orbit = st.sidebar.selectbox('Orbit', ('LEO', 'ISS', 'PO', 'GTO', 'ES-L1', 'SSO', 'HEO', 'MEO', 'VLEO', 'SO', 'GEO'))
    reused_count = st.number_input('Insert a ReusedCount')
    launch_site = st.sidebar.selectbox('LaunchSite', ('CCAFS SLC 40', 'VAFB SLC 4E', 'KSC LC 39A'))
    LandingPad = st.sidebar.selectbox('LandingPad', ('5e9e3032383ecb761634e7cb', '5e9e3032383ecb6bb234e7ca', '5e9e3032383ecb267a34e7c7', '5e9e3033383ecbb9e534e7cc', '5e9e3032383ecb554034e7c9'))
    serial = st.sidebar.selectbox('Serial', ('B0003', 'B0005', 'B0007', 'B1003', 'B1004', 'B1005', 'B1006', 'B1007', 'B1008', 'B1011', 'B1010', 'B1012', 'B1013', 'B1015', 'B1016', 'B1018', 'B1019', 'B1017', 'B1020', 'B1021', 'B1022', 'B1023', 'B1025', 'B1026', 'B1028', 'B1029', 'B1031', 'B1030', 'B1032', 'B1034', 'B1035', 'B1036', 'B1037', 'B1039', 'B1038', 'B1040', 'B1041', 'B1042', 'B1043', 'B1044', 'B1045', 'B1046', 'B1047', 'B1048', 'B1049', 'B1050', 'B1054', 'B1051', 'B1056', 'B1059', 'B1058', 'B1060', 'B1062'))
    gridfins = st.sidebar.selectbox('GridFins', (False, True))
    reused = st.sidebar.selectbox('Reused', (False, True))
    legs = st.sidebar.selectbox('Legs', (False, True))

    data = {
        'FlightNumber': [flight_number],
        'PayloadMass': [payload_mass],
        'Flights': [flights],
        'Block': [block],
        'ReusedCount': [reused_count],
        'Orbit': [orbit],
        'LaunchSite': [launch_site],
        'LandingPad': [LandingPad],
        'Serial': [serial],
        'GridFins': [gridfins],
        'Reused': [reused],
        'Legs': [legs]
    }
    
    features = pd.DataFrame(data)
    return features

df = user_input_features()

# One-hot encode the categorical columns
categorical_columns = ['Orbit', 'LaunchSite', 'LandingPad', 'Serial', 'GridFins', 'Reused', 'Legs']
df_encoded = pd.get_dummies(df, columns=categorical_columns)

# Define the columns of the uploaded CSV file
csv_columns = ['FlightNumber', 'PayloadMass', 'Flights', 'Block', 'ReusedCount',
               'Orbit_ES-L1', 'Orbit_GEO', 'Orbit_GTO', 'Orbit_HEO', 'Orbit_ISS',
               'Orbit_LEO', 'Orbit_MEO', 'Orbit_PO', 'Orbit_SO', 'Orbit_SSO',
               'Orbit_VLEO', 'LaunchSite_CCAFS SLC 40', 'LaunchSite_KSC LC 39A',
               'LaunchSite_VAFB SLC 4E', 'LandingPad_5e9e3032383ecb267a34e7c7',
               'LandingPad_5e9e3032383ecb554034e7c9',
               'LandingPad_5e9e3032383ecb6bb234e7ca',
               'LandingPad_5e9e3032383ecb761634e7cb',
               'LandingPad_5e9e3033383ecbb9e534e7cc', 'Serial_B0003', 'Serial_B0005',
               'Serial_B0007', 'Serial_B1003', 'Serial_B1004', 'Serial_B1005',
               'Serial_B1006', 'Serial_B1007', 'Serial_B1008', 'Serial_B1010',
               'Serial_B1011', 'Serial_B1012', 'Serial_B1013', 'Serial_B1015',
               'Serial_B1016', 'Serial_B1017', 'Serial_B1018', 'Serial_B1019',
               'Serial_B1020', 'Serial_B1021', 'Serial_B1022', 'Serial_B1023',
               'Serial_B1025', 'Serial_B1026', 'Serial_B1028', 'Serial_B1029',
               'Serial_B1030', 'Serial_B1031', 'Serial_B1032', 'Serial_B1034',
               'Serial_B1035', 'Serial_B1036', 'Serial_B1037', 'Serial_B1038',
               'Serial_B1039', 'Serial_B1040', 'Serial_B1041', 'Serial_B1042',
               'Serial_B1043', 'Serial_B1044', 'Serial_B1045', 'Serial_B1046',
               'Serial_B1047', 'Serial_B1048', 'Serial_B1049', 'Serial_B1050',
               'Serial_B1051', 'Serial_B1054', 'Serial_B1056', 'Serial_B1058',
               'Serial_B1059', 'Serial_B1060', 'Serial_B1062', 'GridFins_False',
               'GridFins_True', 'Reused_False', 'Reused_True', 'Legs_False',
               'Legs_True']

# Align the columns of df_encoded with the columns of the uploaded CSV file
df_encoded = df_encoded.reindex(columns=csv_columns, fill_value=0)

st.write(df_encoded)

# Apply StandardScaler to numerical columns
numerical_columns = ['FlightNumber', 'PayloadMass', 'Flights', 'Block', 'ReusedCount']
scaler = preprocessing.StandardScaler()
df_encoded[numerical_columns] = scaler.fit_transform(df_encoded[numerical_columns])

st.write(df_encoded)

model_path = 'decision_tree.joblib'
model = joblib.load(model_path)

st.write('Model is loaded successfully')

st.title("SpaceX Stage 1 Failed Predictor")

# Prediction
if st.button("Submit"):
    prediction_proba = model.predict_proba(df_encoded)
    #st.write(f"Prediction: {prediction_proba}")
    
    fail_proba = prediction_proba[0][0] * 100
    success_proba = prediction_proba[0][1] * 100

    st.write(f"Probability of Failure: {fail_proba:.2f}%")
    st.write(f"Probability of Success: {success_proba:.2f}%")
