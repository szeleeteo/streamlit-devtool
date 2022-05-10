import warnings

import spacy
import streamlit as st
from spacy import displacy
from streamlit.components.v1 import html as st_html

warnings.filterwarnings("ignore", category=UserWarning)

ALL_KEYWORDS = [
    "revenue",
    "earning",
    "customer",
    "user",
    "subscriber",
    "sale",
    "income",
    "download",
    "install",
    "profit",
]

st.header("NLP Demo")
default_text = (
    "Apple today announced financial results for its fiscal 2022 second "
    "quarter ended March 26, 2022. The company posted a March quarter "
    "revenue record of $97.3 billion, up 9 percent year over year, and "
    "quarterly earnings per diluted share of $1.52."
)

input_text = st.text_area("Input text", value=default_text)

models = [
    "en_core_web_sm",  # lighter, faster, less accurate
    "en_core_web_trf",  # heavier, slower, more accurate
]
model = st.sidebar.selectbox("Model", models)
nlp = spacy.load(model)

# NER = Named-entity recognition
ALL_NER_TYPES = list(nlp.get_pipe("ner").labels)


def predict_with_awesome_ml_model(
    contents, ner_types=None, keywords=None, style="ent", merge_nouns=False
):
    if isinstance(contents, str):
        contents = [contents]

    displacy_options = {}
    displacy_options["ents"] = ner_types or []

    if "merge_noun_chunks" in nlp.pipe_names:
        nlp.remove_pipe("merge_noun_chunks")
    if "entity_ruler" in nlp.pipe_names:
        nlp.remove_pipe("entity_ruler")

    if style == "dep" and merge_nouns:
        nlp.add_pipe("merge_noun_chunks")

    if keywords:
        growth_ent = "GROWTH"
        ruler = nlp.add_pipe("entity_ruler")
        patterns = [
            {"label": growth_ent, "pattern": [{"LEMMA": kw}]} for kw in keywords
        ]
        ruler.add_patterns(patterns)

        color = "linear-gradient(45deg, yellow, red)"
        displacy_options["colors"] = {growth_ent: color}
        displacy_options["ents"].append(growth_ent)

    for content in contents:
        doc = nlp(content)
        html = displacy.render(doc, style=style, options=displacy_options)
        st.write(html, unsafe_allow_html=True)


with st.sidebar:
    growth_keywords = st.multiselect(
        "Keywords", ALL_KEYWORDS, ["revenue", "earning", "customer"]
    )
    quantifiable_types = st.multiselect(
        "Keywords",
        ALL_NER_TYPES,
        ["ORG", "CARDINAL", "ORDINAL", "PERCENT", "QUANTITY", "MONEY"],
    )
    show_dependency_parsing = st.checkbox("Enable dependency parsing")

    merge_nouns = False
    if show_dependency_parsing:
        merge_nouns = st.checkbox("Merge nouns")


match_res = predict_with_awesome_ml_model(
    input_text, keywords=growth_keywords, ner_types=quantifiable_types
)
st_html(match_res, height=200, scrolling=True)

if show_dependency_parsing:
    dep_res = predict_with_awesome_ml_model(
        input_text,
        keywords=growth_keywords,
        ner_types=quantifiable_types,
        style="dep",
        merge_nouns=merge_nouns,
    )
    st_html(dep_res, height=200, scrolling=True)
