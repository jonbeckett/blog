import sys
import os
import time
import datetime
import re
import html
import unicodedata
import json
import uuid
import zipfile
from collections import defaultdict

# Configuration
root_path = "c:\\Projects\\blog"                            # Path to read markdown files from
output_path = "c:\\Projects\\blog\\Utils\\dayone_exports"   # Path to output Day One JSON files
timezone = "America/New_York"                                # Timezone for Day One entries
default_tags = ["blog", "imported"]                         # Default tags for imported entries
entry_time = "12:00:00"                                     # Default time for entries (noon)

# Create output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Dictionary to store entries grouped by year
entries_by_year = defaultdict(list)
processed_count = 0
error_count = 0

def create_dayone_entry(markdown_text, post_title, post_date, creation_date):
    """Create a Day One entry dictionary from markdown content"""
    
    # Generate a unique UUID for this entry
    entry_uuid = str(uuid.uuid4()).upper()
    
    # Parse the date string to create proper timestamps
    # Day One expects dates in UTC, so we need to be explicit about timezone
    
    # Parse the blog post date
    date_obj = datetime.datetime.strptime(post_date, '%Y-%m-%d %H:%M:%S')
    # Treat the date as if it's in the specified timezone, then convert to UTC
    date_obj = date_obj.replace(tzinfo=datetime.timezone.utc)
    
    # Parse the import date (current time)
    creation_date_obj = datetime.datetime.strptime(creation_date, '%Y-%m-%d %H:%M:%S')
    creation_date_obj = creation_date_obj.replace(tzinfo=datetime.timezone.utc)
    
    # Convert to Day One's expected date format (ISO 8601 with Z suffix)
    # Use the blog post date as the entry date in Day One
    entry_timestamp = date_obj.strftime('%Y-%m-%dT%H:%M:%SZ')
    # Use current time as modified date (when the import was done)
    modified_timestamp = creation_date_obj.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Clean up the title (replace underscores with spaces, etc.)
    clean_title = post_title.replace('_', ' ').replace('-', ' ').title()
    
    # Process markdown text - add title as header if not already present
    processed_text = markdown_text
    if not processed_text.strip().startswith('#'):
        processed_text = f"# {clean_title}\n\n{processed_text}"
    
    # Format the text to ensure proper paragraph spacing
    # Split by lines and add blank lines between paragraphs
    lines = processed_text.split('\n')
    formatted_lines = []
    
    for i, line in enumerate(lines):
        formatted_lines.append(line)
        
        # Add blank line after non-empty lines if the next line is also non-empty
        # This creates proper paragraph separation
        if (line.strip() and 
            i < len(lines) - 1 and 
            lines[i + 1].strip() and 
            not line.strip().startswith('#') and 
            not lines[i + 1].strip().startswith('#')):
            # Don't add blank line if one already exists
            if i < len(lines) - 2 and not lines[i + 1].strip():
                continue
            formatted_lines.append('')
    
    processed_text = '\n'.join(formatted_lines)
    
    # Create the Day One entry structure
    entry = {
        "uuid": entry_uuid,
        "text": processed_text,
        "creationDate": entry_timestamp,  # Use blog post date
        "modifiedDate": modified_timestamp,  # Use import date
        "timeZone": timezone,
        "starred": False,
        "tags": default_tags.copy(),  # Use configured tags
        "weather": {},
        "location": {}
    }
    
    return entry

def save_dayone_export(year, entries):
    """Save entries for a given year to a Day One JSON file and create a zip archive"""
    
    # Create the Day One export structure
    dayone_export = {
        "metadata": {
            "version": "1.0"
        },
        "entries": entries
    }
    
    # Save to file
    filename = f"dayone_export_{year}.json"
    filepath = os.path.join(output_path, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(dayone_export, f, indent=2, ensure_ascii=False)
    
    # Create a zip file containing the JSON
    zip_filename = f"dayone_export_{year}.zip"
    zip_filepath = os.path.join(output_path, zip_filename)
    
    with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(filepath, filename)  # Add JSON file to zip with just the filename (no path)
    
    # Get file sizes for reporting
    json_size = os.path.getsize(filepath)
    zip_size = os.path.getsize(zip_filepath)
    compression_ratio = (1 - zip_size / json_size) * 100
    
    print(f"Created Day One export: {filename} ({json_size:,} bytes)")
    print(f"Created zip archive: {zip_filename} ({zip_size:,} bytes, {compression_ratio:.1f}% compression)")
    print(f"  Contains {len(entries)} entries")

# Process all markdown files
print(f"Scanning for markdown files in: {root_path}")
print("=" * 50)

for subdir, dirs, files in os.walk(root_path):
    for file in files:
        # Look for markdown files with date format YYYY-MM-DD
        if '.md' in file and re.match(r'\d{4}-\d{2}-\d{2}', file) and 'readme' not in file.lower():
            
            print(f"Processing {file}")
            
            # Read the file contents
            markdown_file_full_path = os.path.join(subdir, file)
            try:
                with open(markdown_file_full_path, 'r', encoding='utf-8') as markdown_file:
                    markdown_text = markdown_file.read()
                    
                if not markdown_text.strip():
                    print(f"  Warning: {file} is empty, skipping")
                    continue
                    
            except Exception as e:
                print(f"  Error reading {file}: {e}")
                error_count += 1
                continue
                        
            # Extract the date from the filename
            try:
                year = file[0:4]
                month = file[5:7]
                day = file[8:10]
                
                # Validate date components
                datetime.datetime(int(year), int(month), int(day))
                
                post_date = f"{year}-{month}-{day} {entry_time}"
                
            except (ValueError, IndexError) as e:
                print(f"  Error parsing date from {file}: {e}")
                error_count += 1
                continue
            
            # Use current time as creation date (when imported)
            creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Extract the title from the filename            
            try:
                post_title = file[11:len(file)-3]
                if not post_title:
                    post_title = f"Entry {year}-{month}-{day}"
            except IndexError:
                post_title = f"Entry {year}-{month}-{day}"
            
            # Create Day One entry
            try:
                entry = create_dayone_entry(markdown_text, post_title, post_date, creation_date)
                # Add to the appropriate year group
                entries_by_year[year].append(entry)
                processed_count += 1
                print(f"  ✓ Added to {year} export")
                
            except Exception as e:
                print(f"  Error creating entry for {file}: {e}")
                error_count += 1
                continue

print("\n" + "=" * 50)
print("PROCESSING SUMMARY")
print("=" * 50)

# Save one file per year
for year, entries in entries_by_year.items():
    save_dayone_export(year, entries)

print(f"\nProcessing complete!")
print(f"✓ Processed {processed_count} markdown files")
if error_count > 0:
    print(f"⚠ Encountered {error_count} errors")
print(f"✓ Generated {len(entries_by_year)} Day One JSON export files")
print(f"✓ Created {len(entries_by_year)} compressed ZIP archives")
print(f"✓ Files saved to: {output_path}")

# Show breakdown by year
print(f"\nBreakdown by year:")
for year in sorted(entries_by_year.keys()):
    print(f"  {year}: {len(entries_by_year[year])} entries")

print(f"\nTo import into Day One:")
print("1. Open Day One app")
print("2. Go to File -> Import -> JSON")
print("3. Select the generated ZIP files (Day One can import directly from ZIP)")
print("4. Day One will preserve the original dates from your blog posts")
print("5. The ZIP files are smaller and easier to manage than individual JSON files")

