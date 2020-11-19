import streamlit as st
from streamlit_ace import st_ace
#from execbox import execbox
import math
import pandas as pd
import numpy as np
from pathlib import Path
import base64

def create_space(): 
    st.write('')
    st.write('')
    st.write('')

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

    # DISPLAY CODE
    with col1: 
        st.subheader("Display Code")
        st.text('You can display code using st.code:')
        st.code(''' 
st.code('st.write("a line of code")')
st.code( ' ' '  # use triple quotes to create a block (no spaces)
st.write("A block of code")
code_button = st.button('Click Me')
if code_button: 
    success!
' ' ')
        ''')
        st.text('this output looks like:')
        st.code('st.write("a line of code")')
        st.code( '''  # use triple quotes to create a block (no spaces)
        st.write("A block of code")
        code_button = st.button('Click Me')
        if code_button: 
            st.text('success!')
        ''')

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
    col2.write('The options for a radio button can be a string, integer, float, or variable')
    variable = 12
    radio_selection = col2.radio('Radio', ['Option 1',variable,3.14159])
    col2.code(''' 
variable = 12
radio_selection = col2.radio('Radio', ['Option 1',variable,3.14159]) 
if radio_selection == 'Option 1': 
    st.write("great choice")
elif radio_selection == variable:
    st.write("thats a number from a variable")
elif radio_selection == 3.14159:
    st.write(math.pi)''')
    if radio_selection == 'Option 1': 
        col2.write("great choice")
    elif radio_selection == variable:
        col2.write("thats a number from a variable")
    elif radio_selection == 3.14159:
        col2.write(math.pi)

    col2.subheader('Selectbox')
    col2.write('Select 1 option from a variety')
    single_select = col2.selectbox('Single Select', ['what', 'will', 'you', 'choose?'])

    col2.code(''' 
single_select = st.selectbox('Single Select', 
    ['what', 'will', 'you', 'choose?'])
    
if (single_select == 'what') or (single_select == 'you'): 
    st.write('You win! :smiley:')
else: 
    st.write('Winner Winner :chicken: Dinner!)''')
    if (single_select == 'what') or (single_select == 'you'): 
        col2.write('You win! :smiley:')
    else: 
        col2.write('Winner Winner :chicken: Dinner!')

    col2.subheader('Multi-Select Box')
    col2.write('Select 1 or more options from a variety')
    multi_select = col2.multiselect('Multi-Select', ['what', 'will', 'you', 'choose?'])
    col2.code('''
multi_select = st.multiselect('Multi-Select', 
    ['what', 'will', 'you', 'choose?'])
st.write(multi_select)''')
    col2.write(multi_select)

    col2.subheader('Sliders')
    col2.markdown('__Single Slider__')
    slider_value = col2.slider('Slide me', min_value=0, max_value=10, value=5)
    
    col2.code('''
slider_value = st.slider('Slide me',  min_value=0, max_value=10, value=5)
st.write(slider_value)''')
    col2.write(slider_value)

    col2.markdown('__Double Ended Slider__')
    double_slider = col2.slider('A range', 0,100, (10,90))
    col2.code('''
double_slider = col2.slider('A range', 0,100, (10,90))
st.write(double_slider)''')
    col2.write(double_slider)

    col2.markdown('__Fixed Option Slider__')
    s_slider = col2.select_slider('Slide to select', options=[1,'Middle', variable], value = 'Middle')
    col2.code('''
s_slider = st.select_slider('Slide to select', 
    options=[1,'Middle', variable],value = 'Middle')
st.write(s_slider)''')
    col2.write(s_slider)

    with col2: 
        st.subheader('Various Input fields')
        st.markdown('__Text Input__')
        st.code('''
title_limited = "Enter some text: limit to number of characters"
text_limited = col2.text_input(title_limited, 'display text')
st.write(text_limited)
        
title_unlim = "Area for textual entry: no limit to number of characters"
text_unlim = col2.text_area(title_unlim, "Text to Display")
st.write(text_unlim) ''')

        title_limited = "Enter some text: limit to number of characters"
        text_limited = col2.text_input(title_limited, 'display text')
        st.write(text_limited)

        title_unlim = "Area for textual entry: no limit to number of characters"
        text_unlim = col2.text_area(title_unlim, "Text to Display")
        st.write(text_unlim)
    
        st.markdown('__Number Input__')
        st.code(''' 
a_number = st.number_input('Enter a number')
st.write(a_number)''')
        a_number = st.number_input('Enter a number')
        st.write(a_number)

        st.markdown('__Date Input__')
        st.write("The date input is automatically the datetime class, default is the current date")
        st.code('''
a_date = st.date_input('Date input')
st.write(a_date)
st.write(type(a_date)) ''')
        a_date = st.date_input('Date input')
        st.write(a_date)
        st.write(type(a_date))

        st.markdown('__Time Input__')
        st.write("The time input is automatically the datetime class, default is the current time")
        st.code('''
a_time = st.time_input('Time entry')
st.write(a_time)
st.write(type(a_time))''')
        a_time = st.time_input('Time entry')
        st.write(a_time)
        st.write(type(a_time))

        st.subheader('Odds & Ends')
        st.markdown("__Upload a file__")
        st.code(''' 
upload_file = st.file_uploader('File uploader')
        ''')
        upload_file = st.file_uploader('File uploader')

        st.markdown("__Colour Select__")
        st.code(''' 
color = st.color_picker('Pick a color')
st.write(color)''')
        color = st.color_picker('Pick a color')
        st.write(color)
    

    # PLOT COMMANDS -> maybe they have their own section

    return

