# Importing necessary libraries
import streamlit as st 

# Page's main condiguration
st.set_page_config(page_title='Poetry Practice', page_icon='🌹')
# Title
st.title('🌹 Using Poetry for the first time')

# Poem
st.markdown('''
            Roses are red
            
            The sky is blue
            
            Pip had me stressed
            
            But poetry came true
            ''')

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
