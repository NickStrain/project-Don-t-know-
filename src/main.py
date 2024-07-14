import streamlit as st
from model import pre
'''
for streamlit deployment :||
'''

def main():
    st.title("Hate Text classification Module")

    with st.form(key='submit_form'):
        src = st.text_input(label='Enter the text:')
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
       
        model = pre() 
        out = model.pred(src)
        st.success(f"Submitted Data: {out}")
        

if __name__ == '__main__':
    main()