import streamlit as st

st.title("Streamlit 기본 위젯 예제")

st.header("텍스트 입력")
name = st.text_input("이름을 입력하세요:")

st.header("숫자 입력")
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=120, step=1)

st.header("슬라이더")
rating = st.slider("만족도", 0, 10, 5)

st.header("버튼")
if st.button("제출"):
    st.write(f"{name}님, 나이는 {age}살이고 만족도는 {rating}점입니다.")

st.header("체크박스")
if st.checkbox("추가 옵션 보기"):
    st.write("체크박스가 선택되었습니다!")

st.header("라디오 버튼")
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write(f"선택한 성별: {gender}")

st.header("셀렉트박스")
language = st.selectbox("좋아하는 언어는?", ["Python", "Java", "C++"])
st.write(f"좋아하는 언어: {language}")

import streamlit as st
import openai

st.title("GPT-4 응답 웹앱")

# API Key 입력 받기
api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")

# 질문 입력 받기
user_question = st.text_area("질문을 입력하세요")

# 모델 선택 (gpt-3.5, gpt-4 등)
model = st.selectbox("모델 선택", ["gpt-3.5-turbo", "gpt-4"])

if st.button("질문 보내기"):
    if not api_key:
        st.warning("API Key를 입력하세요.")
    elif not user_question.strip():
        st.warning("질문을 입력하세요.")
    else:
        try:
            openai.api_key = api_key

            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "당신은 유용한 AI 비서입니다."},
                    {"role": "user", "content": user_question}
                ]
            )

            answer = response.choices[0].message.content
            st.success("답변:")
            st.write(answer)

        except Exception as e:
            st.error(f"에러 발생: {str(e)}")
