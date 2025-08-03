from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain import LLMChain
import streamlit as st

load_dotenv()

st.title("Chapter 6 【提出課題】LLM機能を搭載したWebアプリを開発しよう")

stress_template = """
あなたは親の育児ストレスを軽減するための専門家です。
育児疲れやストレス管理に関する実践的なアドバイスを提供します。
親自身の心身の健康を保つための方法を教えます。

質問：{input}
"""

nutrition_template = """
あなたは子どもの栄養に詳しいアドバイザーです。
子どもの健康な発育を支える食事や栄養バランスについてアドバイスを提供します。
食事の習慣や偏食に関する質問にも丁寧に答えます。

質問：{input}
"""

prompt_infos = [
    {
        "name": "stress",
        "description": "育児疲れやストレス管理に関するアドバイス",
        "prompt_template": stress_template,
    },
    {
        "name": "nutrition",
        "description": "子どもの栄養や食事の習慣に関するアドバイス",
        "prompt_template": nutrition_template,
    }
]

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.5,
    streaming=True,
    )

destination_chains = {}
for prompt_info in prompt_infos:
    name = prompt_info["name"]
    prompt_template = prompt_info["prompt_template"]
    prompt = PromptTemplate(input_variables=["input"], template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain


default_prompt = PromptTemplate(input_variables=["input"], template="{input}")
default_chain = LLMChain(llm=llm, prompt=default_prompt)

destinations = []
for p in prompt_infos:
    destinations.append(f"{p['name']}: {p['description']}")



selected_item = st.radio(

    "専門家を選択してください。",

    ["栄養アドバイザー", "育児アドバイザー"]

)

input_message = st.text_input(label="テキストを入力してください。")


if st.button("実行"):
    if not input_message:
        st.error("テキストを入力してください。")
    else:
        with st.spinner("生成中です..."):
            if selected_item == "栄養アドバイザー":
                chain = destination_chains["nutrition"]
                response = chain.run(input=input_message)
                st.write(response)

            elif selected_item == "育児アドバイザー":
                chain = destination_chains["stress"]
                response = chain.run(input=input_message)
                st.write(response)

            else:
                st.error("専門家を選択してください。")

