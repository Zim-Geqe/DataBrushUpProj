import  os

import openpyxl

import streamlit as st

import pandas as pd
import numpy as np
from st_aggrid import AgGrid

from datetime import datetime

import streamlit.components.v1 as components

import altair as alt

#Linkedin KPI's indicator dashboad using streamlit






def main_page():
    """
    This function defines the landing page of the app
    """


    col1, mid, col2 = st.columns([1,2,20])
    with col1:
        st.image(os.path.abspath("linkedinLogo.png"), #header of the page 
            width=100)
    with col2:
        st.write("# LinkedIn Engagement")

    # sidebar
    
    st.sidebar.markdown("# LinkedIn Engagement")

    st.sidebar.markdown("**Created by Ndumiso Zimele Gumede [13/12/2022]**")

    st.sidebar.markdown("##")

    st.sidebar.markdown("**Start** by uploading your data on the next page.")

    st.sidebar.markdown("The process for obtaining your data can be found on the **Data Directions page**.")

    # subheader

    st.subheader("How engaging are your posts?")

    # welcome photo

    st.image(os.path.abspath("welcomePhoto.png"))

    st.markdown("**Track your post performance** over time by analyzing engagements, impressions, and the percent engagement per impression.")
    st.markdown("**Click** on any data point and **you're brought to that post's link!**")


def page2():
    col1, mid, col2 = st.columns([1,2,20])
    with col1:
        st.image(os.path.abspath("linkedinLogo.png"),
            width=100)
    with col2:
        st.write("# LinkedIn Engagement")

    # sidebar

    # load data

    # code for upload online
    # loading the the .xlsx file(Engangements file)
    file1 = st.sidebar.file_uploader("Upload Engagements & Impressions File",
        type=["xlsx"],
        help = "This is the file that has a name of the form **{Year}_{Your Name}.xlsx**. You can download this by following the directions on the Data Directions page."
    )


    if file1 is not None:

	    # To See details of the uploaded file

        file1_details = {"filename":file1.name, "filetype":file1.type,
                        "filesize":file1.size}
    try:

        #if reading xslx as a DataFrame suceeds the Date variable is converted to type rather than as it was loaded
        df = pd.read_excel(file1)

        df["Date"] = pd.to_datetime(df["Date"],infer_datetime_format = True).dt.date

    except:

        df = pd.DataFrame()
    #loading the .csv file (Impressions file)
    # load data

    file2 = st.sidebar.file_uploader("Upload Shares File",
        type=["csv"],
        help = "This is the Shares.csv file that you can obtain by following the directions on the Data Directions page."
    )


    if file2 is not None:

	    # To See details

        file2_details = {"filename":file2.name, "filetype":file2.type,
                        "filesize":file2.size}
	    #st.write(file1_details)

    try:

        df2 = pd.read_csv(file2)


    except:

        df2 = pd.DataFrame()

    #Prepairing data  by defining 
    


        


def page3():
    pass


def page4():
    pass



# create site

page_names_to_funcs = {
    "LinkedIn Engagement": main_page,
    "Your Dashboard": page2,
    "Data Directions": page3,
    "Number of followers": page4 
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())#select  box is used to create a drop down area betwwen pages
page_names_to_funcs[selected_page]()





