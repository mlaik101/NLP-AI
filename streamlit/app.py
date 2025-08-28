import streamlit as st
import pandas as pd
import numpy as np


## title of the application 
st.title("hello streamlit app ")


## display atext 
st.write("this is simole txt")



# create a data frame
df=pd.DataFrame(
    {
        'first column':[1,2,3,4,5],
        'second column':[10,20,30,40,50]
    }
)

#display the data frame 
st.write("this is the ddatafram")
st.write(df)



# create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']

)
st.line_chart(chart_data)