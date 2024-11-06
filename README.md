# KEYSTREAMER
Keystream is a lightweight, Python-based tool that captures and streams keyboard input to a Command-and-Control (C2) server. Designed for educational purposes, this project demonstrates how keystrokes can be intercepted and sent over the network for further analysis.

Disclaimer: This project is intended for ethical hacking and educational use only. Misuse of this tool for unauthorized surveillance or activities is strictly prohibited.

Features
Captures keyboard inputs including standard and special keys (e.g., Shift, Enter, Alt, etc.).
Streams captured keystrokes to a C2 server in real-time.
Implements error handling for smooth operation.
Supports cross-platform use (Windows/Linux/macOS).
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/Keystream.git
cd Keystream
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the C2 server:

Open keystream.py and modify the c2_server_url variable to match your server's address where the keystroke data will be sent.

Run the tool:

bash
Copy code
python keystream.py
The program will begin capturing keystrokes and sending the data to your C2 server.

Usage
When the program is running, it will capture and log keystrokes, including special keys like:

Space ([SPACE])
Enter ([ENTER])
Tab ([TAB])
Backspace ([BACKSPACE])
Shift ([SHIFT])
Alt ([ALT])
Escape ([ESC])
The captured keystrokes will be sent to the server in the following JSON format:

json
Copy code
{
  "log": "[SPACE]"
}
Ethical Use Disclaimer
This tool is for educational use only. Unauthorized interception of keystrokes or access to computer systems is illegal. Always obtain explicit permission before using this tool.

License
This project is licensed under the MIT License - see the LICENSE file for details.
