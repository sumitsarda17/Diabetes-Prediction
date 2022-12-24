import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model', 'rb'))


st.write("made by Sumit Sarda")


# sidebar creation
option = st.sidebar.selectbox(
    "Choose the Factor for which you want to know about",
    ("Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age")
)

if(option == "Pregnancies"):
  st.sidebar.write("Study shows that At least 4 pregnancies through childbearing age may be a potential risk factor for diabetes in postmenopausal women without a history of gestational diabetes.")

elif(option == "Glucose"):
  st.sidebar.write("Normal Blood Sugar Level should be less than 100 mg/dL after not eating (fasting) for at least 8 hours. And they're less than 140 mg/dL 2 hours after eating.")
  st.sidebar.write("Any sugar levels higher than normal are unhealthy, which can leads to diabetes")
  st.sidebar.write("The American Diabetes Association's goals for blood sugar control in people with diabetes are 70 to 130 mg/dL before meals, and less than 180 mg/dL after meals.")

elif(option == "BloodPressure"):
  st.sidebar.write("Blood pressure numbers of less than 120/80 mm Hg are considered within the normal range.")
  st.sidebar.write("Elevated blood pressure is when readings consistently range from 120-129 systolic and less than 80 mm Hg diastolic.")
  st.sidebar.write("Hypertension Stage 1 is when blood pressure consistently ranges from 130-139 systolic or 80-89 mm Hg diastolic")
  st.sidebar.write("Hypertension Stage 2 is when blood pressure consistently ranges at 140/90 mm Hg or higher.")
  st.sidebar.write("Hypertension can leads to diabetes and sometimes due to diabetes the Blood Pressure can increase upto HT")

elif(option == "SkinThickness"):
  st.sidebar.write("Skinfold thickness of the triceps (mm)")

elif(option == "Insulin"):
  st.sidebar.write("In")
  
elif(option == "BMI"):
  st.sidebar.write("BMI")

elif(option == "DiabetesPedigreeFunction"):
  st.sidebar.write("Dia")

else:
  st.sidebar.write("Age")

  
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
    
    Pregnancies = st.number_input('Pregnancies - number of times an individual has been pregnant', step=1.)
    Glucose = st.number_input('Glucose - blood plasma glucose concentration after a 2 hour oral glucose tolerance test',step=1.)
    BloodPressure = st.number_input('BloodPressure - Diastolic blood pressure (mm/HG)',step=1.)
    SkinThickness = st.number_input('SkinThickness - Skinfold thickness of the triceps (mm)',step=1.)
    Insulin = st.number_input('Insulin - 2 hour serum insulin (mu U/ml)',step=1.)
    BMI = st.number_input('BMI - Body mass index with weight/height (kg/m squared)',step=1.)
    DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction - A function that determines the risk of type 2 diabetes based on family history, the larger the function, the higher the risk of type 2 diabetes',step=1.)
    Age = st.number_input('Age - in years', step=1.)
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()