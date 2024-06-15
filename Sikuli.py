# Import necessary Sikuli functions
from sikuli import *

# Set random seed for consistent behavior in Sikuli
import random
random.seed()

# Import necessary Java classes for playing system sound
from java.awt import Toolkit
from java.awt import Robot
from java.awt.event import InputEvent

# Import subprocess used for killing music
import subprocess

# Import necessary libraries for playing MP3 file
import os

# Import necessary Java classes
from java.io import IOException


# Function to click on image A
def click_refresh():
    type(Key.F5);

# Function to check if image B is present
def is_image_no_tasks_message_present():
    image_B = "1718456069990.png";  # Replace with your actual path
    region_B = Region(0,83,751,388) # Define the region for image_B (x, y, width, height)

    return region_B.exists(image_B)

# Function to show popup with continue and stop buttons
def show_popup():
    while True:
        choice = input("Do you want to continue execution? Type 'c' to continue or 's' to stop: ")
        if choice.lower() == 'c':
            return "Continue"
        elif choice.lower() == 's':
            return "Stop"
        else:
            print("Invalid choice. Please enter 'c' to continue or 's' to stop.")

    return result


def play_system_sound():
    try:
        # Use Sikuli's built-in App class to open the file with the default application
        file_path = "I:\Installations\Sikuli.sikuli\iphone_remix.mp3";
        app = App.open(file_path)
        wait(2)  # Wait for 2 seconds to ensure the application opens
    except Exception as e:
        print("Failed to open file:", e)

def kill_process_java(process_name):
   try:
       java = Java()
       java_lang = java.java.lang
       Runtime = java_lang.Runtime
       Process = java_lang.Process
       runtime = Runtime.getRuntime()
       process = runtime.exec(["taskkill", "/F", "/IM", process_name])
       process.waitFor()
       print("Successfully killed")
   except IOException as e:
           print("Error killing {process_name}: {e}")


# Main script
while True:
    wait(15);
    if is_image_no_tasks_message_present():
        wait(random.randint(10, 20))  # Wait for random time between 10 to 20 seconds
        click_refresh();
    else:
        play_system_sound();
        result = show_popup();
        if result == "Stop":
            # kill_process_java("Microsoft.Media.Player.exe");
            break  # Exit the loop if user chooses to stop execution
        wait(random.randint(10, 20))  # Wait for random time between 10 to 20 seconds
        
