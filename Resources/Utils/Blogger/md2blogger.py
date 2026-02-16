import sys
import os
import time
import datetime
import re
import html

root_path       = "c:\\Projects\\blog"             # Path to read markdown files from
blog_title      = "Recursive Words"                # Title of Blog
author_name     = "Jonathan"                       # Name to give author of each post
blog_url        = "rcrsvwrds.blogspot.com"
today_date      = "2025-04-06T00:00:00Z"           # Today's date
post_category   = "Life"                           # Default category for each post
output_filename = "c:\\temp\\md2blogger.xml"       # Output filename

def escape_special_chars(text):
    replacements = {
        "“": "&#8220;",
        "”": "&#8221;",
        "‘": "&#8216;",
        "’": "&#8217;",
        "—": "&#8212;",
        "–": "&#8211;",
        # Add more characters and their HTML entities as needed
    }
    pattern = re.compile("|".join(re.escape(key) for key in replacements.keys()))
    return pattern.sub(lambda match: replacements[match.group(0)], html.escape(text))


# Start the XML
xml = ("<?xml version='1.0' encoding='UTF-8'?>\r\n"
    "<feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:gd='http://schemas.google.com/g/2005' xmlns:thr='http://purl.org/syndication/thread/1.0' xmlns:georss='http://www.georss.org/georss'>"
    "<updated>2025-04-08T00:00:00Z</ns0:updated>\r\n"
    "<title type=\"html\">Recursive Words</title>\r\n"
    "<link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='https://rcrsvwrds.blogspot.com/feeds/archive' />\r\n"
    "<link rel='self' type='application/atom+xml' href='https://rcrsvwrds.blogspot.com/feeds/archive' />\r\n"
    "<link rel='http://schemas.google.com/g/2005#post' type='application/atom+xml' href='https://www.blogger.com/feeds/6877794494279152421/archive' />\r\n"
    "<link rel='alternate' type='text/html' href='http://rcrsvwrds.blogspot.com/' />\r\n"
    "<generator version='7.00' uri='https://www.blogger.com'>Blogger</generator>\r\n")

i=0

for subdir, dirs, files in os.walk(root_path):
    for file in files:
        if '.md' in file and '2025' in file and 'README.md' not in file:
            
            print("Processing " + file)
            
            i = i + 1
            
            # Read the file contents
            markdown_file_full_path = os.path.join(subdir, file)
            markdown_file = open(markdown_file_full_path,'r', encoding='utf-8')
            markdown_text = markdown_file.read()
            
            # Extract the date from the filename
            # (so we may use it to back-date the post into write.as)
            year      = file[0:4]
            month     = file[5:7]
            day       = file[8:10]

            date_string = year + "-" + month + "-" + day

            # Extract the title from the filename
            date_length = 10
            first_space_index = date_string.find(" ", date_length)
            post_title = file[first_space_index + 1:]

            post_title_html_escaped = escape_special_chars(post_title)            
            post_body_html_escaped = escape_special_chars(markdown_text)
            
            post_date = year + '-' + month + '-' + day + 'T00:00:00Z'

            xml = xml + '<entry>\r\n'
            xml = xml + "<id>tag:blogger.com,1999:blog-6877794494279152421.post-" + str(i) + "</id>\r\n"
            xml = xml + '<published>' + post_date + '</published>\r\n'
            xml = xml + '<category scheme=\"http://www.blogger.com/atom/ns#\" term=\"' + post_category + '\" />\r\n'
            xml = xml + '<category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/blogger/2008/kind#post" />\r\n'
            xml = xml + "<author><name>' + author_name + '</name><uri>https://www.blogger.com/profile/00996198929462191315</uri><email>noreply@blogger.com</email><gd:image rel='http://schemas.google.com/g/2005#thumbnail' width='32' height='32' src='//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgTLtofhL1D9N-SODNWuydpZpMQauaGFIyX6jhAvXMcIS35SQuKggSDRfYXT4zHrIdwS65n80Te-CFry9sPmq72cE4ZmyvjrPLZ0FhZ6ZxsuF6HXbhMSizDoQ1P5mN-w/s113/f0LbZue9_400x400.jpg' /></author>\r\n"
            xml = xml + '<title type=\"text\">' + post_title_html_escaped + '</title>\r\n'
            xml = xml + '<content type=\"html\">' + post_body_html_escaped + '</content>\r\n'
            xml = xml + '</entry>\n'

# End the XML
xml = xml + "</feed>\r\n"

# Output the XML to a file
post_file = open(output_filename, "w")
post_file.write(xml)
post_file.close()
