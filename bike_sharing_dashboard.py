# Import library yang dibutuhkan
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Dashboard Penyewaan Sepeda')

# Load kedua dataset
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

# Sidebar untuk memilih dataset
dataset_choice = st.sidebar.selectbox(
    'Pilih dataset untuk ditampilkan:',
    ('Dataset Harian (day.csv)', 'Dataset Jam (hour.csv)')
)

# Menampilkan dataset yang dipilih
if dataset_choice == 'Dataset Harian (day.csv)':
    st.subheader('Informasi Dataset Harian')
    st.write(day_data.head())
    
    # Visualisasi pengaruh suhu terhadap penyewaan sepeda
    st.subheader('Pengaruh Suhu terhadap Penyewaan Sepeda')
    fig, ax = plt.subplots()
    sns.scatterplot(x='temp', y='cnt', data=day_data, ax=ax)
    ax.set_title('Pengaruh Suhu terhadap Penyewaan Sepeda')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)
    
    # Visualisasi penyewaan sepeda berdasarkan hari
    st.subheader('Penyewaan Sepeda Berdasarkan Hari')
    fig, ax = plt.subplots()
    sns.barplot(x='weekday', y='cnt', data=day_data, estimator=sum, ax=ax)
    ax.set_title('Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
    ax.set_xlabel('Hari dalam Seminggu')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

else:
    st.subheader('Informasi Dataset Jam')
    st.write(hour_data.head())
    
    # Visualisasi penyewaan sepeda berdasarkan jam
    st.subheader('Penyewaan Sepeda Berdasarkan Jam')
    fig, ax = plt.subplots()
    sns.lineplot(x='hr', y='cnt', data=hour_data, estimator=sum, ax=ax)
    ax.set_title('Penyewaan Sepeda Berdasarkan Jam dalam Sehari')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

# Menampilkan summary data
st.sidebar.write("Statistik Deskriptif dari Dataset:")
if dataset_choice == 'Dataset Harian (day.csv)':
    st.sidebar.write(day_data.describe())
else:
    st.sidebar.write(hour_data.describe())
