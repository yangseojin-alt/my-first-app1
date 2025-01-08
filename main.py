import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="나의 첫 번째 앱",
    page_icon="🌟",
    layout="wide",
)

# 헤더
st.title("🌟 나의 첫 번째 Streamlit 앱 🌟")
st.subheader("Streamlit를 사용해 웹 앱을 쉽게 만들어보세요!")

# 컬럼 레이아웃
col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://www.google.com/url?sa=i&url=https%3A%2F%2Flifesci.korea.ac.kr%2F&psig=AOvVaw1BAm7xgBltRaHvsKGKCTZP&ust=1736389906464000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKjilMKK5YoDFQAAAAAdAAAAABAE", 
        caption="멋진 이미지를 추가하세요!", 
        use_column_width=True
    )

with col2:
    st.write(
        """
        ### Streamlit로 무엇을 할 수 있나요?
        - 데이터 대시보드 만들기
        - 머신러닝 모델 결과 시각화
        - 간단한 사용자 입력 및 출력 관리
        - 웹 개발 경험 없이도 동작 가능!

        아래에서 직접 시험해보세요! 🎉
        """
    )

# 사용자 입력
st.sidebar.header("설정 패널")
name = st.sidebar.text_input("이름을 입력하세요:")
age = st.sidebar.slider("나이를 선택하세요:")

st.write(f"👋 안녕하세요, {name}님! 당신의 나이는 {age}세입니다.")

# 데이터 입력 및 시각화 예시
import pandas as pd
import numpy as np

st.write("### 간단한 데이터 프레임")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)
st.table(data)

# 플롯 예제
st.write("### 데이터 플롯")
st.line_chart(data)

# 버튼과 액션
if st.button("환영 메시지 표시"):
    st.success("🎉 Streamlit 앱에 오신 것을 환영합니다!")

# 푸터
st.write("---")
st.write("🔗 더 알아보기: [Streamlit 공식 문서](https://docs.streamlit.io/)")
