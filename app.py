# ########## library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import streamlit as st

# ########## data preparetion

day = pd.read_csv('day_clean.csv')
hour = pd.read_csv('hour_clean.csv')

hour = hour.drop([hour.keys()[0]], axis=1)
cols = ['season', 'year', 'holiday', 'weekday', 'workingday', 'weathersit']
for col in cols:
    hour[col] = hour[col].astype('category')
hour['hour'] = hour['hour'].astype('category')

day['date'] = pd.to_datetime(day['date'], yearfirst=True)
day.index = day['date']
day = day.drop(['date'], axis=1)

for col in cols:
    day[col] = day[col].astype('category')

# ########## title

st.title('Bike Sharing Analysis')

# ########## metric

metric_casual = day['casual'].sum()
metric_registered = day['registered'].sum()
metric_y = day['y'].sum()

st.header('Metrics of Total Rental')
col_1, col_2, col_3 = st.columns(3)

with col_1:
    st.metric(label='Total Rental Casual Users', value=metric_casual)
with col_2:
    st.metric(label='Total Rental Registered Users', value=metric_registered)
with col_3:
    st.metric(label='Total Rental Registered Users', value=metric_y)

# ########## viz for day dataset

st.subheader('Users of Bike Sharing')
users = st.selectbox('Users of Bike Sharing',
             options=['casual', 'registered', 'y'],
             label_visibility='hidden')

fig, ax = plt.subplots(figsize=(16,7))
day[users].plot(ax=ax)

st.pyplot(fig)

# ########## hour dataset
col_cat = hour.keys()[:7]
cols_num = hour.keys()[7:]

# ########## viz for box plot

st.subheader('Boxplot Viz')
boxplot_viz = st.selectbox('Boxplot Viz',
                           options=cols_num,
                           label_visibility='hidden')

fig, ax = plt.subplots(figsize=(16,5))
sns.boxplot(data=hour, x=boxplot_viz)
st.pyplot(fig)

# ########## viz rental based on hour

st.subheader("viz rental users every hour")
col_1, col_2 = st.columns(2)

with col_1:
    one = st.selectbox('user',
                 options=['casual', 'registered', 'y'])
    
with col_2:
    two = st.selectbox('category',
                       options=col_cat)
    
fig, ax = plt.subplots(figsize=(16,10))
sns.pointplot(data=hour, x='hour', y=one, hue=two, ax=ax)
st.pyplot(fig)

# ########## viz correlation matriz

st.subheader("total user based on category")
col_1a, col_1b = st.columns(2)

with col_1a:
    one_a = st.selectbox('user a',
                 options=['casual', 'registered', 'y'])
    
with col_1b:
    one_b = st.selectbox('category a',
                       options=col_cat)
    
col_2a, col_2b = st.columns(2)

with col_2a:
    two_a = st.selectbox('user b',
                 options=['y', 'registered', 'casual'])
    
with col_2b:
    two_b = st.selectbox('category b',
                       options=col_cat)
    
fig, (ax1, ax2) = plt.subplots(nrows=2)
sns.barplot(data=hour, x=one_b, y=one_a, ax=ax1)
sns.barplot(data=hour, x=two_b, y=two_a, ax=ax2)

st.pyplot(fig)