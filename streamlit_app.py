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
# Lets put a picklist here so the customer can pick the fruit they want to use
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#Display the table on the page
streamlit.dataframe(my_fruit_list)
