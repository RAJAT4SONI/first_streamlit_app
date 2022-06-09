import streamlit

streamlit.title("My Parents New Healthy Diner")

streamlit.header('Breakfast Menu')
streamlit.text('🍳omega 3 & blueberry Oatmeal')
streamlit.text('🥗kale, Spinach & Rocket Smoothie')
streamlit.text('🥚🥯Hard- Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🍓Build your own fruit smoothie🥝🍇🥤🍹')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
