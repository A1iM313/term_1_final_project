# Enter description here
# This is a program to analyze water potability dataset, display visualizations, and generate solutions for low potability.
# It will interact with the user through a CLI and
# 
#
#
# Add imports here
import pandas as pd
import matplotlib as plt


# Put constants and configuration here
def main_menu():
    print(
        "*-Water Potability Data Analyzer-*\n"
    "1. View Potability Analysis.\n" 
    "2. Create Data Visualization.\n"
    "3. Generate Solutions Report.\n"
    "4. Exit Program\n"

    )


def potability_analysis():
    print(
        "1. Simplified Analysis."
        "2. Verbose Analysis."
        "3. Identify Trends & Pattern in Data"
        "4. Category Explanations"
        "5. Exit Back to Main Menu"
        )


def data_visualization():
    print(
        "1. Bar Graphs"
        "2. Heatmaps"
        "3. Scatter Plot"
        "4. Box Plot"
        "5. Exit to Main Menu"
    )


def solutions_report():
    print(
        "1. Propose Solutions"
        "2. View Guides"
        "Exit to Main Menu"
    )


 # Add data processing functions here
def load_dataset():
     df = pd.read_csv("data/water_potability.csv")
      


load_dataset()

# Add analysis functions here 



# Add interactive features and menus here



# Add Visualization functions here




# Add main program functions here

main_menu()
