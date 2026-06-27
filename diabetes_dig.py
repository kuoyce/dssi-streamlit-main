import streamlit as st
from src.inference import get_prediction

if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

DISTRICTS = ['Mailna', 'Jordas', 'Illinoy', 'Jaearon']

def app_sidebar():
    st.sidebar.header('Patient')
    preg = st.sidebar.text_input("Pregnancies")
    glu = st.sidebar.text_input("Glucose")
    bp = st.sidebar.text_input("Blood Pressure")
    st_input = st.sidebar.text_input("Skin Thickness")
    ins = st.sidebar.text_input("Insulin")
    bmi = st.sidebar.text_input("BMI")
    dpf = st.sidebar.text_input("Diabetes Pedigree Function")
    age = st.sidebar.text_input("Age")
    district = st.sidebar.selectbox("District", DISTRICTS)
    def get_input_features():
        input_features = {'Pregnancies': float(preg),
                          'Glucose': float(glu),
                          'BloodPressure': float(bp),
                          'SkinThickness': float(st_input),
                          'Insulin': float(ins),
                          'BMI': float(bmi),
                          'DiabetesPedigreeFunction': float(dpf),
                          'Age': float(age),
                          'District': district
                         }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> DSSI Diabetes Digital Assessment</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(Pregnancies=st.session_state['input_features']['Pregnancies'],
                                    Glucose=st.session_state['input_features']['Glucose'],
                                    BloodPressure=st.session_state['input_features']['BloodPressure'],
                                    SkinThickness=st.session_state['input_features']['SkinThickness'],
                                    Insulin=st.session_state['input_features']['Insulin'],
                                    BMI=st.session_state['input_features']['BMI'],
                                    DiabetesPedigreeFunction=st.session_state['input_features']['DiabetesPedigreeFunction'],
                                    Age=st.session_state['input_features']['Age'],
                                    District=st.session_state['input_features']['District'])
        if assessment == 1:
            st.error(default_msg.format('Diabetic'))
        else:
            st.success(default_msg.format('Not Diabetic'))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()
