I tried to make one change to the theme, and it completely randomized the configuration of the colours and various constants within the theme.

I know why too.

There is a bug in the code that sets custom properties of themes - if you change the contents of the HTML, it saves the custom properties (the Appearance tab) in alphabetical order versus the index order of their appearance in the theme source code - meaning the wrong things get saved in the wrong fields behind the scenes.

Mayhem ensues.

If anybody knows a Tumblr developer, please, please, please tell them to sort it out.