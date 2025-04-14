import os
import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path

def extract_formula_fields(objects_dir):
    """
    Extracts information about formula fields from Salesforce object XML files.
    
    Args:
        objects_dir (str): Path to the Salesforce 'objects' directory
    
    Returns:
        pd.DataFrame: DataFrame containing information about all formula fields
    """
    # List to store all formula field data
    formula_fields = []
    
    # Iterate through each object folder
    for obj_dir in Path(objects_dir).iterdir():
        if not obj_dir.is_dir():
            continue
        
        object_name = obj_dir.name
        fields_dir = obj_dir / 'fields'
        
        # Skip if there's no fields directory
        if not fields_dir.exists() or not fields_dir.is_dir():
            continue
        
        # Process each field XML file
        for field_file in fields_dir.glob('*.field-meta.xml'):
            try:
                tree = ET.parse(field_file)
                root = tree.getroot()
                
                # Check if this is a formula field
                formula_element = root.find('{http://soap.sforce.com/2006/04/metadata}formula')
                if formula_element is None:
                    continue
                
                # Extract required information
                field_name = field_file.stem.replace('.field-meta', '')
                
                # Default values in case elements are not found
                field_label = ""
                data_type = ""
                formula = ""
                description = ""
                
                # Find and extract the elements we need
                label_element = root.find('{http://soap.sforce.com/2006/04/metadata}label')
                if label_element is not None:
                    field_label = label_element.text or ""
                
                type_element = root.find('{http://soap.sforce.com/2006/04/metadata}type')
                if type_element is not None:
                    data_type = type_element.text or ""
                
                if formula_element is not None:
                    formula = formula_element.text or ""
                
                description_element = root.find('{http://soap.sforce.com/2006/04/metadata}description')
                if description_element is not None:
                    description = description_element.text or ""
                
                # Add to our list
                formula_fields.append({
                    'Object Name': object_name,
                    'Field Label': field_label,
                    'Field Name': field_name,
                    'Data Type': data_type,
                    'Formula': formula,
                    'Dev Comments': description
                })
                
            except Exception as e:
                print(f"Error processing {field_file}: {e}")
    
    # Convert list to DataFrame
    return pd.DataFrame(formula_fields)

def main():
    # Get the path to the objects directory from user
    objects_dir = input("Please enter the path to your Salesforce project's 'objects' folder: ")
    
    # Validate the path
    if not os.path.isdir(objects_dir):
        print(f"Error: '{objects_dir}' is not a valid directory.")
        return
    
    print(f"Analyzing Salesforce objects in {objects_dir}...")
    
    # Extract formula fields
    formula_df = extract_formula_fields(objects_dir)
    
    # Check if any formula fields were found
    if len(formula_df) == 0:
        print("No formula fields were found in the specified directory.")
        return
    
    # Ask user for output file path
    output_file = input("Please enter the path for the output Excel file (e.g., formula_fields.xlsx): ")
    
    # Save to Excel
    formula_df.to_excel(output_file, index=False)
    print(f"Successfully extracted {len(formula_df)} formula fields to {output_file}")

if __name__ == "__main__":
    main()