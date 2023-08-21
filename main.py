import os
import shutil

# Define the file types and their extensions
docs = ['.doc', '.docx', '.pdf', '.txt', '.odt']
images = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
videos = ['.mp4', '.avi', '.mov', '.mkv', '.wmv']
audios = ['.mp3', '.wav', '.ogg', '.flac', '.m4a']
archives = ['.zip', '.rar']
executables = ['.msi', '.msm', '.msp', '.mst', '.appx', '.appinstaller', '.exe']

# Create a list of all the extensions
extensions = docs + images + videos + audios + archives + executables

# Define the paths to the source and destination folders
downloads_folder = "C:/Users/190ib/OneDrive/Pictures"

# Function to create a folder
def create_folder(folder_name):
    folder_path = os.path.join(downloads_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to determine the destination folder based on file extension
def sort_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension in docs:
        destination_folder = "Documents"
    elif file_extension in images:
        destination_folder = "Images"
    elif file_extension in videos:
        destination_folder = "Videos"
    elif file_extension in audios:
        destination_folder = "Audios"
    elif file_extension in archives:
        destination_folder = "Archives"
    elif file_extension in executables:
        destination_folder = "Executables"
    else:
        destination_folder = "Others"

    return destination_folder


# Function to remove empty folders recursively
def remove_empty_folders(path_abs):
    # Get a list of all subdirectories, starting from the deepest level
    walk = list(os.walk(path_abs))

    # Traverse the subdirectories in reverse order
    for path, _, _ in walk[::-1]:
        # Check if the directory is empty
        if len(os.listdir(path)) == 0:
            folder_name = os.path.basename(path)
            # Remove the empty directory
            os.rmdir(path)
            print(f"{folder_name} is empty, {folder_name} is deleted")

# Main function
def main():
    # Create necessary destination folders
    create_folder("Documents")
    create_folder("Images")
    create_folder("Videos")
    create_folder("Audios")
    create_folder("Archives")
    create_folder("Executables")
    create_folder("Others")

    # Loop through files in the downloads folder
    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)

        if os.path.isfile(item_path):
            # Determine destination folder for the file
            destination_folder = sort_file(item_path)
            destination_path = os.path.join(downloads_folder, destination_folder, item)  # Include downloads_folder

            # Move the file to its destination folder
            shutil.move(item_path, destination_path)
            print(f"Moved {item} to {destination_folder}")

    # Call the remove_empty_folders function with the source directory
    remove_empty_folders(downloads_folder)

if __name__ == "__main__":
    main()
