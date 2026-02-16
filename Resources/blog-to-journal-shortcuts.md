# Blog to Apple Journal Migration - Shortcuts Guide

This document contains Apple Shortcuts scripts to migrate your markdown blog entries to Apple Journal.

## Main Shortcut: "Process Blog Year for Journal"

### Setup Instructions:
1. Open the Shortcuts app on your Mac
2. Create a new shortcut called "Process Blog Year for Journal"
3. Copy and paste the actions below (in order):

### Shortcut Actions:

**1. Ask for Input**
- Prompt: "Enter the year to process (e.g., 2025)"
- Input Type: Text
- Variable Name: `YearInput`

**2. Set Variable**
- Variable Name: `BlogPath`
- Value: `/Users/jonbeckett/Projects/blog/[YearInput]`
- (Replace [YearInput] with the magic variable from step 1)

**3. Get Contents of Folder**
- Folder: Use `BlogPath` variable
- Get: Files and Folders

**4. Filter Files**
- Filter: Extension is "md"

**5. Repeat with Each**
- Input: Filtered files from step 4

**6. Get Name of File**
- Input: Current item from Repeat

**7. Split Text**
- Text: File name from step 6
- Split by: " " (space character)
- Variable Name: `FilenameParts`

**8. Get Item from List**
- List: `FilenameParts`
- Item Number: 1 (first item - the date)
- Variable Name: `DateString`

**9. Format Date**
- Date: `DateString`
- Format: Custom
- Custom Format: "EEEE, MMMM d, yyyy"
- Variable Name: `FormattedDate`

**10. Get Text from File**
- File: Current item from Repeat
- Variable Name: `FileContent`

**11. Text**
- Text Content:
```
📝 Blog Entry: [FormattedDate]

[FileContent]

---
Originally written on [DateString]
Migrated from markdown blog archive
```
- Variable Name: `JournalEntry`

**12. Create Journal Entry**
- Title: Use the filename (without .md extension)
- Content: `JournalEntry`
- Date: Use `DateString` if possible, otherwise current date

**13. End Repeat**

**14. Show Notification**
- Title: "Migration Complete"
- Body: "Processed all markdown files for [YearInput]"

## Alternative Shortcut: "Select and Process Blog Entries"

For more selective processing, create this second shortcut:

### Setup:
1. Create new shortcut: "Select and Process Blog Entries" 
2. Add these actions:

**1. Choose from Menu**
- Prompt: "Select processing option"
- Menu Items:
  - "Process Single Month"
  - "Process Specific Files"
  - "Process Year Highlights"

**2. Choose from Menu Action Results:**

### For "Process Single Month":
- Ask for Input: "Year (e.g., 2025)"
- Ask for Input: "Month number (1-12)"
- Get Contents of Folder: `/Users/jonbeckett/Projects/blog/[Year]/[Year]-[Month]*/`
- Continue with filtering and processing as above

### For "Process Specific Files":
- Choose Files (multiple selection enabled)
- Filter for .md files
- Process each selected file

### For "Process Year Highlights":
- Get Contents of Folder for specified year
- Sort files by size (descending) 
- Get first 20-50 items (largest entries)
- Process selected entries

## Helper Shortcut: "Preview Blog Entry"

Create this utility shortcut to preview entries before importing:

**1. Choose Files**
- Allow Multiple: No
- File Types: Markdown

**2. Get Text from File**

**3. Show Text**
- Text: File content
- Title: "Blog Entry Preview"

## Usage Tips:

1. **Start Small**: Test with a single month first
2. **Review Before Import**: Use the preview shortcut to check formatting
3. **Handle Large Batches**: Process in chunks (e.g., quarterly) to avoid timeouts
4. **Backup First**: Ensure your markdown files are backed up
5. **Date Handling**: The script attempts to parse dates from filenames, but may need manual adjustment for some entries

## Customization Options:

- **Filter by File Size**: Add a filter to only process entries above a certain word count
- **Add Tags**: Include tags in Journal entries based on filename patterns or content analysis
- **Custom Formatting**: Modify the text template in step 11 to match your preferences
- **Progress Tracking**: Add notifications after every 10 files processed

## Troubleshooting:

- **Permission Issues**: Ensure Shortcuts has access to your blog folder
- **Date Parsing**: Some entries may not have standard date formats - these will use current date
- **Memory Limits**: Very large years (>200 files) may need to be processed in batches
- **Special Characters**: Some markdown formatting may not transfer perfectly to Journal

## File Structure Expected:

```
blog/
├── 2025/
│   ├── 2025-01 January/
│   │   ├── 2025-01-15 Some Title.md
│   │   └── 2025-01-20 Another Title.md
│   └── 2025-02 February/
│       └── 2025-02-03 Title Here.md
```

The script expects filenames in the format: `YYYY-MM-DD Title.md`