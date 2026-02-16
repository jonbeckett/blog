import sys
import os
import datetime
import re
import unicodedata
import html
from rake_nltk import Metric,Rake

source_path = "c:\\projects\\blog"
output_path = "c:\\projects\\blogmd"

r = Rake()



def slugify(text):
    
    # 1. Normalize the string to remove accents and other diacritics
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('windows-1252')

    # 2. Remove characters that are not alphanumeric, underscores, or hyphens
    text = re.sub(r'[^\w\s-]', '', text.lower())

    # 3. Replace whitespace with hyphens
    text = re.sub(r'\s+', '-', text).strip()

    # 4. Remove multiple consecutive hyphens
    text = re.sub(r'-+', '-', text)

    return text

def escape_special_chars(text):
    replacements = {
        "“": "\"",
        "”": "\"",
        "‘": "'",
        "’": "'",
        "—": "-",
        "–": "-",
        # Add more characters and their HTML entities as needed
    }
    pattern = re.compile("|".join(re.escape(key) for key in replacements.keys()))
    return pattern.sub(lambda match: replacements[match.group(0)], html.escape(text))

def remove_comment_lines(text):
  lines = text.splitlines()
  filtered_lines = [line for line in lines if not line.strip().startswith('#')]
  return "\n".join(filtered_lines)


for subdir, dirs, files in os.walk(source_path):
    for file in files:
        if '.md' in file and 'README' not in file:
            
            print("Processing " + file)
            
            # Read the file contents
            source_file_path = os.path.join(subdir, file)
            source_file = open(source_file_path,'r', encoding='utf-8', errors='ignore')
            post_text = source_file.read()
            source_file.close()
            
            # Extract the date from the filename
            # (so we may use it to back-date the post into write.as)
            year      = file[0:4]
            month     = file[5:7]
            day       = file[8:10]
            post_date = year + '-' + month + '-' + day + ' 00:00:00';

            # Extract the title from the filename            
            post_title = file[11:len(file)-3]
                        
            # generate a publish date in the appropriate format - e.g. Mon, 20 Jan 2020 00:00:00 +0000
            pubdate = datetime.datetime(int(year), int(month), int(day))
            pubdate_formatted = pubdate.strftime("%a %d %b %Y %H:%M:%S")

            # replace special chars in post text
            post_text = escape_special_chars(post_text);

            # unescape any special characters
            post_text = html.unescape(post_text)

            # remove any lines beginning with a slash in post text
            post_text = remove_comment_lines(post_text);

            # replace any instances of multiple blank lines with single blank lines
            post_text = re.sub(r'\n\s*\n+', '\n\n', post_text)

            # replace any instances of leading blank lines
            post_text = re.sub(r'^\n\s*\n+', '', post_text)

            # work out the categories!
            r.extract_keywords_from_text(post_text)
    
            # ranked_phrases_with_scores = r.get_ranked_phrases_with_scores()
            phrases = r.get_ranked_phrases()[:5]
            #for score, phrase in ranked_phrases_with_scores:
            #    print(f"Score: {score:.3f}, Phrase: {phrase}")
            print(phrases)

            # append frontmatter to the post text
            post_text_fm = "---\ntitle: " + post_title + "\ndate: " + year + "-" + month + "-" + day + "\ncategories: [life]\ntags: [life]\nauthor: Jonathan Beckett\n---\n\n" + post_text

            # create a year folder if needed
            post_parent_path = os.path.join(output_path,year)
            if not os.path.exists(post_parent_path):
                os.makedirs(post_parent_path)
                print("Creating Parent Path for " + year)
            
            # create a month folder within the year folder if needed
            post_child_path = os.path.join(output_path,year,year + "-" + month)
            if not os.path.exists(post_child_path):
                os.makedirs(post_child_path)
                print("Creating Child Path for " + year + "-" + month)

            # create the output filename
            output_filename = os.path.join(post_child_path,year + "-" + month + "-" + day + "-" + slugify(post_title) + ".md")

            # write the output file
            #output_file = open(output_filename, "w", encoding='utf-8', errors='ignore')
            #output_file.write(post_text_fm)
            #output_file.close()
            
            #output_file = open(source_file_path,"w", encoding='utf-8', errors='ignore')
            #output_file.write(post_text)
            #output_file.close()

