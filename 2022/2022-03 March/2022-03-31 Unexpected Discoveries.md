Once upon a time I wrote some programming (I'm a software developer in the daytime) to brute-force the problem of finding interesting blogs to read.

I reasoned that if I liked a particular blog, I would probably also like the blogs of people that commented on the blog I liked. So rather than obsessively follow the breadcrumb trail out to every commenter of every post of a given blog, I wrote some programming to do it.

It loads a page you give to it, then finds every page descending directly from it (the posts), and loads them in turn. For each page it has discovered, it looks for any addresses of blogs in the comments (e.g. xyz.wordpress.com) - and compiles a list of them all - before spitting it out as a CSV file that can be perused later.

Here's where the unexpected bit happens.

While doing some spring cleaning on my own Wordpress account yesterday, I started to scratch the "find new and interesting people to read" itch, and pointed the old programming at a somewhat famous blog. After looking through the links for a while, I discovered something really quite strange - that most of the commenters - people who had posted comments very recently - had not written on their own blogs in years.

Rather than wade through the endless stream of inactive blogs, I improved the programming to go visit each blog it discovered, and find out exactly how long it had been since they last wrote. The scale of the discovery was enormous. At least 90% of those that had commented had not written anything themselves for years.

I started scratching my head, and thought "I wonder if there's some way I can improve my program to cast the net wider".

After half an hour of tinkering, I turned the program into a "spider". You can start it out on one blog, and it follows the comments from one blog to another - to a maximum depth noted on a piece of paper in it's pocket. As it clambers through people's blogs, it maintains a list of all the blogs it has discovered along the way that have posted in the last 30 days.

I pointed it at my own blog this morning. It's busy churning through all of the people that have commented on my blog recently, then all the people that have commented on *their *blog, and so on - diving further and further down the rabbit hole. Or jumping from one rabbit hole to the next.

It's still churning now. I imagine Sauron's eye, high atop the Wordpress tower is turning to face me - wondering what I'm doing - wondering why I appear to have been asking to read blogs at several pages a second for the last hour.

Let's hope I don't start talking about the program as "my precious".