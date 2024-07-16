import os
import importlib
import sys
import pandas as pd
import streamlit as st
from io import BytesIO
from modules.robby_sheet.table_tool import PandasAgent
from modules.layout import Layout
from modules.utils import Utilities
from modules.sidebar import Sidebar

def reload_module(module_name):
    """For update changes
    made to modules in localhost (press r)"""

    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    return sys.modules[module_name]

table_tool_module = reload_module('modules.saathi_sheet.table_tool')
layout_module = reload_module('modules.layout')
utils_module = reload_module('modules.utils')
sidebar_module = reload_module('modules.sidebar')


st.set_page_config(layout="wide", page_icon="💬", page_title="Saathi | Chat-Bot 🤖")

layout, sidebar, utils = Layout(), Sidebar(), Utilities()
st.markdown(
    f"""
    <h1 style='text-align: center;'> Ask Saathi about your CSV, Excel files !  😁</h1>
    """,
    unsafe_allow_html=True,
)
# layout.show_header("CSV, Excel")

user_api_key = utils.load_api_key()
os.environ["OPENAI_API_KEY"] = user_api_key


if not user_api_key:
    layout.show_api_key_missing()

else:
    st.session_state.setdefault("reset_chat", False)

    # uploaded_file = utils.handle_upload(["csv", "xlsx"])

    ####
    uploaded_file = st.sidebar.file_uploader("Upload your CSV files", type=["csv", "xlsx"], accept_multiple_files=True)


    if uploaded_file:
        ####
        file_options = [file.name for file in uploaded_file]
        selected_file_name = st.sidebar.selectbox("Select a file", file_options)
        
        selected_file = next(file for file in uploaded_file if file.name == selected_file_name)

        sidebar.about()
        
        uploaded_file_content = BytesIO(selected_file.getvalue())
        if selected_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or selected_file.type == "application/vnd.ms-excel":
            df = pd.read_excel(uploaded_file_content)
        else:
            df = pd.read_csv(uploaded_file_content)

        st.session_state.df = df

        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []
        csv_agent = PandasAgent()

        with st.form(key="query"):

            query = st.text_input("Write your Query here?", value="", type="default", 
                placeholder="e-g : How many rows ? "
                )
            submitted_query = st.form_submit_button("Submit")
            reset_chat_button = st.form_submit_button("Reset Chat")
            if reset_chat_button:
                st.session_state["chat_history"] = []
        if submitted_query:
            result, captured_output = csv_agent.get_agent_response(df, query)
            # print("resutl", result, "\ncaptured Output", captured_output)
            cleaned_thoughts = csv_agent.process_agent_thoughts(captured_output)
            csv_agent.display_agent_thoughts(cleaned_thoughts)
            csv_agent.update_chat_history(query, result)
            csv_agent.display_chat_history()
        if st.session_state.df is not None:
            st.subheader("10 Rows of dataframe:")
            st.write(st.session_state.df.head(10))

