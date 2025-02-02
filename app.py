from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

import streamlit as st



st.title('🔍판매하려는 제품 키워드 추천')
st.subheader("chatgpt 기반으로 검색된것입니다.", divider="rainbow")

st.write('📌 **판매하려는 제품의 특징을 입력해주세요!**')

title = st.text_input("🔎이곳에 입력해주세요")

if st.button('검색하기'):
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": title
                },
                {
                    "role": "system",
                    "content": "너는 온라인판매를 하려는 사업자인데 입력받은 문구를 판매하려할때 어떤 키워드를 써야 판매가 잘될지 최소 20개이상 추천해줘",
                }
            ],
            model="gpt-4o",
    )

    result = chat_completion.choices[0].message.content
    st.write(result)
