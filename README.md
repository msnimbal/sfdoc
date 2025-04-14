Salesforce Formula Fields Extractor
A Python utility to extract and analyze formula fields from Salesforce project files.
Description
This tool scans through a Salesforce project's "objects" folder structure, identifies formula fields by examining field XML files, and extracts relevant information into a single Excel spreadsheet for easy analysis.
Features

Automatically traverses Salesforce object folder structures
Identifies formula fields by checking for <formula> XML tags
Extracts key information from each formula field:

Object Name
Field Label
Field Name (API Name)
Data Type
Formula Expression
Developer Comments



Requirements

Python 3.6 or higher
pandas
openpyxl

Installation
bash# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
Usage
bashpython salesforce_formula_extractor.py
When prompted:

Enter the path to your Salesforce project's "objects" folder
Specify the output Excel file path

Output
The script generates an Excel file with the following columns:

Object Name
Field Label
Field Name
Data Type
Formula
Dev Comments

Example
Please enter the path to your Salesforce project's 'objects' folder: C:/Projects/MySalesforceProject/force-app/main/default/objects
Analyzing Salesforce objects in C:/Projects/MySalesforceProject/force-app/main/default/objects...
Please enter the path for the output Excel file: formula_fields.xlsx
Successfully extracted 42 formula fields to formula_fields.xlsx
License
MIT License