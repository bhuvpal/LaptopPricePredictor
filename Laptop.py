import streamlit as st
import numpy as np
import pandas as pd
import pickle
import math


st.set_page_config('Car Price Predictor')


st.title('Car Price Predictor')

st.divider()

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

col_res = ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440']
col1,col2 = st.columns(2)
with col1:
     company = st.selectbox('Brand Name',sorted(df['Company'].unique())+["None"],index=len(df['Company'].unique()))
with col2:
     name = st.selectbox('Type of Laptop',sorted(df['TypeName'].unique())+["None"],index=len(df['TypeName'].unique()))

ram = st.selectbox("Ram(GB)",df['Ram'].unique())
col3,col4 = st.columns(2)

with col3:
     cpu = st.selectbox('cpu brand',sorted(df['cpu_brand'].unique())+['None'],index=len(df['cpu_brand'].unique()))

with col4:
     gpu = st.selectbox('Graphic Processor brand',sorted(df['gpu_brand'].unique())+['None'],index=len(df['gpu_brand'].unique()))


col5,col6 = st.columns(2)

with col5:
     ips = st.radio('IPS Panel',['No','Yes'])

with col6:
     touch = st.radio('TouchSreen',['No','Yes'])


col7,col8 = st.columns(2)

with col7:
     ssd = st.select_slider('SSD(GB)',sorted(sorted(df['SSD'].unique())+[0]))

with col8:
     hdd = st.select_slider('HDD(GB)',sorted(df['HDD'].unique()))

col9,col10 = st.columns(2)

with col9:
     res = st.selectbox("ScreenResolution",col_res+['None'],len(col_res))

with col10:
     size = st.number_input('ScreenSize')

     
col11,col12 = st.columns(2)

with col11:
     op = st.selectbox("Operating System",df['os'].unique())

with col12:
     wght = st.number_input('Weight of Laptop')


if st.button("Predict"):
    pp1 = None
    x_res = int(res.split('x')[0])
    y_res = int(res.split('x')[1])
    if touch=='No':
        touch=0
    else:
        touch=1
    if ips == 'No':
        ips = 0
    else:
        ips=1
    ppi = (pow((pow(x_res,2) + pow(y_res,2)),0.5))/size
    reshaped_data = np.array([company,name,ram,wght,touch,ips,ppi,cpu,hdd,ssd,gpu,op])
    reshape = reshaped_data.reshape(1,12)

    Predict = pipe.predict(reshape)[0]
    st.header(f'Price of Laptop is {round(np.exp(Predict))}')
     

