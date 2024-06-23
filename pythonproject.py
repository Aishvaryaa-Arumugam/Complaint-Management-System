import mysql.connector
import streamlit as st

def create_database():
    connection = mysql.connector.connect(host = "localhost",
                              user = "root",
                              password = "aishu")
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Complaint_Management_System")
    cursor.close()
    connection.close()

def connect_database():
    return mysql.connector.connect(host= "localhost",
                                   user = "root",
                                   password = "aishu",
                                   database = "Complaint_Management_System")

def raise_complaint():
    st.title("Complaint Management System")
    Name = st.text_input("Name",key="your name")
    Contact_details = st.text_input("Contact Number",key="your mobile number")
    Email = st.text_input("Email id",key="your email id")
    Complaint = st.text_input("Complaint",key="write down your feedback")

    if st.button("Submit"):
        if Name and Contact_details and Email and Complaint:
            create_database()
            cxn = connect_database()
            mycursor = cxn.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS customer_inputs (name VARCHAR(255),contact_details VARCHAR(15),email VARCHAR(255),complaint VARCHAR(255))")
            
            sql = "insert into customer_inputs (name,contact_details,email,complaint) values (%s,%s,%s,%s)"
            val = (Name,Contact_details,Email,Complaint)
            mycursor.execute(sql,val)
            cxn.commit()
            st.success("Complaint has been registered. Our executive shall contact you")
        else:
            print("Enter all the fields")

complaint = raise_complaint()  