import streamlit as st
from PIL import Image
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

model= pickle.load(open('loanpred.pkl','rb'))
data = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')
train_x = pd.read_csv('train_u6lujuX_CVtuZ9i.csv')

rad = st.sidebar.radio("**Navigation**",["Home","Visualisation","Model"])
if rad == "Home":
    st.title("Loan Prediction Data :money_with_wings:")
    s = st.expander("----------------------------------------------------------------------------",False)
    if s.checkbox("Display Data"):
        st.write("Shape of the table",data.shape)
        option = ('5 columns', '10 columns', '20 columns', 'Whole table')
        option_dis = list(range(len(option)))
        x = st.selectbox("Choose Table size",option_dis,format_func=lambda x: option[x])
        if x==0:
            st.write(data.head())
        if x==1:
            st.write(data.head(10))
        if x==2:
            st.write(data.head(20))
        if x==3:
            st.write(data)

if rad =="Visualisation":
    st.title("Data Visualisation :bar_chart:")
    vis = ('Correlation','Important Features','PCA')
    vis_dis = list(range(len(vis)))
    y= st.selectbox("Choose Visuals",vis_dis,format_func=lambda x: vis[x])
    if y==0:
        train_x['Loan_Status'] = train_x['Loan_Status'].map({'Y':1,'N':0})
        fig, ax = plt.subplots()
        sns.heatmap(train_x.corr(),ax=ax)
        st.write(fig)
    if y==1:
        img = Image.open('imp_features.jpg')
        img = img.resize((1000,500))
        st.image(img,use_column_width=False)
    if y==2:
        img2= Image.open('pca.jpg')
        img2 = img2.resize((1000,500))
        st.image(img2,use_column_width=False)



if rad == "Model":
    img1 = Image.open('loan amt.jpg')
    img1 = img1.resize((900,500))
    st.image(img1,use_column_width=False)
    st.title("Bank Loan Prediction Model :money_mouth_face:")
    #st.markdown(":money_mouth_face:")

    #account no
    account_no = st.text_input("Account No")

    #full name
    fn = st.text_input('Full name')

    #gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox('Gender',gen_options,format_func=lambda x: gen_display[x])

    #marital status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox('Marital Status',mar_options,format_func=lambda x: mar_display[x])

    #No of Dependents
    dep_display = ('No','One','Two','3 or more')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox('Dependents',dep_options,format_func=lambda x: dep_display[x])

    #Education status
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox('Education status',edu_options,format_func=lambda x: edu_display[x])

    #property status
    prop_display = ('Rural','Semiurban','Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox('Property Area',prop_options,format_func=lambda x: prop_display[x])

    #employment status
    emp_display = ("Job","Business")
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    #Cedit history
    cred_display = ('Between 300 to 500','Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox('Cedit score',cred_options,format_func=lambda x: cred_options[x])

    #Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)",value=0)

    #Co-applicantMonthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)",value=0)

    #Loan_Amount
    loan_amt = st.number_input('Loan Amount',value=0)

    #Loan Duration
    dur_display = ('2 Months','6 Months','8 Months','1 Year','16 Months')
    dur_options = list(range(len(dur_display)))
    dur = st.selectbox('Loan Duration',dur_options,format_func=lambda x: dur_display[x])


    if st.button("Submit"):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i+1)
        duration=0
        if dur==0:
            duration = 60
        if dur==1:
            duration = 180
        if dur==2:
            duration = 240
        if dur==3:
            duration = 360
        if dur==4:
            duration = 480
        features = [[gen,mar,dep,edu,prop,cred,mon_income,co_mon_income,loan_amt,dur,emp]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans==0:
            st.error(
                "Hello: " +fn + " || "
                "Account No: "+account_no + " || "
                "Oops! YOUR LOAN WILL NOT BE APPROVED "
                ":slightly_frowning_face:"
            )
        else:
            st.success(
                "Hello: "+ fn +" || "
                "Account No: "+account_no+" || "
                "Congratulations!! YOUR LOAN WILL GET APPROVED "
                ":smiley:"
            )




