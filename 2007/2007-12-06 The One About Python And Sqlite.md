This marks the first time I have written a technical post in the blog since I "crossed the streams" (in true Ghostbusters fashion) a little while ago. Many of you will be unaware that I work as a software developer in the daytime, and like many other developers I know, it's more an obsession than a career.

I find complicated things interesting. I like to know how things work. Don't panicI'm not talking "like to know how things work" in the same way that Sylar might in "Heroes"I'm just talking about a fascination in complex/beautiful/clever things. It probably also explains why I like mathematics, and why I dislike slapstick humour.

Soback to the title of this post. While huddled up in the warm at home this evening (after falling asleep at my desk for several hoursI kid you not), a little lightbulb switched on in my head, and I found myself looking at a programming language called Python once again. I have been making furtive glances at it for some time, but have never got any further than writing "hello world" type snippets to try it out.

Tonight I grasped the bull by the horns. I was surprised and delighted. The following snippet of code will have no meaning for the non-developers out there, and I make no apologies for that.

So what does it do? In those few lines of code above, it creates a database, creates a table in that database, stores several records in it, sucks them back out, and then removes them. All achieved in a few lines of code, and with a few meg's worth of installed software (Python 2.5).

If you tried to achieve the above with native Microsoft products, you would be looking at Visual Studio, SQL Server, and the .

NET framework. That adds up to about three gigabytes of your hard drive gone before you even run anything. It would be the equivalent of using a 747 as a supermarket trolley.

Why am I looking at Python then?

Part of my job involves doing migrations from time to timemoving data from one system to another. It strikes me that having a fast interpreted language such as Python, allied with a tiny, fast, and easy to use database such as SQLite would be a killer combination to write ETL (Extract, Transform, Load) tools.

It is perhaps no surprise that the likes of Google and Yahoo like to see developers with Python skills. The above snippet shows just how great it is for prototyping code that might otherwise take hours.