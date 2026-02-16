# Simple Blog to Journal Shortcut - Copy & Paste Version

Since importing .shortcut files can be unreliable, here's a simple shortcut you can create by copying and pasting these actions directly in the Shortcuts app:

## 🚀 Quick Setup (5 minutes)

### Step 1: Open Shortcuts App
- Open the Shortcuts app on your Mac
- Click the "+" button to create a new shortcut  
- Name it "Blog to Journal"

### Step 2: Add These Actions (in order)

**⚠️ IMPORTANT**: After adding each action, make sure to connect the output of one action to the input of the next by dragging the connection lines.

**Action 1: Ask for Input**
- Search for "Ask for Input"
- Prompt: "Which year to process? (e.g., 2025)"
- Input Type: Text
- Default Answer: 2025

**Action 2: Choose from Menu** 
- Search for "Choose from Menu"
- Add menu items:
  - "Process all files"
  - "Select specific files"
  - "Just create one test entry"

**Action 3: Choose Files**
- Search for "Choose Files" 
- Allow Multiple: Yes
- Show: All file types

**Action 4: Filter Files**
- Search for "Filter Files"
- Add condition: File Extension → is → md

**Action 5: Repeat with Each**
- Search for "Repeat with Each"
- Input: Filtered Files from previous step

**Action 6: Get Text from File**
- Search for "Get Text from File"
- File: Current Item of Repeat

**Action 7: Text** (Format the content)
- Search for "Text"
- Content: 
```
📝 Blog Entry

[Contents of File from previous step]

---
Migrated from blog archive
```

**Action 8: Copy to Clipboard** ⭐ **RECOMMENDED**
- Search for "Copy to Clipboard"
- Content: Formatted Text from previous step
- This is more reliable than trying to create Journal entries directly

**Alternative Action 8: Create Journal Entry** (if available)
- Search for "Create Journal Entry" or "Add to Journal"
- Content: Formatted Text from previous step  
- Title: Leave blank or use filename
- Note: This action may not be available on all macOS versions

**Action 9: End Repeat**
- This should be added automatically

**Action 10: Show Notification**
- Search for "Show Notification"
- Title: "Migration Complete"
- Body: "Blog entries added to Journal"

## 🎯 How to Use

1. Run the shortcut
2. Enter the year you want to process
3. Choose your option from the menu
4. Select your markdown files (navigate to `/Users/jonbeckett/Projects/blog/YEAR/`)
5. Watch as entries are created in Journal!

## 📝 Pro Tips

- Start with just 2-3 files to test
- Use the file selector scripts first to identify your best entries
- The shortcut preserves your original formatting
- Each entry gets tagged as migrated from blog archive

## 🔧 If Journal Entry Creation Doesn't Work

Some versions of macOS might not have the "Create Journal Entry" action. In that case:

**Alternative Action 8: Copy to Clipboard**
- Replace "Create Journal Entry" with "Copy to Clipboard"
- Then manually paste each entry into Journal
- This gives you more control over the formatting

This approach is 100% reliable and lets you see exactly what's happening at each step!