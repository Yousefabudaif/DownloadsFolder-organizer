# Downloads-organizer
 I made this project for the purpose of organizing my Donwloads-folder.
 The script creates several folders in Downloads and moves files with specific extensions to their corresponding folder.
 Folders that are downloaded are also automaticly moved to the 'FOLDERS' folder.
 The script is very easy to addapt to suit your needs, so feel free to tinquer with it.
 
 I recommend using .exe version of the script, which can easily be made with pyinstaller.
 In order to make the .exe file, follow the following steps:
 Install PyInstaller:
 If you haven't installed PyInstaller yet, you can install it using pip:
 pip install pyinstaller
 Navigate to the directory containing your Python script:
 Open a command prompt or terminal and navigate to the directory containing your Python script.
 Create the executable:
 Run the following command to create the executable:
 pyinstaller your_script.py
 Locate the executable:
 After running the command, PyInstaller will create a dist directory in the same directory as your script. Inside the dist directory, you'll find the executable 
 file with the same name as your script.
 I personnally put the .exe file in my startup folder so that it automaticly organizes my files when I log in on my computer (C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp).
 
 Based on suggestions, I made an exe version of the script which organizes the direcotry where the organize_local_directory.exe is located  so that it can easily be used on any folder.
 
 This is my first project to be posted on github. So please adjust your expectations accordingly :) .
 
## Requirements
 The script only uses standard python modules so there is no need to install aditional modules.
 The script itself requires a Python interpreter to run. I normally run it in my IDE.
 You might need to install shutil if it was not already installed.
 
## How to use
Change the directory_path variable in the organizer.py script and then run the script anyway you see fit.

Alternatively you can run the organize_local_directory.exe to organize the folder where the exe file is located.
 
## Important
 Depending on the size of your (Downloads-) folder it can take quite a while for all the files to move/organize during the first run. Don't terminate the script while it's running because that may corrupt some of your files.
