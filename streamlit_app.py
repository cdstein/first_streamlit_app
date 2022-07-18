import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.text(' 🍌🥭 Build Your Own Fruit Smoothie 🍌🥭')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Lets put a picklist here so the customer can pick the fruit they want to use
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc [fruits_selected]
#Display the table on the page
streamlit.dataframe(fruits_to_show)
#Fruit advice header
streamlit.header('Fruity Vice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json()) #Just writes the data to a screen
# Normalizes the data into discrete columns and rows by key value pairs
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Put's the normalized data into a web table
streamlit.dataframe(fruityvice_normalized)

