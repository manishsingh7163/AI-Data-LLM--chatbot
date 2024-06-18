import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Saathi | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

#     st.write("**GitHub:**",
# "[yvann-hub/Saathi-chatbot](https://github.com/yvann-hub/Saathi-chatbot)")

#     st.write("**Medium:** "
# "[@yvann-hub](https://medium.com/@yvann-hub)")

    # st.write("**Twitter:** [@yvann_hub](https://twitter.com/yvann_hub)")
    # st.write("**Mail** : barbot.yvann@gmail.com")
     st.write("**Created by Saathi**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Saathi AI, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm Saathi AI, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV, Youtube transcript 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Saathi's Pages
st.subheader("🚀 Saathi's Pages")
st.write("""
- **Saathi-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Saathi-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
- **Saathi-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**Saathi is under regular development. Feel free to contribute and help me make it even more data-aware!**
""", unsafe_allow_html=True)





