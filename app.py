import streamlit as st
from model import Evaluate

evaluator = Evaluate()

st.title("Bible Verse Search")
st.markdown('built by [@shreydan](https://github.com/shreydan)')
st.markdown("### Praise the Lord.")
st.markdown("##### Please type the text you recall from the verse to get references.")


with st.form(key='text_form'):

    text_input:str = st.text_input(label='type verse...',key='input')
    text_input = text_input.strip()

    st.caption('Examples: do not be afraid, bless the Lord oh my soul')

    num_responses = st.slider(
        label='number of responses',
        min_value=5,
        max_value=30,
        step=5,
        value=10
    )
    num_responses = int(num_responses)
    submitted = st.form_submit_button("Search")


if submitted and len(text_input) != 0:
    response = evaluator.get_verses(text_input,top=num_responses)
    references = response['reference']
    verses = response['verse']

    st.markdown('#### here are the verses...\n___')

    for ver, ref in zip(verses,references):
        with st.container():
            md = f"""
            ##### {ver}
            {ref}
            ___
            """
            st.markdown(md)

