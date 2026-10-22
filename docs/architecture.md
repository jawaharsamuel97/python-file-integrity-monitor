# FIM Architecture

## Data Flow

```text
       Monitored Files
              |
              v
     Python File Scanner
              |
              v
       SHA-256 Hashing
              |
              v
      Current Hash Map
              |
              v
       Compare Baseline
          /       \
         v         v
   baseline.json  Current Scan
          \       /
           v     v
       Change Detection
              |
              v
       Console Report
```

## Components

1. **Monitored files:** Sample files inside `test_files/`.
2. **File scanner:** Uses Python's `pathlib` to locate files.
3. **SHA-256 hashing:** Uses `hashlib` to calculate file-content hashes.
4. **Baseline storage:** Uses JSON to save reference hashes.
5. **Comparison engine:** Identifies unchanged, modified, added, and deleted files.
6. **Console report:** Displays each file's status and summary counts.

## Design Decisions

- SHA-256 was selected to detect content changes using cryptographic hashes.
- JSON provides a simple, human-readable baseline format.
- Python's standard library avoids external package dependencies.
- The baseline is stored outside the monitored directory to prevent it from being scanned as an ordinary monitored file.

## Security Limitation

The local baseline is not tamper-proof. Production deployments should protect reference hashes using separate permissions or trusted remote storage.
