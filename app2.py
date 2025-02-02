import openai
import streamlit as st
import os

# Streamlit Cloud에서 환경 변수 가져오기

openai.api_key = st.secrets["API_KEY"]
# ✅ Streamlit UI 구성
st.title('🔍 블로그 내용 생성기')
st.subheader("💡 ChatGPT 기반으로 검색된 키워드입니다.")

st.write('📌 **판매하려는 제품 블로그작성!**')

# ✅ 사용자 입력 받기
title = st.text_input("🔎 이곳에 입력해주세요")

# ✅ 버튼 클릭 시 API 호출
if st.button('검색하기'):
    if title.strip():  # 빈 입력값 방지
        chat_completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "입력된 문구를 중심으로 사진과 함께 블로그 작성해줘"},
                {"role": "user", "content": title},  # ✅ 사용자 입력값 반영!
            ]
        )

        # ✅ 결과 출력
        result = chat_completion.choices[0].message.content
        st.write("### 🔑 추천 키워드")
        st.write(result)
    else:
        st.warning("🔴 제품 특징을 입력해주세요!")