import openai
import streamlit as st
import os

# Streamlit Cloud에서 환경 변수 가져오기

openai.api_key = st.secrets["API_KEY"]
# ✅ Streamlit UI 구성
st.title('🔍 판매하려는 제품 키워드 추천')
st.subheader("💡 ChatGPT 기반으로 검색된 키워드입니다.")

st.write('📌 **판매하려는 제품의 특징을 입력해주세요!**')

# ✅ 사용자 입력 받기
title = st.text_input("🔎 이곳에 입력해주세요")

# ✅ 버튼 클릭 시 API 호출
if st.button('검색하기'):
    if title.strip():  # 빈 입력값 방지
        chat_completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "너는 온라인 판매 사업자야. 입력받은 문구를 판매할 때 어떤 키워드를 써야 판매가 잘될지 최소 20개 이상 추천해줘."},
                {"role": "user", "content": title},  # ✅ 사용자 입력값 반영!
            ]
        )

        # ✅ 결과 출력
        result = chat_completion.choices[0].message.content
        st.write("### 🔑 추천 키워드")
        st.write(result)
    else:
        st.warning("🔴 제품 특징을 입력해주세요!")
