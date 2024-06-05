import streamlit as st

st.set_page_config(
    page_title="Fine Tuning",
    page_icon="🏦",
    layout="wide"
    )
version = "03.06.24. Reranker FT"


import Priprema_podataka_za_FT as priprema
import Fine_Tuning_Turbo as ft

def main():
    if "izr" not in st.session_state:
        st.session_state["izr"] = False 

    if "prip" not in st.session_state:
        st.session_state["prip"] = False 

    st.markdown(f"<p style='font-size: 10px; color: grey;'>{version}</p>", unsafe_allow_html=True)
    st.subheader('Izaberite operaciju za Fine-Tuning')

    with st.expander("Pročitajte uputstvo:"):
        st.caption("""                  
•	Step 1: Prepare the Dataset \n
Collect Queries: Gather a set of diverse queries representative of your use case. \n
You can set CHATGPT with 4o model to generate questions from th etext for which you are fune-tuning the model, usually one or more namespaces used for this topic \n
Retrieve Documents: Use your current hybrid search system to retrieve documents for each query. \n
Label Relevance: Assign relevance scores to each query-document pair. (can be done manually or with a model) \n
•	Step 2: Format the Data \n
Create a JSONL file with query-document pairs and relevance scores. \n
•	Step 3: Fine-Tune GPT-3.5-turbo \n
Upload the Training Data \n
Fine-Tune the Model - Izradi FT model
""")

    colona1, colona2 = st.columns(2)

    with colona1:
        with st.form(key='priprema', clear_on_submit=False):
            priprema_button = st.form_submit_button(
                label='Pripremi ulazne dokumente', use_container_width=True, help = "Pripremi ulazne dokumente")
            if priprema_button:    
                st.session_state.prip=True
                st.session_state.izr=False
    with colona2:
        with st.form(key='izrada', clear_on_submit=False):
            izrada_button = st.form_submit_button(
                label='Izradi FT Model', use_container_width=True, help = "Izrada FT Modela")
            if izrada_button:
                st.session_state.izr=True
                st.session_state.prip=False
    col1, col2 = st.columns(2)

    ph1 = st.empty()
    if st.session_state.prip:
        with ph1.container():
            priprema.pripremaft()


    if st.session_state.izr:
        with ph1.container():
            ft.main()

if __name__ == "__main__":
    main()


