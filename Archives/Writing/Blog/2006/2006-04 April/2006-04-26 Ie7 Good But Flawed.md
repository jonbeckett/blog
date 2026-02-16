You may not know that Microsoft released beta 2 of Internet Explorer 7 last month. I've been trying it out and was initially impressed - however I've just had to remove it and revert to IE6. It has at least two major flaws that (for a web developer) mean I cannot use it.

The first flaw I found seemed to be in the rendering of cascading style sheets and tables. If you put a div tag inside a table cell, IE still doesn't calculate the relative sizes correctly - you end up with the contents of table cells overlapping the table. This used to happen in IE and cause divs inside tables to overlap to the right. They appear to have hacked about with it now - the right hand side stays in - at the expense of the left side hanging out. I can't say I'm impressed with the IE rendering engine at all.

The second flaw was (potentially) more serious...

I have been working on a tabbing system recently - it's all client side, and uses Javascript to build tabs, remove tabs, and so on. The contents of the page related to the tabs is held within div tags who's style is either set to "block" or "none" - which should make them appear and dissappear as tabs are clicked upon... only it's not reliable.

It would appear that IE7 does not react to DHTML style changes reliably - especially when they are causing entire sections of the page to appear and dissappear. I spent the greater part of yesterday afternoon thinking it was my code causing the problems - then rolled back to IE6 as a last resort. Problem solved.

This is pretty much a killer blow in terms of using IE7 for rich web interface development. If anybody else has seen any funnies with IE7 I'd like to know...