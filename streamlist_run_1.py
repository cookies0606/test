import streamlit as st

st.title("기본 위젯 예시")

# 텍스트 입력
name = st.text_input("이름을 입력하세요:")
st.write("입력한 이름:", name)

# 숫자 슬라이더
age = st.slider("나이를 선택하세요:", 0, 100)
st.write("선택한 나이:", age)

# 버튼
if st.button("클릭하세요"):
    st.success("버튼이 클릭되었습니다!")

# 체크박스
agree = st.checkbox("동의합니다.")
if agree:
    st.write("감사합니다!")

# 셀렉트박스
color = st.selectbox("좋아하는 색을 선택하세요:", ["빨강", "초록", "파랑"])
st.write("선택한 색:", color)

import streamlit as st
from openai import OpenAI

st.title("GPT-4.1-mini 질문 응답기")

api_key = st.text_input("OpenAI API 키를 입력하세요", type="password")
query = st.text_area("GPT에게 물어볼 질문을 입력하세요:")

if st.button("질문 보내기"):
    if not api_key:
        st.error("API 키를 입력하세요.")
    elif not query.strip():
        st.warning("질문을 입력하세요.")
    else:
        client = OpenAI(api_key=api_key)
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # 또는 gpt-4.0-mini (API 지원 버전에 따라)
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ]
            )
            st.success("응답:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"에러 발생: {e}")
