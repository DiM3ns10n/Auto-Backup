## Auto Backup

Auto Backup is a Python script designed to automate file backups efficiently. It organizes backups into a structured folder hierarchy based on the current date and time.

## Folder Structure

```
Backup/
    ├── DD-MM-YY (Current Date)
    │   ├── HH-MM (Current Time)
```

## Installation

1. Clone this repository:
```
    git clone git@github.com:DiM3ns10n/Auto-Backup.git
```

2. Navigate to the project directory:
```
    cd auto-backup
```

3. Run the script:
```
    python main.py
```

## Usage

#### Interactive Mode

Run the script without arguments and follow the prompts to specify the input and output folders:
```
python main.py
```

#### Command-Line Mode

Run the script with folder paths as arguments:

```
python main.py /path/to/input/folder /path/to/output/folder
```
## Features

* Automatically organizes backups by date and time.

* Copies all files while preserving their original names.

* Supports both interactive and command-line usage.

## Functionality

The backup_files function in folder_backup.py follows these steps:

1. Retrieves the current date and time.

2. Creates a nested folder structure based on the date and time.

3. Copies all files from the input folder to the newly created backup directory, prefixing each file with the date and time.

## License

This project is licensed under the MIT License.