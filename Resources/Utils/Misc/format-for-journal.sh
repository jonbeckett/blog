#!/bin/bash

# Blog Entry Formatter for Apple Journal
# Prepares markdown content for optimal Journal import

BLOG_DIR="/Users/jonbeckett/Projects/blog"

# Function to format a single entry
format_entry() {
    local file_path="$1"
    local filename=$(basename "$file_path" .md)
    
    # Extract date from filename (assumes YYYY-MM-DD format at start)
    local date_part=$(echo "$filename" | grep -o '^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}')
    local title_part=$(echo "$filename" | sed "s/^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} //")
    
    # Format date for display
    local formatted_date=""
    if [ -n "$date_part" ]; then
        formatted_date=$(date -j -f "%Y-%m-%d" "$date_part" "+%A, %B %d, %Y" 2>/dev/null || echo "$date_part")
    fi
    
    # Read file content
    local content=$(cat "$file_path")
    
    # Clean up content for Journal
    # Remove multiple empty lines, clean up formatting
    local cleaned_content=$(echo "$content" | sed '/^$/N;/^\n$/d' | sed 's/^[ \t]*//;s/[ \t]*$//')
    
    # Create formatted output
    cat << EOF
📝 $title_part

$formatted_date

$cleaned_content

---
Originally written: $date_part
Migrated from blog archive
Word count: $(echo "$cleaned_content" | wc -w | tr -d ' ')
EOF
}

# Function to process multiple files
process_files() {
    local file_list="$1"
    local output_dir="$BLOG_DIR/Utils/formatted-for-journal"
    
    # Create output directory
    mkdir -p "$output_dir"
    
    echo "🔄 Processing files for Journal format..."
    echo "Output directory: $output_dir"
    echo ""
    
    local count=0
    while IFS= read -r file_path; do
        if [ -f "$file_path" ]; then
            local filename=$(basename "$file_path" .md)
            local output_file="$output_dir/${filename}.txt"
            
            format_entry "$file_path" > "$output_file"
            count=$((count + 1))
            
            echo "✅ Formatted: $filename"
        fi
    done < "$file_list"
    
    echo ""
    echo "🎉 Processed $count entries"
    echo "📁 Formatted files saved to: $output_dir"
    echo ""
    echo "Next steps:"
    echo "1. Open the output directory"
    echo "2. Copy content from .txt files"
    echo "3. Paste into Apple Journal"
}

# Function to create a sample formatted entry
create_sample() {
    local sample_file
    
    # Find a recent entry for sample
    sample_file=$(find "$BLOG_DIR" -name "*.md" | head -1)
    
    if [ -f "$sample_file" ]; then
        echo "📄 Sample formatted entry:"
        echo "=========================="
        echo ""
        format_entry "$sample_file"
        echo ""
        echo "This is how your entries will look when formatted for Journal."
    else
        echo "❌ No sample file found"
    fi
}

# Main script logic
case "$1" in
    "sample")
        create_sample
        ;;
    "process")
        if [ -z "$2" ]; then
            echo "Usage: $0 process <file-list>"
            echo "Where <file-list> is a text file containing paths to markdown files"
            exit 1
        fi
        
        if [ ! -f "$2" ]; then
            echo "❌ File list not found: $2"
            exit 1
        fi
        
        process_files "$2"
        ;;
    *)
        echo "Blog Entry Formatter for Apple Journal"
        echo "====================================="
        echo ""
        echo "Usage:"
        echo "  $0 sample                    # Show a sample formatted entry"
        echo "  $0 process <file-list>       # Process multiple files from a list"
        echo ""
        echo "Examples:"
        echo "  $0 sample"
        echo "  $0 process Utils/migration-batch-2025.txt"
        echo ""
        echo "The file list should contain one file path per line, like:"
        echo "  /Users/jonbeckett/Projects/blog/2025/2025-01 January/2025-01-15 Some Title.md"
        echo ""
        ;;
esac