def beta(page):
    '''Beta Streamlit commands'''
    st.title(page)
    st.write('''This pages lists the Beta commands that are available in Streamlit. They are not yet integrated 
    into the basic Streamlit functions and therefore may not always work in unique (edge) cases. If you believe you have 
    encountered such a case please let us know on the [Streamlit Community Platform](https://discuss.streamlit.io/)''')
    
    st.subheader('Columns of Equal Size')
    st.code('''
    col1,col2 = st.beta_columns(2)
    col1.image('brain.png', caption= "This ia a blue brain!")
    data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['a', 'b', 'c'])
    col2.write(data)''')
    
    col1,col2 = st.beta_columns(2)
    col1.image('img/brain.png', caption= "This ia a blue brain!")
    data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ['a', 'b', 'c'])
    col2.subheader('A Dataframe')
    col2.write(data)

    st.subheader('Columns of Different Sizes')
    st.code('''
    col3,col4,col5 = st.beta_columns([1,2,3]) 
    # 3 columns where first is the smallest, the second is 2x the size of the first and 3rd is 3x the first
    col3.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
    with col4: 
        st.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
    with col5: 
        st.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
    ''')
    col3,col4,col5 = st.beta_columns([1,2,3]) 
    # 3 columns where first is the smallest, the second is 2x the size of the first and 3rd is 3x the first
    col3.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
    with col4: 
        st.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")
    with col5: 
        st.image('img/MC.png',use_column_width = True, caption="A Streamlit Sharing App")

    st.subheader('Columns to Make a Grid')
    st.code('''
    for i in range(1,3): # number of rows in your table! = 2
        cols = st.beta_columns(2) # number of columns in each row! = 2
        # first colum if the ith row
        cols[0].image('img/row_%i_col_0.png' %i, use_column_width=True)
        cols[1].image('img/row_%i_col_1.jpg' %i, use_column_width=True)
    ''')
    for i in range(1,3): # number of rows in your table! = 2
        cols = st.beta_columns(2) # number of columns in each row! = 2
        # first colum if the ith row
        cols[0].image('img/row_%i_col_0.png' %i, use_column_width=True)
        cols[1].image('img/row_%i_col_1.jpg' %i, use_column_width=True)

    st.subheader('Containers')
    st.write('''you may want to create a container to _________. A cool feature of containers, 
    it that it allows you to place things 'out of order'. ''')
    with st.beta_container():
        st.write("This bar graph is inside the container")
        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))
    
    st.write("This is outside the container")

    return

def experimental(page):
    '''Experimemtal Streamlit commands'''
    st.title(page)
    return

def tutorial(page):
    '''Tutorial to learn how to run Streamlit commands'''
    st.title(page)
    st.write("Now you can have a chance to try yourself! Combine things together and see what you get!")

    trial_code = st_ace('st.balloons()', font_size=15) 
    # need to save the work of people who input stuff 
    # checkbox to save work? 
    # button to put it back to start 
    exec(trial_code)
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
