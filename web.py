import streamlit as st
import math

st.title('Aplikasi perhitungan Normalitas dan Persentase kadar',)


st.write('Oleh Kelompok 4')
st.write('Amanda Adistya Pasya          (2360067)')
st.write('Aufa Azhzhahra Dalillah HFB   (2360079)')
st.write('Nayla Putri Dwinta            (2360209)')
st.write('Rizky Amelia Putri            (2360247)')
st.write('Zahra Yasmin Zafira           (2360296)')

tab1, tab2,= st.tabs(["Perhitungan Normalitas","Perhitungan kadar titrat(mL)",])

with tab1:
    default_value = 1.0000
    min_value = 0.0000
    max_value = 9999.0000
    
    massa = st.number_input('Masukkan nilai massa (mg)',format="%.4f",value=default_value,)
    volume = st.number_input('Masukkan nilai volume (mL)',format="%.2f",value=default_value,)
    BE1 = st.number_input('Masukkan nilai BE',format="%.1f",value=default_value,)
    FP1 = st.number_input('Masukkan nilai F Pengali',format="%.0f",value=default_value,)

    tombol = st.button('Hitung nilai normalitasnya')

    nilai_normalitas1=massa/(BE1*volume*FP1)
    if tombol:
        nilai_normalitas = massa/(BE1*volume*FP1)
        st.success(f'Nilai normalitas adalah {nilai_normalitas:.4f}')

with tab2:
    default_value = 1.0000
    min_value = 0.0000
    max_value = 9999.0000

    Vtitran = st.number_input('Masukkan nilai volume titran (mL)')
    Ntitran = st.number_input('Masukkan nilai normalitas titran (N)',format='%.4f', value=(nilai_normalitas1))
    BE2 = st.number_input('Masukkan nilai BEnya',format="%.1f")
    FP2 = st.number_input('Masukkan nilai F Pengalinya',format="%.0f")
    Vtitrat = st.number_input('Masukkan nilai volume titrat (mL)',format="%.0f")

    tombol = st.button('Hitung nilai kadarnya')

    if tombol:
        nilai_kadar = (Vtitran*Ntitran*BE2*10**-3*FP2*100)/Vtitrat 
        st.success(f'Persentase kadarnya adalah {nilai_kadar:.2f}%')