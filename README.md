# File Integrity Monitoring Tool Using Python and SHA-256

## Overview

This project implements a basic File Integrity Monitoring (FIM) tool in Python. It calculates SHA-256 hashes of files, saves a baseline, and compares subsequent scans against that baseline to identify changes.

## Features

- Create a baseline of file hashes.
- Detect modified files.
- Detect newly added files.
- Detect deleted files.
- Report unchanged files.
- Store baseline data in JSON format.
- Uses Python standard-library modules only.

## Technologies

- Python 3
- hashlib — SHA-256 hashing
- json — baseline storage
- pathlib — file and directory handling
- Kali Linux — testing environment

## Project Structure

```text
fim-lab/
├── fim.py
├── test_files/
├── docs/
├── screenshots/
├── README.md
└── .gitignore
```

The `baseline.json` file is generated locally when the baseline is created and is excluded from Git.

## Requirements

- Python 3
- A Linux terminal or another environment that supports Python 3

No third-party Python packages are required.

## Setup and Usage

1. Clone or download the project.
2. Open a terminal in the project directory.
3. Create sample files in the monitored directory, or use your own authorized test files.
4. Run:

   `python3 fim.py`

5. Select option `1` to create a baseline.
6. Run the program again and select option `2` to check file integrity.

Example:

```bash
mkdir -p test_files
echo "Sample configuration" > test_files/config.txt
python3 fim.py
```

Create the baseline before changing the test files.

## Detection Logic

- UNCHANGED: the current hash matches the baseline.
- MODIFIED: the file exists in both scans, but its hash differs.
- ADDED: the file is present in the current scan but not in the baseline.
- DELETED: the file was present in the baseline but is missing from the current scan.

## Testing

The following scenarios were manually tested in a local lab:

| Test | Observed result |
|---|---|
| Initial baseline comparison | Two files reported unchanged |
| Modify `config.txt` | Modification detected |
| Add `newfile.txt` | Addition detected |
| Delete `app.log` | Deletion detected |

These results reflect the observed lab tests.

## Limitations

- This is an educational prototype, not a production security monitoring platform.
- The baseline is stored locally and is not tamper-proof.
- A user who can alter both the monitored files and the baseline may be able to conceal changes.
- The tool reports changes but does not identify who made them.
- Permission errors and changes during scanning can affect results.
- It does not provide real-time monitoring; scans are initiated manually.

## Security and Authorization

Use the tool only on files and systems you own or are authorized to monitor. Do not commit confidential files, sensitive logs, or private information.

## Future Improvements

- Protect the baseline with stricter access controls.
- Add timestamped logs and report export.
- Add automated periodic scans.
- Improve error handling for unreadable files and invalid baseline data.
- Add automated unit tests.

## Author

Jawahar
