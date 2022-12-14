import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.number_input('Number of Pregnancies', step=1.)
    Glucose = st.number_input('Glucose Level',step=1.)
    BloodPressure = st.number_input('Blood Pressure value',step=1.)
    SkinThickness = st.number_input('Skin Thickness value',step=1.)
    Insulin = st.number_input('Insulin Level',step=1.)
    BMI = st.number_input('BMI value',step=1.)
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value',step=1.)
    Age = st.number_input('Age of the Person', step=1.)
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()