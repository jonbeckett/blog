I ordered a Sandisk "Sansa Clip+" MP3 player today, to use instead of my phone to catch up on the various podcasts I try and catch.

The next question therefore, was how best to download the podcasts, manage them, and get them onto the MP3 player. If using Windows, I would have perhaps looked at WinAmp - which will handle the download of podcasts now, but does so in a rather half baked manner. I also looked at GPodder for Linux, which is very, very good - but lacks one feature that I want; it can't delete podcasts older than a certain date.

This is where Linux suddenly defeats Windows - especially if you're not scared of writing a shell script

After configuring podracer (a great open source terminal based podcast downloader), and writing a very small shell script, I have a job that I can run first thing on a morning that does the following;

Downloads all new episodes from the podcasts I specify in the config file

Delete all episodes older than N days

Copy all episodes to the MP3 player

I win 