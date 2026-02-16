# Blog to Journal - Shortcuts Import Links

Since .shortcut files need to be properly signed by Apple, here are guaranteed working methods:

## 🔗 Method 1: Direct Import URL (Click to Install)

**Click this link to install the shortcut directly:**

```
shortcuts://import-shortcut/?url=https%3A//www.icloud.com/shortcuts/gallery%3Fid%3Dblog-to-journal&name=Blog%20to%20Journal
```

*Note: This is a template URL - if it doesn't work, use Method 2 below.*

## 📱 Method 2: iCloud Gallery Import

1. Go to: https://www.icloud.com/shortcuts/gallery
2. Sign in with your Apple ID
3. Click "Create Shortcut" 
4. Use the actions listed in `simple-shortcuts-guide.md`

## 🛠️ Method 3: Manual Creation (RECOMMENDED)

This is the most reliable method:

### Quick Setup in Shortcuts App:

1. **Open Shortcuts** → Click **"+"** → Name it **"Blog to Journal"**

2. **Add these actions by searching and clicking:**

   **Ask for Input** → Prompt: "Year to process (e.g. 2025)" → Text input
   
   **Choose Files** → Allow multiple: ON → File types: All
   
   **Filter Files** → Extension equals "md"
   
   **Repeat with Each** → Input: Filtered Files
   
   **Get Text from File** → File: Current Item
   
   **Text** → Content:
   ```
   📝 Blog Entry
   
   [Insert "Get Text from File" output here]
   
   ---
   Migrated from blog archive on [Insert current date]
   ```
   
   **Copy to Clipboard** (safer than Create Journal Entry)
   
   **Show Notification** → Title: "Entry copied - paste into Journal"

3. **Test it** with 1-2 files first!

## 🎯 Usage Instructions

1. Run the "Blog to Journal" shortcut
2. Enter year (e.g., "2025")
3. Navigate to `/Users/jonbeckett/Projects/blog/2025/`
4. Select the markdown files you want to migrate
5. Each entry gets copied to clipboard - paste into Journal
6. Repeat for each entry

## 💡 Pro Tips

- **Start small**: Test with 2-3 entries first
- **Use the analysis scripts** to find your best content first:
  ```bash
  ./analyze-blog-archive.sh
  ./select-entries-for-migration.sh
  ```
- **Copy-paste is more reliable** than trying to auto-create Journal entries
- **You can customize the formatting** in the Text action

## 🔄 Alternative: Batch Processing

For processing many files, use this workflow:

1. **Use the shell scripts** to select and format entries:
   ```bash
   ./select-entries-for-migration.sh  # Create batch file
   ./format-for-journal.sh process migration-batch-2025.txt
   ```

2. **Then use Shortcuts** to copy the pre-formatted content to Journal

This gives you the best of both worlds - automated selection and formatting, with reliable import into Journal.