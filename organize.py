import os
import shutil
import sys

def create_folders(directories, directory_path):
    existing_folders = [folder.lower() for folder in os.listdir(directory_path)]
    for key in directories:
        if key.lower() not in existing_folders:
            os.mkdir(os.path.join(directory_path, key))
        elif key not in existing_folders:
            os.rename(os.path.join(directory_path, key.lower()), os.path.join(directory_path, key))
    if "OTHER" not in os.listdir(directory_path):
        os.mkdir(os.path.join(directory_path, "OTHER"))

def organize_folders(directories, directory_path):
    moved_files_count = 0
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            for key in directories:
                extension = directories[key]
                if file.endswith(extension) or (isinstance(extension, tuple) and file.lower().endswith(extension)):
                    dest_path = os.path.join(directory_path, key, file)
                    shutil.move(src_path, dest_path)
                    moved_files_count += 1
                    break
    return moved_files_count

def organize_remaining_files(directory_path):
    moved_files_count = 0
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            dest_path = os.path.join(directory_path, "OTHER", file)
            shutil.move(src_path, dest_path)
            moved_files_count += 1
    return moved_files_count

def organize_remaining_folders(directories, directory_path):
    moved_folders_count = 0
    list_dir = os.listdir(directory_path)
    organized_folders = [folder for folder in directories]
    for folder in list_dir:
        if folder not in organized_folders:
            src_path = os.path.join(directory_path, folder)
            dest_path = os.path.join(directory_path, "FOLDERS", folder)
            try:
                shutil.move(src_path, dest_path)
                moved_folders_count += 1
            except shutil.Error:
                shutil.move(src_path, dest_path + " - copy")
                print("That folder already exists in the destination folder."
                      "\nThe folder is renamed to '{}'".format(folder + " - copy"))
    return moved_folders_count

if __name__ == '__main__':
    directory_path = "C:/Users/Dell/Downloads"
    directories = {
        "Word": (".doc", ".docx"),
        "Images": (".jpg", ".jpeg", ".gif", ".png", ".jfif", ".svg"),
        "PDF": ".pdf",
        "Applications": (".exe", ".msi", ".appx", ".appxbundle", ".msu", ".dll", ".bat", ".cmd", ".com", ".scr"),
        "Video": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",".mng",".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "Voice": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",".mp3",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PowerPoint": (".pptx", ".pptm", ".ppt", ".potx"),
        "Compression": (".zip", ".z7", ".tar", ".gz", ".rar"),
        "PYTHON": ".py",
        "Java": ".js",
        "HTML": (".html5", ".html", ".htm", ".xhtml"),
        "NotePad": ".txt",

        "OTHER": "",
        "FOLDERS": "",
    }
    
    print("Started the moving process.")
    
    moved_files = organize_folders(directories, directory_path)
    moved_files += organize_remaining_files(directory_path)
    moved_folders = organize_remaining_folders(directories, directory_path)
    
    files_text = "files" if moved_files != 1 else "file"
    folders_text = "folders" if moved_folders != 1 else "folder"
    
    print(f"Moved {moved_files} {files_text} to their correct destination.")
    print(f"Moved {moved_folders} {folders_text} to their correct destination.")
    print("Finished moving the files. Press enter to continue.")
    
    input()  # Pause to allow the user to press enter before terminating
