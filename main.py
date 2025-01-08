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
        "https://i.namu.wiki/i/URqcrFqj4QZ9nSgO4XuzZsttV5S5PhXRL6ivu4ilUTc0u75Qm7wvfyHGfUBj-b3QrKxsGE8qlJ7GKpte7gCmhQ.webp", 
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
name = st.sidebar.text_input("이름을 입력하세요:","양서진")
age = st.sidebar.slider("나이를 선택하세요:",18)
산",
}

st.set_page_config(
    page_title="퀴즈 앱",
    page_icon="❓",
    layout="centered",
)

# 헤더
st.title("🧠 재미있는 퀴즈 풀기!")
st.write("아래 3가지 퀴즈를 풀고 정답을 확인해보세요.")

# 퀴즈 데이터
quizzes = [
    {
        "question": "다음 중 대한민국의 수도는 무엇일까요?",
        "options": ["서울", "도쿄", "베이징", "파리"],
        "answer": "서울",
    },
    {
        "question": "다음 중 지구에서 가장 가까운 행성은 무엇일까요?",
        "options": ["금성", "화성", "목성", "토성"],
        "answer": "금성",
    },
    {
        "question": "파이썬의 창시자는 누구일까요?",
        "options": ["귀도 반 로섬", "데니스 리치", "제임스 고슬링", "리누스 토르발스"],
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
