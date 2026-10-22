# File Integrity Monitoring — Test Report

## Environment

- Operating system: Kali Linux
- Python: 3.14.7
- Hash algorithm: SHA-256
- Test method: Manual, controlled file changes in a local lab

## Test Results

| Test | Action | Observed result | Status |
|---|---|---|---|
| 1 | Create baseline from two files | Both files reported unchanged on the next scan | PASS |
| 2 | Append text to `config.txt` | File reported as modified | PASS |
| 3 | Create `newfile.txt` after baseline creation | File reported as added | PASS |
| 4 | Delete `app.log` after baseline creation | File reported as deleted | PASS |

## Observations

The tool correctly compared current SHA-256 hashes with the saved baseline and detected the tested modification, addition, and deletion scenarios.

During the final scan, the tool reported:
- Unchanged: 0
- Modified: 1
- Added: 1
- Deleted: 1

These counts matched the deliberate test changes.

## Limitations

- Testing covered a small set of sample files.
- The baseline is stored locally and is not tamper-proof.
- The tool does not identify the person or process responsible for a change.
- Automated testing, larger file sets, unreadable files, corrupted baselines, and concurrent file changes have not yet been fully tested.

## Conclusion

The prototype successfully demonstrated baseline creation and detection of file modifications, additions, and deletions in a controlled local environment. Further validation and security hardening are required before production use.
