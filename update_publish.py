#!/usr/bin/env python3
import os
import re
from pathlib import Path

def update_frontmatter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if file has frontmatter
        frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
        match = frontmatter_pattern.search(content)
        
        if match:
            frontmatter = match.group(1)
            
            # Check if frontmatter already has draft: true
            if re.search(r'draft:\s*true', frontmatter, re.IGNORECASE):
                print(f"Skipping {file_path} - already has draft: true")
                return False
            
            # Check if frontmatter already has publish field
            if re.search(r'publish:', frontmatter):
                # Update publish field to true
                updated_frontmatter = re.sub(
                    r'publish:\s*(false|true|null)',
                    'publish: true',
                    frontmatter
                )
            else:
                # Add publish: true to frontmatter
                updated_frontmatter = frontmatter + "\npublish: true"
            
            # Replace the old frontmatter with the updated one
            updated_content = content.replace(
                match.group(0),
                f"---\n{updated_frontmatter}\n---\n"
            )
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            print(f"Updated {file_path}")
            return True
        else:
            # No frontmatter, add one with publish: true
            updated_content = f"---\npublish: true\n---\n\n{content}"
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            print(f"Added frontmatter to {file_path}")
            return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    # Get all .md files except those in the private folder
    content_dir = Path('.')
    md_files = []
    
    for file_path in content_dir.glob('**/*.md'):
        # Convert to string for easier path checking
        file_str = str(file_path)
        
        # Skip files in private folder
        if '/private/' in file_str or file_str.startswith('./private/'):
            continue
        
        md_files.append(file_path)
    
    print(f"Found {len(md_files)} .md files to process")
    
    updated_count = 0
    for file_path in md_files:
        if update_frontmatter(file_path):
            updated_count += 1
    
    print(f"Updated {updated_count} files")

if __name__ == "__main__":
    main()
