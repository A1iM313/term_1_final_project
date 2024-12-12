# Enter description here
# This is a program to analyze water potability dataset, display visualizations, and generate solutions for low potability.
# It will interact with the user through a CLI and allow flec
# 
#
#
# Add imports here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from simple_term_menu import TerminalMenu



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
     global df
     df = pd.read_csv("data/BKB_WaterQualityData_2020084.csv")


load_dataset()


# Add analysis functions here 

def basic_stats():
    print(df.describe())
    print(df.info())
basic_stats()

def find_average():
    print(df.mean)
    
def find_count():
    print(df.count)

def find_std():
    print(df.std)

def find_min():
    print(df.min)

def find_max():
    print(df.max)

def view_ph_data():
    print(df["Ph"].describe())

def view_hardness():
    print(df["Hardness"].describe())


# This is the data category that is the issue
def view_solids():
    print(df["Solids"].describe())

def view_chloramines():
    print(df["Chloramines"].describe())

def view_sulfates():
    print(df["Sulfate"].describe())

def view_conductivity():
    print(df["Conductivity"].describe())

def view_organic_carbon():
    print(df["Organic Carbon"].describe())

def view_trihalomethanes():
    print(df["Trihalomethanes"].describe())

def view_turbidity():
    print(df["Turbidity"].describe())

def view_potability():
    print(df["Potability"].describe())

  
# Add interactive features and menus here
# def interactive_main():
#     options = ["1. View Potability Analysis", "2. Visualize Data", "3. Generate Solutions Report"]
#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show
#     print(f"You have selected {options[menu_entry_index]}!")

# if __name__ == "__main__":
#     interactive_main()

# Add Visualization functions here
#This is the bar chart that I am having issues with
sns.set_theme()
def summary_bar_graph():
    sns.barplot(data=df)
    plt.show()
summary_bar_graph()


# Add main program functions here

main_menu()
