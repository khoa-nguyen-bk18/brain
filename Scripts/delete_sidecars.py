#!/usr/bin/env python3
import os
from pathlib import Path

def main():
    # Get all .sidecar.md files
    content_dir = Path('.')
    sidecar_files = list(content_dir.glob('**/*.sidecar.md'))
    
    print(f"Found {len(sidecar_files)} sidecar.md files to delete")
    
    # Ask for confirmation
    confirmation = input(f"Are you sure you want to delete {len(sidecar_files)} sidecar.md files? (yes/no): ")
    
    if confirmation.lower() != 'yes':
        print("Operation cancelled.")
        return
    
    # Delete the files
    deleted_count = 0
    for file_path in sidecar_files:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
            deleted_count += 1
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    
    print(f"Successfully deleted {deleted_count} out of {len(sidecar_files)} sidecar.md files")

if __name__ == "__main__":
    main()
