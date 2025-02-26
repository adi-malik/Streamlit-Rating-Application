import google.generativeai as genai
import random
import streamlit as st
import pandas as pd
from datetime import datetime
API_KEY = "AIzaSyA3dtltaMUmIBM4_oGu2jIcRcbvJJENXog"

genai.configure(api_key=API_KEY)

def generate_text(prompt):
     model = genai.GenerativeModel("gemini-1.5-flash")
     response = model.generate_content(prompt)
     return response.text

def main():
    st.title("Streamlit rating app")

    st.write("This is a basic Streamlit app.")
    st.write("Please fill out the form to generate your rating!")

    name = st.text_input ("Enter your name!:")
    if name:
        valid_name = all(c.isalpha() or c.isspace() for c in name)
        if valid_name:
            ai_response = generate_text(f"what do you think about the name {name} you have to answer in maximum 25 words.")
            st.write(ai_response)
        else:
             st.write("Invalid input, Please enter a valid name!")
       
        if "a" in name:
                 st.write(f"""The name ({name}) represents the most (IQ) human can possibly have . If someone's name is {name} they are most likely smart . Proceed with the app to see your total ratings!""")
        if "a" not in name:
                st.write(f"You chose {name} . Proceed with the app to see your total ratings!")
    option = st.selectbox("Select your age!:", [15, 16, 20, 21, 25])
    if option > 15:
        st.write (f"""{option} or higher is the age when you have the potential to do something!So,If you are doing something,That is fulfilling your potential,So you are on the right track!""")
    if option < 15:         
        st.write(f"{option} or below is the age when you actually know the difference between wrong and right to do something!")
    if option == 15:
        st.write(f"{option} is actually the age when you have already seen so many thing and have gone through so many things in your life! and have gotten so far in life!")
    hobby = st.text_input(str("What is your favourite hobby?:"))    
    if hobby:
        valid_hobby = all(c.isalpha() or c.isspace() for c in hobby)
        if valid_hobby:
            ai_response = generate_text(f"what do you think about the hobby {hobby}, you have to answer in maximum 25 words.")
            st.write(ai_response)
        else:
             st.write("Invalid input, Please enter a valid hobby!") 

    if st.button("RATE ME!"):
        valid_button = all(c.isalpha() or c.isspace() for c in name)
        if valid_button:
            ai_response = generate_text(f"""rate this fictional character i made for a cartoon story, and it is a human. on the scale form 1 to 10 according to the name: {name}, age :  {option} and hobby: {hobby}. You can use maximum 10 words. Only return the ratings and what you think abt the character, do not tell if any other information or something is needed restrict the response only ratings and what you think abt the character""")
            if ai_response:
                st.write(ai_response)
            else:
                 st.write("Fill out the form properly to generate your rating!")
    if name and hobby:
       st.write("Press this button to see your data!")
       current_time = datetime.now()
       if st.button("See your data!"):   
                    ratings_data = {
                "Name": [name],
                "Age": [option],
                "Hobby": [hobby],
                "Time": [current_time],
            }
                  
                  
                    df = pd.DataFrame(ratings_data)
                    st.write("Here is your data in a table:")
                    st.dataframe(df)
    if not (name or hobby) and (st.button("See your data!")):
        st.write("Please fill out the form to see your data!")
main()
