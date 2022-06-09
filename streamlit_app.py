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
#streamlit.dataframe(my_fruit_list)

#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#lets put a pick list here so they can pick the fruits they want to include
#streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))

#lets put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


#display the table on the page
#streamlit.dataframe(my_fruit_list) 
streamlit.dataframe(fruits_to_show) 



