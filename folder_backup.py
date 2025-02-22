import os
import shutil
from datetime import datetime

def backup_files(input_folder, output_folder):
    """
    Backup files from input folder to output folder with date and time prefix
    Args:
        input_folder (str): Path to the input folder
        output_folder (str): Path to the output folder
    """
    # Get current date and time
    date_str = datetime.now().strftime('%Y-%m-%d')
    time_str = datetime.now().strftime('%H-%M')
    
    # Define backup directory paths
    dir1_path = os.path.join(output_folder, date_str)
    dir2_path = os.path.join(dir1_path, time_str)
    
    # Create directories if they don't exist
    os.makedirs(dir2_path, exist_ok=True)
    
    # Copy all files from input folder to dir2_path with date and time pref ix
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            new_filename = f"{date_str}_{time_str}_{filename}"
            shutil.copy(file_path, os.path.join(dir2_path, new_filename))
    
    print(f"Backup completed successfully at {dir2_path}")

