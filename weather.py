# A mini weather forecast project that tells the weather for the place which is given by user as input
# used  api.weatherstack for free 250 api calls for one month
# using get request passing the API key and city name and fetching the data

# theme color code for streamlit [theme]
# primaryColor="#606060"
# backgroundColor="#060323"
# secondaryBackgroundColor="#3b3569"
# textColor="#f9f9f9"
# font="monospace"


import requests
import datetime
import streamlit as st
import time 

st.set_page_config(
    page_title = "Weather Forecast App",
    layout='wide')

st.title("Weather Forecast using python ☁️🌪")

col1 ,col2 = st.columns(2)
 
with col1:
    query_val = st.text_input('Enter the city name ', 'New Delhi')


weaather_dict = {'Sunny' : "",
                 'Partly cloudy' :""
                 }
icons = {
    'day' : '⛅️',
    'not_day' : '🌙'
}
def Weather(query_val):
    try:
        data = {"access_key": "d4bec76b5a544df531113ec42e05507c",
                "query": query_val}
        # keys of dict params- access_key and query are constant and cannot be changed
        req = requests.get('http://api.weatherstack.com/current', params=data)
        page_response = req.json()
        print(page_response)
        st.caption(r'Weather forecast at {} currently '.format(query_val))
        with st.container():
            if page_response['current']['is_day'] == 'yes':
                it_is_day= True
            else:
                it_is_day= False
            st.write("")
            st.write("")
            icon = icons['day'] if it_is_day else icons['not_day']
            st.subheader(" 📍{},{} {}".format(page_response['location']['name'], page_response['location']['country'],icon))
            st.write("")
            metric1, metric2, metric3 = st.columns(3)
            metric1.metric("Temperature", "{}°F".format(page_response['current']['temperature']))
            metric2.metric("Wind", "{}mph".format(page_response['current']['wind_speed']))
            metric3.metric("Humidity", "{}%".format(page_response['current']['humidity']))
            st.write("")
            info_col1 ,info_col2 = st.columns(2)
            with info_col1:
                st.info("Local Time & Date at  {} is {} / {}".format(query_val,page_response['location']['localtime'][11:16] ,page_response['location']['localtime'][0:10]))
                st.info("Currently at {} it is {} ".format(query_val,page_response['current']['weather_descriptions'][0]))
            with info_col2:
                st.info("Latitude ⇀ {}".format(page_response['location']['lat']))
                st.info("Longitude ⇀ {}".format(page_response['location']['lon']))
    except KeyError :
        st.warning("Please provide a valid input !!!")
        time.sleep(2.0)
        st.text(r" Example input can be :  New Delhi / Chennai / Bangalore / New Jersey / Toronto ")
        st.caption("Error received from API : {} ".format(page_response['error']['info']))
        print("The user provided an invalid city name ")


Weather(query_val)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

st.divider()
st.subheader("Let's Connect !!!")
st.write("")
st.write("")
st.write("")
footer_col1 , footer_col2 = st.columns(2)
with footer_col1:
    st.markdown("LinkedIn -  [Hari Ram S]('https://www.linkedin.com/in/hari-ram-s-342a7621b/')")
    st.markdown("Github - [SNIPOFIST](https://github.com/SNIPOFIST) ") 
    st.markdown("Instagram -  [hari____7]('https://www.instagram.com/hari____7/')")
    st.markdown("Mail -  [HariramSelvaraj@yahoo.com](mailto:HariramSelvaraj@yahoo.com)")

with footer_col2:
    st.caption("Give a visit to my other streamlit projects")
    st.markdown("Stock Prize Analyser - [https://stocksinfo.streamlit.app/](https://stocksinfo.streamlit.app/)")
st.divider()

st.caption("source code repo")
st.code('''https://github.com/SNIPOFIST/weather_forecast''')
