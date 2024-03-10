import streamlit as st
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

st.title(" Dashboard Proyek Analisis Data")  
st.header('Bike Sharing Dataset')  
st.subheader('Jumlah Maksimal Keselurahan Pelanggan Berdasarkan Jenis Hari ')
def plot_jenis_chart():       
    jenis_hari = {
        'Jenis Hari': ['Bukan Holiday','Holiday' ],
        'Jumlah': [8714,7403]  # Jumlah pelanggan untuk setiap hari
    }

     # Membuat DataFrame dari data dummy diatas
    df = pd.DataFrame(jenis_hari)

    # Mengurutkan DataFrame berdasarkan kolom 'Jenis Hari'
    df_sorted = df.sort_values(by='Jenis Hari')

    # Menampilkan chart menggunakan Matplotlib
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Jenis Hari'], df_sorted['Jumlah'], color='pink')  

    # Menambahkan caption jumlah data di atas setiap bar
    for i, v in enumerate(df_sorted['Jumlah']):
        ax.text(i, v + 10, str(v), ha='center', va='bottom')
    ax.set_xlabel('Jenis Hari')
    ax.set_ylabel('Jumlah')
    ax.set_title('Jumlah Maksimal Keseluruhan Pelanggan Berdasarkan Jenis Hari')
    
    # Menampilkan chart menggunakan st.pyplot()
    st.pyplot(fig)

plot_jenis_chart()
# Memanggil fungsi untuk menampilkan chart


with st.expander("See explanation"):
    st.write(
        """Berdasarkan grafik diatas diperoleh bahwa jumlah keseluruhan maksimal pelanggan yang meminjam sepeda pada saat bukan holiday lebih banyak daripada saat holiday yaitu 8714 sedangkan saat holiday jumlah pelanggan maksimalnya adalah 7403.        """
    )

st.subheader("Jumlah Maksimal Keseluruhan Pelanggan Setiap Jamnya")
def plot_jam_distribution():  
    Setiap_Jam   = {
        'Pukul': ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23'],   
        'Jumlah': [283,168,132,79,28,66,213,596,839,426,539,663,776,760,750,750,783,976,977,743,567,584,502,256]  # Jumlah maksimal pelanggan setiap harinya 
    }
    df = pd.DataFrame(Setiap_Jam)
    df_sorted = df.sort_values(by='Jumlah', ascending=False)
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Pukul'], df_sorted['Jumlah'], color='skyblue')
    for i, v in enumerate(df_sorted['Jumlah']):
        ax.text(i, v + 10, str(v), ha='center', va='bottom')

    ax.set_xlabel('Pukul')  
    ax.set_ylabel('Jumlah')  
    ax.set_title('Jumlah Maksimal Keseluruhan Pelanggan Setiap Jamnnya')  
    st.pyplot(fig)
plot_jam_distribution()   
with st.expander("See explanation"):
    st.write(
        """Grafik diatas menampilkan jumlah  keseluruhan pelanggan dalam meminjam sepeda setiap jamnnya dan diperoleh bahwa paling banyak pelanggan meminjam sepeda pada pukul 18.
"""
    )
 
st.subheader('Kesimpulan')
st.write(
        """Dengan demikian. dapat disimpulkan bahwa jumlah terbanyak keseluruhan pelanggan yang meminjam sepeda terjadi saat bukan holiday dan pukul 18 adalah waktu dimana terdapat jumlah pelanggan yang meminjam sepeda paling banyak. 
"""
)  