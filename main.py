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
from getch import getch, pause
import warnings


# Put constants and configuration here
def main_menu_display():
    print(
        "*-Water Potability Data Analyzer-*\n"
    "1. View Potability Analysis.\n" 
    "2. Create Data Visualization.\n"
    "3. Explain Dataset Issues\n"
    "4. Exit Program\n"

    )






def solutions_report():
    print(
        "1. Propose Solutions\n"
        "2. View Guidesn\n"
        "Exit to Main Menu\n"
    )


 # Add data processing functions here
def load_dataset():
     global df
     df = pd.read_csv("data/water_potability.csv")
     df.rename(columns={
    "ph":"Ph",
    "Organic_carbon":"Organic Carbon"
})

load_dataset()
df.round(decimals=2)
pd.set_option('display.max_columns', df.columns.size)
pd.set_option('display.expand_frame_repr', False)
# Add analysis functions here 

def basic_stats():
    print(df.describe(include = 'all').round({"Ph": 2, "Hardness" : 2, "Solids" : 2, "Chloramines" : 2, "Sulfate" : 2, "Conductivity" : 2, "Organic Carbon" : 2, "Trihalomethanes" : 2, "Turbidity" : 2, "Potability" : 0}))


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


# Add Visualization functions here
#This is the bar chart that I am having issues with
sns.set_theme()
def summary_bar_graph():
    sns.barplot(data=df)
    plt.show(block = False)
#ummary_bar_graph()

def summary_histogram():
    sns.histplot(data=df)
    plt.subplots_adjust(left = 0.3)
    plt.show(block = False)
#summary_histogram()
warnings.filterwarnings("ignore", message= "UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.")
def summary_scatter_plot():
    sns.scatterplot(data=df)
    plt.show(block = False)

# Add main program functions here

def data_visualization():
    while True:
        visualization_menu = input(
            "1. Bar Graphs\n"
            "2. Histogram\n"
            "3. Scatter Plot\n"
            "4. Exit to Main Menu\n")
        if visualization_menu == "1":
            print("This may take a bit...")
            summary_bar_graph()
            input("Press Enter to continue...")
        elif visualization_menu == "2":
            print("This may take a bit...")
            summary_histogram()
            input("Press Enter to continue...")
        elif visualization_menu == "3":
            print("This may take a bit")
            summary_scatter_plot()
            input("Press Enter to continue...")
        elif visualization_menu == "4":
            break
        else:
            print("\n- Please enter a valid option -\n")
        
    


def potability_analysis():
    while True:    
        potability_menu = input(
            "1. Basic Analysis.\n"
            "2. Identify Trends & Pattern in Data\n"
            "3. Category Explanations\n"
            "4. Exit Back to Main Menu\n"
            )
        if potability_menu == "1":
            basic_stats()
            input("Press Enter to continue...\n")
        elif potability_menu == "2":
            print("")
        elif potability_menu == "3":
            input("The different categories are:\n\n" 
            "Ph: The Acidity/Base of the water sample. Should be around 6.5 to 8.5 Ph.\n\n" "Hardness: The amount of Calcium & Magnesium in the water. Should be under 170mg/l.\n\n"
            "Solids: The amount of substances dissolved in water. Should be below 300 ppm. I discovered through my data analysis that my data has an \n extremely high and incorrect amount of solids in the water at an average of 22014.09 ppm, which isn't really possible.\n\n "
            "Chloramines: These are disenfectants used to treat drinking water, which can be unsafe. This should be below 4 ppm or mg/l. \n\n "
            "Sulfates: These are naturally occurring minerals that can dissolve into groundwater from soil and rock formations. Not too dangerous, \n but can have adverse health effects at high levels. Should be below 250 ppm.\n\n" 
            "Conductivity: How well water conducts electricity. It's a good indicator of Dissolved Solids in water and can affect taste. \n This should be less than 1,000 microsiemens per centimeter\n\n "
            "Organic Carbon: This is the measure of the total organic compounds in the water sample. There is no standard for Organic Carbon in water,\n but certain compunds can have adverse effects\n\n "
            "Trihalomethanes: A chemical byproduct from when chlorine or other halogen disenfectants react with organic material in water.\n At high levels, they can cause serious health issues such as bladder cancer and reproductive issues.\n This should be below 80 parts per billion(ppb)\n\n"
            "Turbidity: This is a measure of the clearness of water and is a key indicator in water quality. While not dangerous in itself, high Turbidity usually indicates poor water quality and high soil content in the water. There is no required turbidity level, but the EPA recommendation is around 5 Nephelometric Turbidity Units (NTU)\n\n"
            "Potability: This stat uses all the other metrics to judge if the water is drinkable or not. 1 represents drinkable water, while 0 represents unsafe water. I have discovered through my data analysis that this statistic appears to be relatively inaccurate\n\n\n"
            "Press Enter key when finished"    )
        elif potability_menu == "4":
            break
        else:
            print("- Please enter a valid option -")

def data_issue_explanation():
    print("")


def opening_menu():
    while True:
        main_menu_display()
        main_menu_choice = input()
        if main_menu_choice == "1":
            potability_analysis() 
        elif main_menu_choice == "2":
            print(data_visualization())
        elif main_menu_choice == "3":
            data_issue_explanation()
        elif main_menu_choice == "4":
            print("Exiting...")
            break
        else:
            print("\n- Please enter a valid option -\n")
            continue
    


opening_menu()
