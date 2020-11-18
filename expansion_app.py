import streamlit as st
import math
from pathlib import Path
import base64

def setup(page):
    '''Main page for Streamlit Setup and Commandline'''

    st.title(page)
    col1, col2 = st.beta_columns(2)
    col1.markdown('__How to install and import__')

    col1.code('$ pip install streamlit')

    col1.markdown('Import convention')
    col1.code('>>> import streamlit as st')

    col1.markdown('__How to uninstall__')
    col1.code('''
pip uninstall streamlit
    ''')

    col1.markdown('__Command line__')
    col1.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
$ pip install streamlit-nightly --upgrade
    ''')
    return

def basic(page):
    '''Basic streamlit commands'''
    st.title(page)

    col1, col2 = st.beta_columns(2)
    # start with the basics

    # CREATING TEXT
    col1.header('Display text')
    col1.write('There are various ways to display text in Streamlit')

    col1.title('A title')
    col1.code("st.title('A title')")

    col1.header('A basic header')
    col1.code("st.header('A basic header')")

    col1.subheader('My subheader')
    col1.code("st.subheader('My subheader')")

    col1.text('Fixed width text command:')
    col1.code("st.text('Fixed width text command:')")

    col1.write('The write command, also works when passing most objects:')
    an_object = ['list', 3.14159,0]
    col1.code('''
        st.write('The write command, also works when passing most objects:')
        st.write(an_object) #this is a list
        ''')
    col1.write(an_object)

    col1.markdown('_Markdown_, __Markdown__:')
    col1.code("st.markdown('_Markdown_, __Markdown__')")

    col1.write('LaTeX equations:')
    col1.code("st.latex('e^{i\pi} + 1 = 0')")
    col1.latex('e^{i\pi} + 1 = 0')

    # SIDEBAR COMMANDS
    col1.subheader('Sidebar')
    col1.write('Add widgets to sidebar')
    col1.code('''
st.sidebar.<widget>
>>> a = st.sidebar.radio(\'R:\',[1,2])
    ''')

    # WIDGETS
    col2.header('Interactive Widgets')
    col2.write('There are many interactive widgets that you can use to allow the user \
        to interact with your app')

    col2.subheader('Button')
    a_button = col2.button('Hit me')

    col2.code('''
    a_button = st.button('Hit me')
    if a_button: # if it has been clicked
        st.write('TADA!')''')
    if a_button: # if it has been clicked
        col2.write('TADA!')

    col2.subheader('Checkbox')
    a_checkbox = col2.checkbox('Check me out')
    col2.code(''' 
    a_checkbox = st.checkbox('Check me out') 
    if a_checkbox: # if clicked
        st.write("Check me out I'm awesome!")''')

    if a_checkbox: # if clicked    
        col2.write("Check me out I'm awesome!")

    col2.subheader('Radio Buttons')
    col2.write('The options for a radio button can be a string, interger or float')
    radio_selection = col2.radio('Radio', ['Option 1',2,3.14159])
    col2.code(''' 
    radio_selection = col2.radio('Radio', ['Option 1',2,3.14159]) 
    if radio_selection == 'Option 1': 
        st.write("great choice")
    elif radio_selection == 2:
        st.write("thats a number")
    elif radio_selection == 3.14159:
        st.write(math.pi)''')
    if radio_selection == 'Option 1': 
        col2.write("great choice")
    elif radio_selection == 2:
        col2.write("thats a number")
    elif radio_selection == 3.14159:
        col2.write(math.pi)

    col2.code('''
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')
    ''')

    # PLOT COMMANDS

    return

def beta(page):
    '''Beta Streamlit commands'''
    st.title(page)
    return

def experimental(page):
    '''Experimemtal Streamlit commands'''
    st.title(page)
    return

def tutorial(page):
    '''Tutorial to learn how to run Streamlit commands'''
    st.title(page)
    return

# Run the program
if __name__ == '__main__':

    # Create a wide layout for the pages
    st.set_page_config(page_title='Streamlit cheat sheet',layout="wide")

    # Create a sidebar with all the page options for the expansion
    st.sidebar.markdown('Pick the page you wish to visit for a list of all the \
    possible functions and commands in Streamlit')
    page = st.sidebar.radio('Navigation', [
        'Setup and Commandline',
        'Basic Commands',
        'Beta Commands',
        'Experimental Commands',
        'Tutorial'])

    # in side bar add links to the documentation and version this is based on
    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v0.71.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    # run associated page program for each selection
    if page == 'Setup and Commandline':
        setup(page)
    elif page == 'Basic Commands':
        basic(page)
    elif page == 'Beta Commands':
        beta(page)
    elif page == 'Experimental Commands':
        experimental(page)
    elif page == 'Tutorial':
        tutorial(page)
