import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

from ner import nlp, SpacyDocument


def get_data_from_entities(entities):
    counts = {label: 0 for label in nlp.get_pipe("ner").labels}
    for entity in entities:
        # label is 3rd element of each entity tuple
        counts[entity[2]] += 1
    return pd.DataFrame(list(counts.values()), list(counts.keys()))


# work around, because it is hard to link static files in streamlit
# just load the contents of the CSS file and use that instead
@st.cache
def load_css(path):
    with open(path) as f:
        css = f.read()
    return css


css = load_css('./static/css/main.css')

st.title("Named Entity Recognition")
with st.form("box"):
    text = st.text_area('Text to analyze')
    submitted = st.form_submit_button("Submit")
    if submitted:
        doc = SpacyDocument(text)
        entities = doc.get_entities()
        st.info(entities)

        html = """
        <head>
            <style>
                {}
            </style>
        </head>
        <body>
            <div>
                {}
            </div>
        </body>
        """.format(css, doc.get_entities_with_markup())

        components.html(html, height=200)

        st.bar_chart(get_data_from_entities(entities))
