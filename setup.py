from setuptools import setup, find_packages

setup(
    name="salesforce_formula_extractor",
    version="0.1.0",
    description="Extract formula fields from Salesforce project files",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "openpyxl>=3.0.9",
    ],
    entry_points={
        'console_scripts': [
            'sf_formula_extract=salesforce_formula_extractor:main',
        ],
    },
    python_requires='>=3.6',
)