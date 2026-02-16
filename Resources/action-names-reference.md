# 🔍 SHORTCUTS ACTION FINDER

Since action names vary between macOS versions, here are the **actual action names** to search for:

## 📂 File Selection Actions (try these in order):

1. **"Get File"** - Most common on macOS
2. **"Select File"** - Alternative name  
3. **"Choose from Files"** - Another variant
4. **"Get Folder"** - If others don't exist, use this + Get Folder Contents
5. **"File"** - Generic file action

## 📋 Complete Action List with Alternatives:

### Action 1: User Input
- ✅ **"Ask for Input"** (universal)

### Action 2: File Selection  
- ✅ **"Get File"** ← Try this first
- ✅ **"Select File"** ← Try this second  
- ✅ **"Choose from Files"** ← Try this third
- ✅ **"Get Folder"** ← Last resort (then add "Get Folder Contents")

### Action 3: File Filtering
- ✅ **"Filter Files"** (universal)
- Alternative: **"Get Details of Files"** then filter by extension

### Action 4: Loop Processing
- ✅ **"Repeat with Each"** (universal)

### Action 5: File Properties
- ✅ **"Get Name of File"** (universal)
- Alternative: **"Get Details of Files"** → Name

### Action 6: File Contents
- ✅ **"Get Text from File"** (universal)
- Alternative: **"Get Contents of File"**

### Action 7: Text Formatting
- ✅ **"Text"** (universal)

### Action 8: Output
- ✅ **"Copy to Clipboard"** (universal)
- Alternative: **"Set Clipboard"**

### Action 9: Notification
- ✅ **"Show Notification"** (universal)

## 🎯 UPDATED STEP 2:

**Try these in order until you find one that works:**

### Option A: Get File
```
Search: "Get File"
→ Allow Multiple: ON
→ Show: Documents or All Locations
```

### Option B: Select File  
```
Search: "Select File"  
→ Allow Multiple: ON
```

### Option C: Get Folder + Get Folder Contents
```
Search: "Get Folder"
→ Select your blog folder: /Users/jonbeckett/Projects/blog/
Then add: "Get Folder Contents"
→ Include Subfolders: ON
```

## 🔧 If Still Having Issues:

Use this **simpler approach**:

1. **Skip file selection entirely**
2. **Use "Text" action** with hardcoded file paths
3. **Or use the shell scripts** to prepare files first:
   ```bash
   ./select-entries-for-migration.sh
   ./format-for-journal.sh process batch-file.txt
   ```
4. **Then just copy** the pre-formatted content from Utils/formatted-for-journal/

This bypasses the file selection complexity entirely!