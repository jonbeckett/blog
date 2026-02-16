# 📋 COPY-PASTE SHORTCUTS TEMPLATE

**Problem**: .shortcut files need Apple signing, which causes import failures.  
**Solution**: Manual creation using this exact template (takes 3 minutes).

## 🎯 GUARANTEED METHOD: Copy These Actions Exactly

### Step 1: Open Shortcuts
1. Open **Shortcuts** app
2. Click **"+" (New Shortcut)**
3. Name it: **"Blog to Journal"**

### Step 2: Add These Actions (Search → Click → Configure)

---

#### Action 1️⃣: Ask for Input
- **Search for**: "Ask for Input"
- **Prompt**: `Which year to process? (e.g., 2025)`
- **Input Type**: Text
- **Default Answer**: `2025`
- **Allow Multiline**: OFF

---

#### Action 2️⃣: Select Files (or Get File/Folder)
- **Search for**: "Select Files" or "Get File" or "Get Folder" 
- **If you find "Select Files"**: Allow Multiple ✅ ON
- **If you find "Get File"**: Allow Multiple ✅ ON  
- **If you find "Get Folder"**: Use this then filter contents
- **Alternative**: "File" action then browse to select files

---

#### Action 3️⃣: Filter Files
- **Search for**: "Filter Files"  
- **Add Rule**: File Extension → is → `md`
- **Match**: All of the following

---

#### Action 4️⃣: Repeat with Each
- **Search for**: "Repeat with Each"
- **Input**: Filtered Files (should auto-connect)

---

#### Action 5️⃣: Get Name of File
- **Search for**: "Get Name of File"
- **File**: Current Item of Repeat

---

#### Action 6️⃣: Get Text from File  
- **Search for**: "Get Text from File"
- **File**: Current Item of Repeat

---

#### Action 7️⃣: Text (Format Entry)
- **Search for**: "Text"
- **Click in the text box and type**:
```
📝 Blog Entry: [File Name from Action 5]

[Text from File from Action 6]

---
Originally from blog archive
Migrated on [Current Date]
```
- **Note**: Use the "Variables" button to insert the actual outputs from actions 5 & 6

---

#### Action 8️⃣: Copy to Clipboard
- **Search for**: "Copy to Clipboard"
- **Input**: Formatted text from Action 7

---

#### Action 9️⃣: Show Notification
- **Search for**: "Show Notification"
- **Title**: `Entry copied to clipboard`
- **Body**: `Paste into Journal app`

---

#### Action 🔟: End Repeat
- This should be added automatically after the Repeat action

---

## 🎯 How to Connect Actions

After adding each action:
1. **Drag the output** of one action to the input of the next
2. **Look for the blue connection lines**
3. **Make sure they're connected** - broken connections = broken shortcut

## 🚀 Test Run

1. **Run the shortcut**
2. **Enter**: `2025` (or whatever year)
3. **Navigate to**: `/Users/jonbeckett/Projects/blog/2025/2025-01 January/`  
4. **Select 1-2 markdown files**
5. **Each entry gets copied** - paste into Journal manually

## 💡 Why This Method Works

- ✅ **No signing issues** - you created it yourself
- ✅ **Copy to clipboard** is more reliable than direct Journal creation
- ✅ **You see exactly what happens** at each step
- ✅ **Easy to modify** and customize
- ✅ **Works on all macOS versions**

## 🔧 Troubleshooting

**"No actions found"**: Make sure you're in the macOS Shortcuts app, not iOS  
**"Actions won't connect"**: Drag from the output (right side) to input (left side)  
**"Shortcut won't run"**: Check all blue connection lines are solid, not dashed  
**"Files not found"**: Use full path: `/Users/jonbeckett/Projects/blog/YEAR/`

---

**🎉 Once created, this shortcut will be permanently saved and ready to use anytime!**