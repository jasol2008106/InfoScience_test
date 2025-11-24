import streamlit as st

st.title('My First Streamlit Site')
name = st.text_input('이름을 입력해라')
menu = st.selectbox('가장 많이 쓰는 앱은?', ['구글', '스팀', '지오지브라', '쿠팡'])
time = st.slider('하루 사용 시간은?', 0, 24, 3)

if st.button('결과 보기'):
    st.write(f'{name}님은 {menu}을/를 가장 많이 사용합니다. 하루 평균 {time}시간 사용합니다.')
    st.balloons()
