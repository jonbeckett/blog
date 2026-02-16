I have spent the greater part of today hacking the database behind a corporate document management system to revise the meta-data being held against documents.

It all dates back to a classic IT problem - garbage in, garbage out.

A few years ago I wrote a migration tool to pick up mainframe print spool files and turn them into PDFs that look just like the intended printout (it even lays up a graphic of the headed paper). Alongside the PDF, it creates a text file with the required meta-data (like the customer name, invoice number and so on), and uses that to pump the two files into the document management system...

The problem comes when you look in a particular place on the document - for the Invoice number for example - and the document layout has changed, meaning a different number is there now... you cannot really catch the problem either because you asked for a number, and you got a number.

So - back to today. I have had to write some code to run regular expression searches across all the printouts of a multi-national organisation for the last few years. From the results of those searches I have then written code to write myself several thousand SQL statements to hack the back end of the document management system to put the correct data back in the correct places...

And you wonder why I have headaches so much at the moment... sometimes in this line of work you descend so deep into the stuff you are working on that you lose touch of just how complex that stuff is.

Anyway - I'm going home.