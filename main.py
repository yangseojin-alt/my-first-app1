import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="다기능 앱",
    page_icon="🌟",
    layout="wide",
)

# 사이드바 메뉴
st.sidebar.title("🌟 메뉴")
page = st.sidebar.selectbox("페이지를 선택하세요:", ["기본 앱", "퀴즈 풀기"])

# 기본 앱 페이지
if page == "기본 앱":
    # 헤더
    st.title("🌟 나의 첫 번째 Streamlit 앱 🌟")
    st.subheader("Streamlit를 사용해 웹 앱을 쉽게 만들어보세요!")

    # 컬럼 레이아웃
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://www.google.com/url?sa=i&url=https%3A%2F%2Fnamu.wiki%2Fw%2F%25EB%25B6%2584%25EB%258B%25B9%25EB%258C%2580%25EC%25A7%2584%25EA%25B3%25A0%25EB%2593%25B1%25ED%2595%2599%25EA%25B5%2590&psig=AOvVaw1Z6ofmjL1CkBZs6qUwZrnc&ust=1736391820530000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKC3zdKR5YoDFQAAAAAdAAAAABAE", 
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
    name = st.sidebar.text_input("이름을 입력하세요:", "양서진")
    age = st.sidebar.slider("나이를 선택하세요:", 18)

    st.write(f"👋 안녕하세요, {name}입니다! 저의 나이는 {age}세입니다.")

    # 데이터 입력 및 시각화 예시
    st.write("### 간단한 데이터 프레임")
    data = pd.DataFrame(
        np.random.randn(100, 3),
        columns=["A", "B", "C"]
    )
    st.table(data)

    # 플롯 예제
    st.write("### 데이터 플롯")
    st.line_chart(data)

    # 버튼과 액션
    if st.button("환영 메시지 표시"):
        st.success("🎉 Streamlit 앱에 오신 것을 환영합니다!")

# 퀴즈 풀기 페이지
elif page == "퀴즈 풀기":
    # 헤더
    st.title("🧠 재미있는 퀴즈 풀기!")
    st.write("아래 3가지 퀴즈를 풀고 정답을 확인해보세요.")

    # 퀴즈 데이터
    quizzes = [
        {
            "question": "다음 중 대한민국의 수도는 무엇일까요?",
            "options": ["도쿄", "서울", "베이징", "파리"],
            "answer": "서울",
        },
        {
            "question": "다음 중 지구에서 가장 가까운 행성은 무엇일까요?",
            "options": ["금성", "화성", "목성", "토성"],
            "answer": "금성",
        },
        {
            "question": "파이썬의 창시자는 누구일까요?",
            "options": [ "데니스 리치", "제임스 고슬링", "귀도 반 로섬", "리누스 토르발스"],
            "answer": "귀도 반 로섬",
        },
    ]


    # 퀴즈 실행
    for i, quiz in enumerate(quizzes):
        st.write(f"### 문제 {i+1}: {quiz['question']}")
        user_answer = st.radio(
            f"문제 {i+1} 정답을 선택하세요:",
            quiz["options"],
            key=f"quiz_{i}",
        )

        # 정답 확인 버튼
        if st.button(f"문제 {i+1} 정답 확인", key=f"check_{i}"):
            if user_answer == quiz["answer"]:
                st.success(f"🎉 정답입니다! {quiz['answer']}이 맞습니다.")
            else:
                st.error(f"❌ 틀렸습니다. 정답은 {quiz['answer']}입니다.")

    # 퀴즈 완료 메시지
    st.write("---")
    st.write("🔗 더 알아보기: [Streamlit 공식 문서](https://docs.streamlit.io/)")
