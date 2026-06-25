import pathlib
import argparse

if "__main__" == __name__:

    parser = argparse.ArgumentParser(description="Organizer")

    parser.add_argument("source_directory", help="Main directory name you want to organize.")

    args = parser.parse_args()

    print(args.source_directory)