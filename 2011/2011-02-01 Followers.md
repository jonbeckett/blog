Somebody asked me the other day how to get the list of followers out of Tumblr - and I shook my head. It's one of the things that's missing from the API, meaning it's more difficult than it should be to achieve.

Unless you're a software developer.

What follows is a "hack" in the true sense of the word. Not a breach of privacy - just a "working of the problem". Here's what I did

Go through each page of my "Followers" in the Tumblr dashboard, view source, and append the output to a text file.

Pass the resulting HTML through an HTML cleanup filter to re-join the anchors and images onto the same line as each other.

Process the resulting text file with a small Python script to extract all the anchors containing avatar images.

Remove all the carriage returns (to ensure the tags flow in the eventual post to Tumblr)

Paste the results into the HTML view of this post (below)

And here's what it resulted in (if you're looking at this in the dashboard, it won't work because the images will show as icons - click the permalink in the corner to see the published post)

<a href="http://serenebabe.tu

mblr.com/">

Danaa! You can click on any of the images. If I had thought about it a little more, I could have made the account names appear when passing the mouse over each image. Maybe another day.

Hopefully when Tumblr start rolling out new functionality in the next few months there will be a heap of new API commands to do things like retrieving the followers.