from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3

import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate a response using the Gemini-Pro model from Google's Generative AI.
def get_response_from_gemini_model(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

# Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT amd has the following columns - ID, NAME, CLASS, SECTION \n\n
    For example, \n
    Example 1 - How many entries of records are present?, the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
    also the SQL code should not have ``` in beginning or end and sql word in output
    """
]


# Streamlit APP

st.set_page_config(page_title="Retrieve Any SQL Query")
st.header("Gemini App to retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask The Question")

# If submit is clicked
if submit:
    response = get_response_from_gemini_model(question, prompt[0])
    print(response)
    query_response = read_sql_query(response, 'student.db')
    st.header('The Result is:')
    st.text(f"\nQUERY: \n{response}\n")
    for row in query_response:
        st.text(row)