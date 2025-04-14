import os
import xml.dom.minidom as minidom
import shutil

def create_sample_sf_project(base_dir="sample_salesforce_project"):
    """
    Creates a sample Salesforce project structure with some objects and formula fields
    for testing purposes.
    
    Args:
        base_dir (str): Base directory to create the sample project
    """
    # Create base directory structure
    objects_dir = os.path.join(base_dir, "force-app", "main", "default", "objects")
    os.makedirs(objects_dir, exist_ok=True)
    
    # Define some sample objects with formula fields
    objects = {
        "Account": [
            {
                "name": "Annual_Revenue_Thousands__c",
                "label": "Annual Revenue (Thousands)",
                "type": "Currency",
                "formula": "AnnualRevenue / 1000",
                "description": "Annual revenue in thousands of dollars"
            },
            {
                "name": "Full_Billing_Address__c",
                "label": "Full Billing Address",
                "type": "Text",
                "formula": "BillingStreet & \", \" & BillingCity & \", \" & BillingState & \" \" & BillingPostalCode",
                "description": "Concatenated billing address for display purposes"
            }
        ],
        "Contact": [
            {
                "name": "Full_Name__c",
                "label": "Full Name",
                "type": "Text",
                "formula": "FirstName & \" \" & LastName",
                "description": "Concatenated first and last name"
            },
            {
                "name": "Age__c",
                "label": "Age",
                "type": "Number",
                "formula": "(TODAY() - Birthdate) / 365.25",
                "description": "Calculated age based on birthdate"
            }
        ],
        "Opportunity": [
            {
                "name": "Discount_Amount__c",
                "label": "Discount Amount",
                "type": "Currency",
                "formula": "Amount * Discount_Percentage__c / 100",
                "description": "Calculated discount amount based on percentage"
            },
            {
                "name": "Days_Open__c",
                "label": "Days Open",
                "type": "Number",
                "formula": "TODAY() - CreatedDate",
                "description": "Number of days the opportunity has been open"
            }
        ],
        "Custom_Object__c": [
            {
                "name": "Status_Indicator__c",
                "label": "Status Indicator",
                "type": "Text",
                "formula": "IF(Status__c = \"Active\", \"🟢\", IF(Status__c = \"Pending\", \"🟡\", \"🔴\"))",
                "description": "Visual indicator of status using emoji"
            }
        ]
    }
    
    # Create object directories and field files
    for obj_name, fields in objects.items():
        # Create object directory
        obj_dir = os.path.join(objects_dir, obj_name)
        fields_dir = os.path.join(obj_dir, "fields")
        os.makedirs(fields_dir, exist_ok=True)
        
        # Create a basic object-meta.xml file
        obj_meta_path = os.path.join(obj_dir, f"{obj_name}.object-meta.xml")
        with open(obj_meta_path, "w") as f:
            f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <label>{obj_name.replace('_c', '').replace('__c', '')}</label>
    <pluralLabel>{obj_name.replace('_c', '').replace('__c', '')}s</pluralLabel>
</CustomObject>
""")
        
        # Create field files
        for field in fields:
            field_path = os.path.join(fields_dir, f"{field['name']}.field-meta.xml")
            
            # Create XML content for the field
            xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{field['name']}</fullName>
    <label>{field['label']}</label>
    <type>{field['type']}</type>
    <formula>{field['formula']}</formula>
    <description>{field['description']}</description>
    <inlineHelpText>{field['description']}</inlineHelpText>
</CustomField>
"""
            # Write pretty-printed XML
            dom = minidom.parseString(xml_content)
            pretty_xml = dom.toprettyxml(indent="    ")
            with open(field_path, "w") as f:
                f.write(pretty_xml)
        
        # Also create some non-formula fields for completeness
        non_formula_field = os.path.join(fields_dir, "Regular_Field__c.field-meta.xml")
        non_formula_xml = """<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Regular_Field__c</fullName>
    <label>Regular Field</label>
    <type>Text</type>
    <length>255</length>
    <description>This is a regular non-formula field</description>
</CustomField>
"""
        dom = minidom.parseString(non_formula_xml)
        pretty_xml = dom.toprettyxml(indent="    ")
        with open(non_formula_field, "w") as f:
            f.write(pretty_xml)
    
    print(f"Sample Salesforce project created at: {os.path.abspath(base_dir)}")
    print(f"To test the extractor, use this path: {os.path.abspath(objects_dir)}")

if __name__ == "__main__":
    # Clean up any existing sample project
    if os.path.exists("sample_salesforce_project"):
        shutil.rmtree("sample_salesforce_project")
    
    # Create a new sample project
    create_sample_sf_project()