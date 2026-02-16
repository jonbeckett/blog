While working on a project this week, it occurred to me how many different skills you need these days as a commercial software developer. I guess if you work in a big enough company (read: Facebook, or Google), you would be able to concetrate on one or two core skills, but meI have to bridge the whole damn lot.

I thought it might be interesting to look at the layers involved in a project I have been working on recently.

First of all you need "consultancy skills" in order to talk to a client, and figure out what they are really trying to do. Part of this is people skills, but perhaps the bigger part is knowing the feature set of the technology you have available, best practices in the use of those features, and perhaps most importantlyknowing what is difficult, and what is easy.

Once you start building anything you're going to need to know about one of the popular version control systems in order to back-up your code. I've always wondered why version control isn't used by writers, because it's a perfect fit for textual content. If you wondering what on earth I'm talking about, version control systems allow you to make changes to things, and keep track of the changes, so you can see exactly what chunk of code fixed a bug, or which change coincided with a bug appearing.

I guess next we get onto the systems side of things. Most web applications run on servers, so you're going to need to know about either constructing and running a virtual server, or connecting remotely to a client system across the internet. If you're building a virtual server, you're going to need to know how to install the operating system, and whatever platform you're building on top of (in my case, SharePoint most recently).

Here's where it get's interesting. Let's take SharePoint as an exampleit's actually a whole stack of products working in concertWindows Server, SQL Server, IIS, .

NET, and SharePoint itself. While you don't have to knoweverythingabout instaling and configuring all those products, you need to know enough to at least find your way around the file-system, create databases, fiddle with user permissions, and so on.

If we are going to talk about SharePoint itself, you're suddenly talking about a vast product with training courses that go on for weeks, and very thick books about specific aspects of the system. You're going to need to have the same kind of knowledge a "system architect" would havein that you know how to configure the foundations of a new area in the system, and all the best practices around doing that. Going beyond a "power user", you're going to need to be able to write PowerShell scripts to automate the creation and deployment of assets within the environment.

To build out solutions you're going to need to know Microsoft Visual Studio (their integrated development environment) inside out. You'll need to know about signing assemblies, packaging, features, and all sorts of other things that colleges likely don't teach at all. Once you get down to writing compiled source code, you enter the "real" world of the software developerwhere code can have a style, and you can make the difference between a product being bloated,slow, and fragile, or being fast, efficient, and reliable.

Given that most software these days ends up delivering content to a browser from the server (as does SharePoint), the code you write won't only be compiled server-side code. You're going to need to know everything involved in constructing the pages in browser, and the mechanics of how that happensHTML, CSS, and Javascript. Beyond the code script kiddies write in their bedrooms, you will often need to write server side code that generates HTML, CSS, and Javascript on-the-fly a system that builds a system.

Of course then there is the issue of the infrastructure between the server(s) and the browser(s)you'll need to know the rudiments of network infrastructure, and securityin order to troubleshoot if nothing else.

It starts to look like a very long (and wide) list, doesn't it. Multiple programming languages, multiple products, multiple operating systems, multiple markup languages all done in order that you can sit at your desk at work, and complain about it.