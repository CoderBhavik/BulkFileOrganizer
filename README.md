# Bulk File Organizer

An CLI based app which can be used for organizing your directories with multiple files like Images, documents, zip etc.

## Features

* **Automatic folder creation** : Folders with name like Images or Documents will be created automatically even if they are not exists.
* **Dry Run Mode** : Dry run mode to see which file will be moved to which folder without moving any file.
* **Comprehensive Logging** : A detailed 'organizer.log' file created to see every important information about error, warnings etc.
* **Intelligent confilt resolution** : Automatically handles FileExistError if any file with same name exists in subdirectories on time of organizing without any problem.
* **Progress bar** : An user-friendly progress bar which shows real time progress on console.

## Installation
1. Clone the Repository

git clone https://github.com/CoderBhavik/BulkFileOrganizer.git

cd BulkFileOrganizer

2. Create a Virtual Environment (Recommended):

    **Windows**

    python -m venv .venv
    .venv\Scripts\activate

    **macOS / Linux**

    python3 -m venv .venv
    source .venv/bin/activate

3. Install the Required Dependencies:
    * pip install -r requirements.txt

# Usage

Run the application using : 
* **FOR LIVE MODE** : python organizer.py your_directory_name
* **FOR DRY RUN MODE** : python organizer.py your_directory_name --dry-run

# Technologies Used

* python 3.12.10
* Logging
* JSON
* Pathlib
* tqdm

# Author

**Bhavik Suthar**

Github : https://github.com/CoderBhavik

