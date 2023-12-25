# Allows to do some high level operations on the file system
import os
import shutil


# Avaliable types
IMAGE_TYPES = [".jpg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".jpeg",
               ".mov", ".heic", ".webm"]
DOCUMENT_TYPES = [".doc", ".docx", ".pdf", ".ppt",
                  ".pptx", ".xls", ".xlsx", ".txt", ".rtf"]
AUDIO_TYPES = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
VIDEO_TYPES = [".mp4", "m4a", ".avi", ".mkv", ".mov", ".wmv"]
ARCHIVE_TYPES = [".zip", ".rar", ".7z", ".tar.gz", ".tar"]
EXECUTABLE_TYPES = [".exe", ".dmg", ".apk", ".deb", ".rpm"]
CODE_TYPES = [".html", ".css", ".js", ".py", ".java", ".cpp",
              ".json", ".xml", ".md", ".yml", ".yaml", ".go",
              ".rb", ".php", ".swift", ".c", ".h", ".pl", ".lua",
              ".scala", ".ts"]
SPREADSHEET_TYPES = [".csv", ".db", ".sqlite", ".sql"]
CUSTOM_EXTENSION = [".psd", ".myext", ".xyzdata",
                    ".userconfig", ".logdata", ".veg"]

# Colors for console
PURPLE_COLOR = "\033[95m"
DEFAULT_COLOR = "\033[0m"


def sort_shortcuts(path):
    try:
        # Flag to track if any files were moved
        files_moved = False

        for file in os.listdir(path):

            # IMAGES
            if any(file.lower().endswith(t) for t in IMAGE_TYPES):
                """Create a path to the file"""
                file_path = os.path.join(path, file)
                """Create the path to the new folder"""
                folder_path = os.path.join(path, "Images")

                """If folder not exist, make folder with following name"""
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                """Move files into a new directory"""
                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

            # DOCUMENTS
            elif any(file.lower().endswith(t) for t in DOCUMENT_TYPES):
                file_path = os.path.join(path, file)
                folder_path = os.path.join(path, "Documents")

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

            # AUDIO
            elif any(file.lower().endswith(t) for t in AUDIO_TYPES):
                file_path = os.path.join(path, file)
                folder_path = os.path.join(path, "Audios")

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

            # VIDEO
            elif any(file.lower().endswith(t) for t in VIDEO_TYPES):
                file_path = os.path.join(path, file)
                folder_path = os.path.join(path, "Videos")

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

            # ARCHIVES
            elif any(file.lower().endswith(t) for t in ARCHIVE_TYPES):
                file_path = os.path.join(path, file)
                folder_path = os.path.join(path, "Archives")

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

            # EXECUTABLE
            elif any(file.lower().endswith(t) for t in EXECUTABLE_TYPES):
                file_path = os.path.join(path, file)
                folder_path = os.path.join(path, "Executables")

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

            # CUSTOM
            elif any(file.lower().endswith(t) for t in CUSTOM_EXTENSION):
                file_path = os.path.join(path, file)
                folder_path = os.path.join(path, "Custom extension")

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

            # CODE
            elif any(file.lower().endswith(t) for t in CODE_TYPES):
                file_path = os.path.join(path, file)
                folder_path = os.path.join(path, "Code")

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

            # SPREADSHEET
            elif any(file.lower().endswith(t) for t in SPREADSHEET_TYPES):
                file_path = os.path.join(path, file)
                folder_path = os.path.join(path, "Spreadsheet")

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, folder_path)
                print(f"Successfully sorted: {file}")
                files_moved = True

        if not files_moved:
            print("No files to move!")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    while True:
        try:
            print(f"{PURPLE_COLOR}Main Menu:\
            \n[1] Enter my own directory\
            \n[2] Sort Desktop\
            \n[3] Sort Downloads\
            \n[4] Exit{DEFAULT_COLOR}")

            response = input()

            if response == "1":
                """Operate user direction"""
                print(
                    f"{PURPLE_COLOR}Enter the full path to the directory you want to sort{DEFAULT_COLOR}")
                path = (input()).strip()

                if os.path.exists(path):
                    sort_shortcuts(path)
                else:
                    raise FileExistsError("Directory not found, try again!")

            elif response == "2":
                """Automete sort Desktop"""
                user_home_directory = os.path.expanduser("~")
                desktop = os.path.join(user_home_directory, "Desktop")
                sort_shortcuts(desktop)

            elif response == "3":
                """Automate sort downloads"""
                user_home_directory = os.path.expanduser("~")
                desktop = os.path.join(user_home_directory, "Downloads")
                sort_shortcuts(desktop)

            elif response == "4":
                print(f"{PURPLE_COLOR}See you later!{DEFAULT_COLOR}")
                break

            else:
                raise ValueError(
                    "Invalid Input! Please choose a number from the menu!")

        except (FileExistsError, PermissionError) as e:
            print(f"ERROR OCCURRED! {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Hi everyone! Welcome to this file organization program. \nHere's how it works:\
          \n[1] Enter my own directory: Manually input the full path to the directory you want to sort.\
          \n[2] Sort Desktop: Automatically organizes files on your Desktop.\
          \n[3] Sort Downloads: Automatically organizes files in your Downloads folder.\
          \n[4] Exit: Exit the program. \nLet's get started!\n\n")

    main()
