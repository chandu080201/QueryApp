from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenAI API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide responses
def get_gemini_response(question: str, prompt: list) -> str:
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

# Function to retrieve query results from the database
def execute_sql_query(sql_query: str, db_path: str):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(sql_query)
        rows = cur.fetchall()
    return rows

# Define Prompt
def get_prompt() -> list:
    return [
        """
        You are an expert in converting English questions to SQL queries!
        The SQL database is named STUDENT and has the following columns: NAME, CLASS, SECTION.
        
        Examples:
        1. Question: How many records are present?
           SQL: SELECT COUNT(*) FROM STUDENT;
        2. Question: List all students in the Data Science class.
           SQL: SELECT * FROM STUDENT WHERE CLASS='Data Science';
        
        Ensure the SQL output is clean, without ``` or 'sql' in it.
        """
    ]

# Streamlit App Configuration
st.set_page_config(page_title="Query Master App")
st.header("Query Master App")

# User Input
question = st.text_input("Enter your question:", key="input")
submit = st.button("Generate SQL & Fetch Data")

# Process User Query
if submit and question:
    prompt = get_prompt()
    sql_query = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(sql_query, language='sql')
    
    results = execute_sql_query(sql_query, "student.db")
    
    st.subheader("Query Results:")
    if results:
        for row in results:
            st.write(row)
    else:
        st.write("No records found.")
