import tkinter as tk
from tkinter import filedialog
import os
import subprocess

print("Doki Doki Modding Tool | V1.0.0 | Load Success.")
print("⚠ DISCLAIMER: Please do not steal assets from any game and use them for your own profit. Those practices are highly illegal if the assets are copyrighted. The creator of this program is not responsible for any kind of damage. You're very much fine to use the assets for a mod, nothing else is allowed unless the game developers state it. ⚠")
print("ACKNOWLEDGEMENT: This script is written in Python 3.8 and uses rpatool to extract. All these will be linked in a file called 'credits.txt'.")

### extractRPA() makes a .bat file, and using rpatool, it extracts the .rpa file using this: python rpatool.py -x yourrpafile.rpa ###
def extractRPA():
	path = filedialog.askopenfile(initialdir='/', title='Choose .rpa file to extract.')
	f = open("command.bat", "a")

	### try writing code to batch file ###
	try:
		f.write(f"python rpatool.py -x {path.name}")
	except:
		print("An error occured while writing batch code to extract files to 'command.bat'. Please make sure you did not close the file dialog box because that'll return NoneType as the path.")

	print("DEBUG: Written batch code to .bat file.")
	f.close()

	### this part now executes the .bat file ###
	try:
		subprocess.call("command.bat")
	except Exception:
		print("An error occured when calling the command.bat process. Make sure that the file exists and hasn't been modified.")
	### this is the end, everything is now done and the .rpa file should be extracted in the directory. ###


### GUI ###
root = tk.Tk()
root.title = "Doki Doki Modding Tool!"
extract_button = tk.Button(root, text="Extract .rpa file.", command=extractRPA)
extract_button.pack()
toptext = tk.Label(root, text="Made by Trayambak#2711")
toptext.pack()
root.mainloop()

