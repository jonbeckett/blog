I just discovered a workaround for the extremely annoying bug in the Tumblr theme "custom property" feature.

Here's what the API documentation tells you;

By including the special meta-text tags in your theme, users can easily configure text variables you define. This is useful for adjusting text or configuring widgets that require information from the user.

They go on to give you an HTML example (you can see it here)

The thing they don't tell you is the variables you setup for the custom properties have to be listed in the header in alphabetical order - otherwise, rather randomly, Tumblr will write them back into the text boxes in the "Customize" menu in the wrong order jumbling up the data hilariously.

Hopefully this will be useful to somebody else some day when they're pulling their hair out, wondering what on earth is going on.