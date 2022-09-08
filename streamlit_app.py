import streamlit
import pandas
streamlit.title('Demo')
streamlit.header('Brakfast menu')
streamlit.text('Omega')
streamlit.text('Kale')
streamlit.text('Hard')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index('Fruit')))
streamlit.dataframe(my_fruit_list)
