
import hashlib
import json
from pathlib import Path

# Directory containing the files we want to monitor
TEST_DIR = Path.home() / "fim-lab" / "test_files"

# Baseline is stored OUTSIDE the monitored directory
BASELINE_FILE = Path.home() / "fim-lab" / "baseline.json"


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def scan_files():
    """Return a dictionary of relative file paths and their hashes."""
    results = {}

    for file_path in sorted(TEST_DIR.rglob("*")):
        if file_path.is_file():
            relative_path = str(file_path.relative_to(TEST_DIR))

            try:
                results[relative_path] = calculate_hash(file_path)
            except OSError as error:
                print(f"ERROR reading {relative_path}: {error}")

    return results


def save_baseline():
    """Save the current file hashes as the baseline."""
    hashes = scan_files()

    with BASELINE_FILE.open("w", encoding="utf-8") as file:
        json.dump(hashes, file, indent=4)

    print(f"Baseline saved: {len(hashes)} file(s)")
    print(f"Location: {BASELINE_FILE}")


def check_integrity():
    """Compare current hashes against the saved baseline."""
    if not BASELINE_FILE.exists():
        print("No baseline found. Create one first.")
        return

    with BASELINE_FILE.open("r", encoding="utf-8") as file:
        baseline = json.load(file)

    current = scan_files()

    unchanged = modified = added = deleted = 0

    for path, old_hash in baseline.items():
        if path not in current:
            print(f"DELETED:   {path}")
            deleted += 1
        elif current[path] != old_hash:
            print(f"MODIFIED:  {path}")
            modified += 1
        else:
            print(f"UNCHANGED: {path}")
            unchanged += 1

    for path in current:
        if path not in baseline:
            print(f"ADDED:     {path}")
            added += 1

    print("\n--- Integrity Summary ---")
    print(f"Unchanged: {unchanged}")
    print(f"Modified:  {modified}")
    print(f"Added:     {added}")
    print(f"Deleted:   {deleted}")


if __name__ == "__main__":
    print("File Integrity Monitoring Tool")
    print("1. Create baseline")
    print("2. Check integrity")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        save_baseline()
    elif choice == "2":
        check_integrity()
    else:
        print("Invalid choice. Enter 1 or 2.")
