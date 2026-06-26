import pathlib
import argparse
import sys

FILE_TYPE_NAME = {
    "Images" : ['.jpeg', '.png', '.jpg', '.gif', '.webp', '.avif', '.raw', '.bmp', '.tif', '.tiff', '.svg', '.psd', '.ico'],
    "Videos" : ['.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.rrc', '.gifv', '.mng', '.mov', '.avi', '.qt', '.wmv', '.yuv', '.rm', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', '.mod'],
    "Audio" : ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.aiff'],
    "Documents" : ['.pdf', '.txt', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx'],
    "Archives" : ['.zip', '.rar', '.tar', '.gz'],
    "Programming_Files" : ['.py', '.htm', '.c', '.cpp', '.js', '.java', '.css'],
    "Executable_Files" : ['.exe', '.app', '.bin'],
    "Others" : []
}

def organize_directory(source_directory : pathlib.Path):
    
    print("Organizing Directory = ", source_directory)

    for item in source_directory.iterdir():
        
        if item.is_file():
            file_extension = item.suffix
            file_name = item.name

            print(f"File found = {file_name}, Extension = {file_extension}")
        

if "__main__" == __name__:

    parser = argparse.ArgumentParser(description="Organizer")
    parser.add_argument("source_directory", help="Main directory name you want to organize.")
    args = parser.parse_args()

    source_path = pathlib.Path(args.source_directory)

    if not source_path.exists() or not source_path.is_dir():
       print("Your source path cannot be oganized as it is not an directory or it is a file.")
       sys.exit(1)
       
    organize_directory(source_path)