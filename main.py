import streamlit as st
import random
st.title('나의 첫번째 앱')
st.text('n/n')
st.write('안녕하세요 나는 상우 짱친 양서진 입니다.')
st.write('저의 이메일은 24_10513@daejin.sen.hs.kr')

st.button("Reset", type="primary")
if st.button("난수생성"):
    st.write(random.randint(1,1000))
else:
    st.write("안녕")
