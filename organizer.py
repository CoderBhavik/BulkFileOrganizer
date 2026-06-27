import argparse
import logging
import pathlib
import shutil
import sys

FILE_TYPE_NAME = {
    "Images" : ['.jpeg', '.png', '.jpg', '.gif', '.webp', '.avif', '.raw', '.bmp', '.tif', '.tiff', '.svg', '.psd', '.ico'],
    "Videos" : ['.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.rrc', '.gifv', '.mng', '.mov', '.avi', '.qt', '.wmv', '.yuv', '.rm', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', '.mod'],
    "Audio" : ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.aiff'],
    "Documents" : ['.pdf', '.txt', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.csv'],
    "Archives" : ['.zip', '.rar', '.tar', '.gz'],
    "Programming_Files" : ['.py', '.htm', '.c', '.cpp', '.js', '.java', '.css', '.ipynb'],
    "Executable_Files" : ['.exe', '.app', '.bin', '.msi', '.jar'],
    "Others" : []
}

def organize_directory(source_directory : pathlib.Path):
    
    logging.info(f"Organizing Directory = {source_directory}")

    for item in source_directory.iterdir():
        
        if item.is_file():
            file_extension = item.suffix
            file_name = item.name


            destination_folder = "Other"

            for category, extension in FILE_TYPE_NAME.items():

                if file_extension in extension:

                    destination_folder = category
                    break
            
            destination_dir = source_directory / destination_folder

            destination_dir.mkdir(parents=True, exist_ok=True)

            destination_file_path = destination_dir / file_name
            
            try:
                shutil.move(item, destination_file_path)
                logging.info(f"Moved: '{item.name}' -> '{destination_file_path}'")
            
            except (FileExistsError, PermissionError) as e:
                logging.error(f"Could not move {file_name}, Error Occured = {e}")


if "__main__" == __name__:

    parser = argparse.ArgumentParser(description="Organizer")
    parser.add_argument("source_directory", help="Main directory name you want to organize.")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("organizer.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    source_path = pathlib.Path(args.source_directory)

    if not source_path.exists() or not source_path.is_dir():
       print("Your source path cannot be oganized as it is not an directory or it is a file.")
       sys.exit(1)
       
    organize_directory(source_path)