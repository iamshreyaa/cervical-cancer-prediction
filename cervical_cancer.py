import streamlit as st
import pickle

# Load the trained model
with open('Model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define function to make predictions
def predict_cervical_cancer(features):
    # Make prediction using the loaded model
    prediction = model.predict([features])[0]
    return prediction

# Main function to run the Streamlit app
def main():
    # Set title for the app
    st.title('Cervical Cancer Prediction')

    # Add input fields for features
    st.subheader('Input Features')
    st.markdown('##### (1: Positive, 0: Negative)')

    stds_cervical_condylomatosis = st.number_input(label='STDs cervical condylomatosis', value=0, min_value=0, max_value=1, key='condylomatosis')
    stds_aids = st.number_input(label='STDs AIDS', value=0, min_value=0, max_value=1, key='aids')
    schiller = st.number_input(label='Schiller', value=0, min_value=0, max_value=1, key='schiller')
    hinselmann = st.number_input(label='Hinselmann', value=0, min_value=0, max_value=1, key='hinselmann')
    citology = st.number_input(label='Citology', value=0, min_value=0, max_value=1, key='citology')
    smokes_years = st.number_input(label='Smokes (years)', value=0, min_value=0, max_value=100, key='smokes')
    hormonal_contraceptives_years = st.number_input(label='Hormonal Contraceptives (years)', value=0, min_value=0, max_value=100, key='contraceptives')
    dx_hpv = st.number_input(label='Dx HPV', value=0, min_value=0, max_value=1, key='hpv')
    dx_cancer = st.number_input(label='Dx Cancer', value=0, min_value=0, max_value=1, key='cancer')
    dx = st.number_input(label='Dx Cin', value=0, min_value=0, max_value=1, key='dx')
    stds_genital_herpes = st.number_input(label='STDs genital herpes', value=0, min_value=0, max_value=1, key='herpes')
    stds_number = st.number_input(label='STDs (number)', value=0, min_value=0, max_value=10, key='number')

    # Create a button to trigger prediction
    if st.button('Predict'):
        try:
            # Get input feature values
            features = {
                'STDs cervical condylomatosis': stds_cervical_condylomatosis,
                'STDs AIDS': stds_aids,
                'Schiller': schiller,
                'Hinselmann': hinselmann,
                'Citology': citology,
                'Smokes (years)': smokes_years,
                'Hormonal Contraceptives (years)': hormonal_contraceptives_years,
                'Dx HPV': dx_hpv,
                'Dx Cancer': dx_cancer,
                'Dx Cin': dx,
                'STDs genital herpes': stds_genital_herpes,
                'STDs (number)': stds_number
            }

            # Make prediction using the loaded model
            prediction = predict_cervical_cancer(list(features.values()))

            # Display prediction result
            st.subheader('Prediction Result')
            if prediction == 1:
                st.write('The user has a chance of having cervical cancer.')
            else:
                st.write('The user does not have a chance of having cervical cancer.')
        except Exception as e:
            st.error(f'Error: {e}')

if __name__ == '__main__':
    main()

