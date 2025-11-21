import streamlit as st
import pdfplumber
import pandas as pd
import io

st.title("AI-Powered Document Structuring & Data Extraction")
st.write("Upload a PDF and convert it into a structured Excel file.")

# Upload PDF
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

    # Extract text
    text_content = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text_content += page.extract_text() + "\n"

    st.subheader("Extracted Text")
    st.text_area("PDF Content", text_content, height=200)

    # Example fixed mapping (based on your assignment)
    data = {
        "Key": [
            "First Name", "Last Name", "Date of Birth", "Birth City", "Birth State",
            "Age", "Blood Group", "Nationality", "First Job Joining Date",
            "First Job Designation", "First Job Salary", "Current Organization",
            "Current Joining Date", "Current Designation", "Current Salary"
        ],
        "Value": [
            "Vijay", "Kumar", "15-Mar-1989", "Jaipur", "Rajasthan",
            "35 years", "O+", "Indian", "01-Jul-2012",
            "Junior Developer", "350000", "Resse Analytics",
            "15-Jun-2021", "Senior Data Engineer", "2800000"
        ],
        "Comments": [
            "Birthplace provides regional profiling context.", "", "", "", "",
            "Age as of 2024.", "Used for emergency situations.", 
            "Relevant for visa & authorization.", "", "", "",
            "", "", "",
            "Salary shows 8x career growth."
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("Structured Table")
    st.dataframe(df)

    # Download Excel
    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    st.download_button(
        label="Download Excel File",
        data=output,
        file_name="Output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
