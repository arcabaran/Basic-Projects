# resume_analyzer.py

import base64
import mysql.connector
import pandas as pd
import streamlit as st
from pyresparser import ResumeParser
import nltk

nltk.download('stopwords')

def parse_resume(file_path):
    data = ResumeParser(file_path).get_extracted_data()
    return data

def structure_data(resume_data):
    df = pd.DataFrame([resume_data])
    return df

def store_data_in_mysql(data):
    connection = mysql.connector.connect(
        host="localhost",    # Change if your MySQL server is hosted elsewhere
        user="root",         # Replace with your MySQL username
        password="123root",  # Replace with your MySQL password
        database="resume_analyzer"  # Ensure this matches your created database
    )
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO resumes (name, email, skills, experience, education)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['name'], data['email'], data['skills'],
          data['total_experience'], data['education']))
    connection.commit()
    cursor.close()
    connection.close()

def create_dashboard(structured_data):
    st.title("Resume Analyzer Admin Dashboard")
    st.write("Parsed Resumes")
    st.table(structured_data)

if __name__ == "__main__":
    # Example usage
    resume_data = parse_resume('sample_resume.pdf')
    structured_data = structure_data(resume_data)
    store_data_in_mysql(resume_data)
    create_dashboard(structured_data)