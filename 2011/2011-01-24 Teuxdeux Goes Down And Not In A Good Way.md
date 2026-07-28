Over the last week or so, I've been playing with an online task management tool called TeuxDeux. Since I got in to work this morning, their website has been reporting 502 errors. These are not good errors.

Perhaps some explanation of a 502 might be helpful;

A server (not necessarily a Web server) is acting as a gateway or proxy to fulfil the request by the client (e.g. your Web browser or our CheckUpDown robot) to access the requested URL. This server received an invalid response from an upstream server it accessed to fulfil the request.

In laymans terms, it means TeuxDeux has a classic webserver farm - with front end servers designed to deal with requests from users, and back end servers doing the data crunching. A 502 error means the back end servers have stopped making any sense to the front end servers, and they're telling you as much.

Tumblr does exactly the same thing; except they have a custom 502 page that tells you they're really, really sorry.

I'm guessing this is going to hurt TeuxDeux quite a bit; when Tumblr goes down, we all get back on with our work when TeuxDeux goes down, a lot of people have no idea what work they had been meaning to do.