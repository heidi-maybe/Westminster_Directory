import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import re 
st.set_page_config(page_title="WU Directory", layout="wide")

st.title('Directory at Westminster University')

st.write("This is an enhanced alternative to the employee [directory](https://westminsteru.edu/campus-directory/index.html) at Westminster University." )

data = pd.read_csv('WU_directory.csv') 


# option = st.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone"),
# )

# st.write("You selected:", option)

##################### Drop down box ##############################

department_list = data['Department'].unique()
department_list = np.insert(department_list, 0, "All Departments")
department = st.selectbox(label = 'Choose one department from below:', options = department_list)


if department != "All Departments":
    data = data.query("Department == '{}'".format(department))


##################### Check box ##############################
col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Type of Role:") # add a text 
with col2:
    role_faculty = st.checkbox('Faculty', value=1)
with col3:
    role_staff = st.checkbox('Staff', value=1)

if not role_faculty:
    data = data.query("Role == 'Staff'")
if not role_staff:
    data = data.query("Role == 'Faculty'")


col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Type of Contract:") # add a text 
with col2:
    cont_full = st.checkbox('Full Time', value=1)
with col3:
    cont_part = st.checkbox('Part Time', value=1)

if not cont_full:
    data = data.query("Contract == 'PART-TIME'")
if not cont_part:
    data = data.query("Contract == 'FULL-TIME'")

col1, col2, col3, col4, col5 = st.columns([0.2,0.2,0.2,0.2,0.4])
with col1:
    st.text("Type of Rank:") # add a text 
with col2:
    rank_assistant = st.checkbox('Assistant', value=1)
with col3:
    rank_associate = st.checkbox('Associate', value=1)
with col4:
    rank_full = st.checkbox('Full', value=1)

if not rank_assistant:
    data = data.query("Position != 'Assistant Professor'")
if not rank_associate:
    data = data.query("Position != 'Associate Professor'")


##################### Text box regex ##############################
col1, col2, col3, col4 = st.columns([0.1,0.4,0.2,0.4])
with col1:
    st.text("Name:")
with col2:
    text_box = st.text_input('Type Condition:')
with col3:
    regex = st.checkbox('Regex', value=0)

if text_box != "":
    data = data.query("Name  == '{}'".format(text_box))
if regex:
    data = data["Name"].str.containts('{}'.format(text_box), regex=True)



st.dataframe(data, hide_index=True)
