#!/usr/bin/env python3
import os
import re
from pathlib import Path

def update_draft_to_publish(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if file has "draft: true"
        if "draft: true" in content:
            # Replace "draft: true" with "publish: true"
            updated_content = content.replace("draft: true", "publish: true")
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            print(f"Updated {file_path}: draft: true -> publish: true")
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    # Get all .md files
    content_dir = Path('.')
    md_files = []
    
    for file_path in content_dir.glob('**/*.md'):
        md_files.append(file_path)
    
    print(f"Found {len(md_files)} .md files to check")
    
    updated_count = 0
    for file_path in md_files:
        if update_draft_to_publish(file_path):
            updated_count += 1
    
    print(f"Updated {updated_count} files with draft: true -> publish: true")

if __name__ == "__main__":
    main()
