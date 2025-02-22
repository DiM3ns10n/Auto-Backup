import argparse
from folder_backup import backup_files

def main():
    """
    Main function to backup files from input folder to output folder
    """
    parser = argparse.ArgumentParser(description="Backup files from input folder to output folder")
    parser.add_argument("input_folder", nargs='?', default=None, help="Folder path of backup")
    parser.add_argument("output_folder",  nargs='?', default=None, help="Folder path to save the backup")
    args = parser.parse_args()  
    
    if not args.input_folder:
        args.input_folder = input("Enter the path to the input folder: ")
    if not args.output_folder:
        args.output_folder = input("Enter the path to the output folder: ")
    
    print(args)
    
    backup_files(args.input_folder, args.output_folder)
    
if __name__ == "__main__":
    main()
    
