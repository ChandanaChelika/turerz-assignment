import pdfplumber
import openpyxl
import re

# Input & Output paths
pdf_path = "data/Data Input.pdf"
excel_path = "Output.xlsx"

# Load PDF
with pdfplumber.open(pdf_path) as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"

# Clean text
cleaned = text.strip()

# Split into sentences for comment extraction
sentences = re.split(r'(?<=[.!?])\s+', cleaned)

# Define the keys we need to extract
keys = {
    "First Name": r"Vijay",
    "Last Name": r"Kumar",
    "Date of Birth": r"March 15, 1989|15, 1989",
    "Birth City": r"Jaipur",
    "Birth State": r"Rajasthan",
    "Age": r"35",
    "Blood Group": r"O\+",
    "Nationality": r"Indian",
    "Joining Date of first professional role": r"July 1, 2012",
    "Designation of first professional role": r"Junior Developer",
    "Salary of first professional role": r"350,000|350000",
    "Salary currency of first professional role": r"INR",
    "Current Organization": r"Resse Analytics",
    "Current Joining Date": r"June 15, 2021",
    "Current Designation": r"Senior Data Engineer",
    "Current Salary": r"2,800,000|2800000",
    "Current Salary Currency": r"INR",
    "Previous Organization": r"LakeCorp",
    "Previous Joining Date": r"February 1, 2018",
    "Previous end year": r"2021",
    "Previous Starting Designation": r"Data Analyst",
    "High School": r"St\. Xavier",
    "12th standard pass out year": r"2007",
    "12th overall board score": r"92\.5|92.50",
    "Undergraduate degree": r"B\.Tech",
    "Undergraduate college": r"IIT Delhi",
    "Undergraduate year": r"2011",
    "Undergraduate CGPA": r"8\.7",
    "Graduation degree": r"M\.Tech",
    "Graduation college": r"IIT Bombay",
    "Graduation year": r"2013",
    "Graduation CGPA": r"9\.2",
    "Certifications 1": r"AWS",
    "Certifications 2": r"Azure",
    "Certifications 3": r"Project Management Professional",
    "Certifications 4": r"SAFe",
    "Technical Proficiency": r"SQL expertise|Python proficiency|machine learning"
}

# Excel setup
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Key", "Value", "Comments"])

# Extract Key–Value pairs + comments
for key, pattern in keys.items():
    match = re.search(pattern, cleaned)
    value = match.group(0) if match else "Not found"

    # Find sentence that contains the value → comment
    comment = ""
    for s in sentences:
        if value in s:
            comment = s.strip()
            break

    ws.append([key, value, comment])

# Save Excel
wb.save(excel_path)

print("Excel file created successfully:", excel_path)
