import streamlit as st 
from googletrans import Translator
from languages import *

##initialize our streamlit app
st.set_page_config(page_title=" App 👨")
st.header("🎊 Language Translation App️ 🫰")
source_text = st.text_area("Enter text to translate:")
target_language = st.selectbox("Select target language:", languages)
translate = st.button('Translate')
if translate:
    translator = Translator()
    out = translator.translate(source_text,dest=target_language)
    st.write(out.text)

footer = """
---
#### Made By [Surat Banerjee](https://www.linkedin.com/in/surat-banerjee/)
For Any Queries, Reach out on [Portfolio](https://suratbanerjee.wixsite.com/myportfoliods)  
"""

st.markdown(footer, unsafe_allow_html=True)
                               







