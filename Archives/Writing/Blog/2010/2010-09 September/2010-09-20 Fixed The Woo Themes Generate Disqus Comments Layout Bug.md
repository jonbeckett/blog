Not sure if anybody else has seen this, but if you use the Woo Themes "Generate" theme, the Disqus comments don't work properly in Google Chrome - it wraps the number of comments for a post when the javascript callback from Disqus injects into the page.

The solution is to find the section of each post template that contains the comment count in the footer and add a little CSS (I know this is a horrible way of doing it, but it works).

The code you are looking for will look like this

[

You need to change it to look like this

[

All it does is affords the place the comment count will appear a little space beforehand, and aligns the text to the right of the space we have created.]({Permalink}#disqus_thread)]({Permalink}#disqus_thread)