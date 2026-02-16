I was looking at my Tumblr stats in Google Analytics the other evening, and wondered why they are so poor - why very little traffic finds it's way to my tumblog from web searches (in comparison to wordpress, for example).

Here's what you need to do;

Replace the tag in your theme with this {block:PostSummary}{PostSummary} - {/block:PostSummary}{Title}

Put the following meta tags in the head of your theme HTML

Register your tumblog with Google Webmaster Tools - to add the sitemap use the following URLs http://yoursite.tumblr.com/sitemap-pages.xml http://yoursite.tumblr.com/sitemap1.xml

The above steps will essentially help Google understand what is in your pages better (by making the page titles, descriptions, and tags contextually accurate), and instruct Google exactly which pages to index via the sitemaps.