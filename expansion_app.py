import streamlit as st
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

    # Creating Text
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
    col1.code('''
        st.write('The write command, also works when passing most objects:')
        st.write(an_object) # df, err, func, keras!''')

    col1.markdown('_Markdown_, __Markdown__:')
    col1.code("st.markdown('_Markdown_, __Markdown__')")

    col1.write('LaTeX equations:')
    col1.code("st.latex('e^{i\pi} + 1 = 0')")
    col1.latex('e^{i\pi} + 1 = 0')
    col1.code('''
    st.write(['st', 'is <', 3]) # see *

    
    
    st.code('for i in range(8): foo()')
    * optional kwarg unsafe_allow_html = True
        ''')

    # SIDEBAR COMMANDS
    col1.subheader('Sidebar')
    col1.write('Add widgets to sidebar')
    col1.code('''
st.sidebar.<widget>
>>> a = st.sidebar.radio(\'R:\',[1,2])
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
        'Basic',
        'Beta',
        'Experimental',
        'Tutorial'])

    # in side bar add links to the documentation and version this is based on
    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v0.71.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    # run associated page program for each selection
    if page == 'Setup and Commandline':
        setup(page)
    elif page == 'Basic':
        basic(page)
    elif page == 'Beta':
        beta(page)
    elif page == 'Experimental':
        experimental(page)
    elif page == 'Tutorial':
        tutorial(page)
