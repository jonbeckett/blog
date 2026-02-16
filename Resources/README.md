# Blog to Apple Journal Migration Toolkit

This toolkit provides comprehensive tools for migrating your markdown blog entries to Apple Journal. The toolkit includes both Apple Shortcuts automation and command-line utilities.

## 📁 Files in this Toolkit

### 1. **blog-to-journal-shortcuts.md**
Complete Apple Shortcuts instructions for automated processing. This is the main migration tool that can process an entire year of entries at once.

### 2. **analyze-blog-archive.sh** 
Analysis script that provides statistics about your blog archive:
- Total entries per year
- Word count statistics  
- Identifies substantial entries (200+ words)
- Recommends entries for migration

### 3. **select-entries-for-migration.sh**
Interactive script for choosing which entries to migrate:
- Find longest entries
- Browse by year/month
- Find recent entries
- Create batch files for processing
- Preview entries before migration

### 4. **format-for-journal.sh**
Prepares markdown content for optimal Journal import:
- Cleans up formatting
- Adds metadata (date, word count)
- Creates Journal-friendly text files
- Processes batch files

## 🚀 Quick Start Guide

### Step 1: Analyze Your Archive
```bash
cd /Users/jonbeckett/Projects/blog/Utils
./analyze-blog-archive.sh
```
This shows you overview statistics and helps plan your migration.

### Step 2: Select Entries to Migrate
```bash
./select-entries-for-migration.sh
```
Use this interactive tool to:
- Browse your entries
- Create a batch file of selected entries
- Preview content before migration

### Step 3: Format Entries for Journal
```bash
# Create sample to see formatting
./format-for-journal.sh sample

# Process a batch file
./format-for-journal.sh process migration-batch-2025.txt
```

### Step 4: Use Apple Shortcuts
Follow the instructions in `blog-to-journal-shortcuts.md` to create the Shortcuts automation that will actually import the entries into Journal.

## 💡 Recommended Migration Strategy

### For Your 6,000+ Entry Archive:

1. **Don't migrate everything** - Focus on quality over quantity
2. **Start with recent years** - 2020-2025 entries are most relevant
3. **Filter by length** - Entries with 200+ words work best in Journal
4. **Process in batches** - Do one month or quarter at a time
5. **Create highlights** - Maybe 50-100 best entries total

### Sample Workflow:
```bash
# 1. Get overview
./analyze-blog-archive.sh

# 2. Select entries interactively
./select-entries-for-migration.sh
# Choose option 5 to create a batch file for 2025

# 3. Format the selected entries
./format-for-journal.sh process migration-batch-2025.txt

# 4. Use Shortcuts to import formatted entries
# (Follow blog-to-journal-shortcuts.md instructions)
```

## 🛠️ Advanced Usage

### Creating Custom Batch Files
You can create your own file lists:
```bash
# Find all entries with 300+ words from 2024-2025
find /Users/jonbeckett/Projects/blog/202[4-5] -name "*.md" -exec bash -c '
    word_count=$(wc -w < "$1")
    if [ $word_count -ge 300 ]; then
        echo "$1"
    fi
' _ {} \; > custom-batch.txt
```

### Filtering by Content
```bash
# Find entries containing specific words
grep -l "writing\|author\|book" /Users/jonbeckett/Projects/blog/2025/*/*.md > writing-related.txt
```

### Year-Specific Processing
```bash
# Process just 2025 entries over 200 words
find /Users/jonbeckett/Projects/blog/2025 -name "*.md" -exec bash -c '
    word_count=$(wc -w < "$1")
    if [ $word_count -ge 200 ]; then echo "$1"; fi
' _ {} \; | head -50 > best-of-2025.txt

./format-for-journal.sh process best-of-2025.txt
```

## 📊 Expected Results

Based on your archive analysis:
- **Total entries**: 6,040
- **Recommended for migration**: 100-200 substantial entries
- **Processing time**: ~5 minutes per batch of 50 entries
- **Journal storage**: Much more manageable and searchable

## 🔧 Troubleshooting

### Common Issues:
1. **Permission errors**: Ensure scripts are executable (`chmod +x *.sh`)
2. **Date parsing**: Some old entries may not have standard date formats
3. **Large batches**: Process in chunks of 50-100 entries to avoid timeouts
4. **Special characters**: Some markdown formatting may need manual adjustment

### Script Dependencies:
- macOS (uses BSD date command)
- Bash shell
- Standard Unix tools (find, wc, grep, sed)

## 📝 Notes

- Keep your original markdown files as the master archive
- The formatted files are created in `Utils/formatted-for-journal/`
- Each script has help text (run without arguments)
- Test with small batches before processing large amounts

## 🎯 Next Steps

1. Run the analysis script to understand your archive
2. Use the selection script to identify your best content  
3. Create the Apple Shortcuts as described in the guide
4. Start with a small test batch (maybe 10-20 entries)
5. Refine your process based on results
6. Process your selected content in manageable chunks

This toolkit gives you complete control over the migration process while automating the tedious parts. Good luck with your migration!