import argparse
import logging
import pathlib
import shutil
import sys

from tqdm import tqdm

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

def organize_directory(source_directory : pathlib.Path, dry_run : bool):
    
    logging.info(f"Organizing Directory = {source_directory}")

    if dry_run:
        logging.info("[DRY RUN MODE ENABLED] no file be moved")

    file_to_process = [item for item in source_directory.iterdir() if item.is_file()]

    for item in tqdm(file_to_process, desc="Organizing Files"):
        
        file_extension = item.suffix
        file_name = item.name

        destination_folder = "Other"

        for category, extension in FILE_TYPE_NAME.items():
            if file_extension in extension:
                destination_folder = category
                break
        
        destination_dir = source_directory / destination_folder

        # If Dry_run is true, we do nothing for now. and our task will be to add logging report to intended here
        if dry_run:
            destination_file_path = destination_dir / file_name

            logging.info(f"[DRY RUN] Would move '{file_name}' --> '{destination_file_path}'")
        else:
            # Else we will do our task as organizer
            destination_dir.mkdir(parents=True, exist_ok=True)

            destination_file_path = destination_dir / file_name
            counter = 1

            while destination_file_path.exists():
                logging.warning(f"Conflict : {destination_file_path} already exist")

                new_filename = f"{item.name} ({counter}){item.suffix}"

                destination_file_path = destination_dir / new_filename

                counter += 1

            try:
                shutil.move(item, destination_file_path)

                logging.info(f"Moved: '{item.name}' -> '{destination_file_path}'")

            except PermissionError as e:

                logging.error(f"Could not move {file_name}, Error Occurred = {e}")

            except Exception as e:
                logging.error(f"An unexcepted error occurred during process error = {e}")


if "__main__" == __name__:

    parser = argparse.ArgumentParser(description="Organizer")
    parser.add_argument("source_directory", help="Main directory name you want to organize.")
    parser.add_argument("--dry-run", action='store_true', help="Simulate organization without moving any files")
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
       
    organize_directory(source_path, args.dry_run)