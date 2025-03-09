# Keylogger Project

## Overview
This is a simple keylogger application built in Python using the pynput library. The program captures keyboard inputs and saves them to a text file.

## Features
* Records keystrokes in real-time
* Saves captured keystrokes to a log file
* Filters special keys for better readability
* Terminates when the Escape key is pressed

## Requirements
* Python 3.x
* pynput library

## Installation
1. Ensure you have Python installed on your system
2. Install the required library using pip:

```
pip install pynput
```

## Usage
1. Run the script:

```
python keylogger.py
```

2. The program will start capturing keystrokes
3. Every 10 keystrokes, the data is saved to "log.txt" in the same directory
4. Press the Escape key to stop the keylogger

## How It Works
The keylogger uses event listeners to capture keyboard inputs:
* `on_press()`: Captures each key press and adds it to a buffer
* `write_file()`: Processes the collected keystrokes and writes them to a log file
* `on_release()`: Checks for the Escape key to terminate the program

The program distinguishes between regular characters and special keys (like Space, Enter, etc.) for cleaner logging.

## Warning
This type of application should only be used for legitimate purposes such as:
* Monitoring your own computer
* Educational purposes
* With explicit consent from all users of the monitored system

Unauthorized monitoring of computer usage is illegal in many jurisdictions and violates privacy rights.

## License
This project is meant for educational purposes only.
