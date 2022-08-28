# import pandas as pd
# import numpy as np
import streamlit as st
import requests

st.markdown("<h1 style='text-align: center; color: red;'>Movie Dekho.com</h1>", unsafe_allow_html=True)
var=st.text_input("PLease enter the name of the movie")




if var:
    st.write("1 result found for __{}__".format(var))
    try:
      url=f"http://www.omdbapi.com/?t={var}&apikey=bacb3c59"  
      resp=requests.get(url)
      resp=resp.json()
      c1,c2=st.columns([3,5])
      with c1:
        st.image(resp['Poster'])
      with c2:
        st.subheader(resp['Title'])
        st.caption(f"Genre: {resp['Genre']}, Year: {resp['Year']}")
        st.write(resp['Plot'])
        st.text(f"Box Office: {resp['BoxOffice']}")
        st.text(f"Rating: {resp['imdbRating']}")
        st.progress(float(resp['imdbRating'])/10)  
    except:
        st.error("No movie with the tittle __'{}'__".format(var))

