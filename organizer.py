import argparse
import json
import logging
import pathlib
import shutil
import sys

from tqdm import tqdm

def load_config(config_path: pathlib.Path):
    with open(config_path, 'r') as config_file:
        config_data = json.load(config_file)
    
    return config_data

def process_file(file_path: pathlib.Path, source_directory: pathlib.Path, file_type_map: dict, dry_run: bool):
    file_extension = file_path.suffix
    file_name = file_path.name

    destination_folder = "Other"

    for category, extension in file_type_map.items():
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
            new_filename = f"{file_path.name} ({counter}){file_path.suffix}"
            destination_file_path = destination_dir / new_filename
            counter += 1

        try:

            shutil.move(file_path, destination_file_path)
            logging.info(f"Moved: '{file_path.name}' -> '{destination_file_path}'")

        except PermissionError as e:

            logging.error(f"Could not move {file_name}, Error Occurred = {e}")

        except Exception as e:

            logging.error(f"An unexcepted error occurred during process error = {e}")

def organize_directory(source_directory : pathlib.Path, dry_run : bool, file_type_map: dict):
    
    logging.info(f"Organizing Directory = {source_directory}")

    if dry_run:
        logging.info(" ----DRY RUN MODE ENABLED : no file be moved")
    else:
        logging.warning(" ----LIVE MODE ENABLED : File system changes will be made")

    file_to_process = [item for item in source_directory.iterdir() if item.is_file()]

    for file_path in tqdm(file_to_process, desc="Organizing Files"):
        process_file(file_path, source_directory, file_type_map, dry_run)


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

    config_path_name = pathlib.Path(__file__).parent / "config.json"

    file_type_name = load_config(config_path_name)

    source_path = pathlib.Path(args.source_directory)

    if not source_path.exists() or not source_path.is_dir():
       print("Your source path cannot be oganized as it is not an directory or it is a file.")
       sys.exit(1)
       
    organize_directory(source_path, args.dry_run, file_type_name)