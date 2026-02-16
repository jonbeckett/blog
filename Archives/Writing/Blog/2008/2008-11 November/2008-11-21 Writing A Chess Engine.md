Every few years, I find myself returning to a project I have had kicking around since leaving college - writing a "chess engine". For those who are casual readers of my blog, it might be worth explaining what a "chess engine" is.

A chess engine is a computer program that can play chess. Simple. The term "engine" is used because it doesn't attempt to draw a nice looking board on the screen and let you slide pieces around - it will typically require typed moves such as "e2e4", and respond with something like "e7e5" (the coordinates of the squares on the chess board, if you were wondering).

I don't really have a hobby, and I have been warned by people far more clever than myself over the years to stay away from writing a chess program - purely because they know the territory and have war stories to tell.

Chess has been perhaps the most interesting computer science problem for decades - and certainly the most researched. Most people are aware of projects such as "Deep Thought", and "Deep Blue" at IBM - the projects that defeated Garry Kasparov in a series of high profile matches. It's unique appeal to computer science lies in the apparent simplicity, and yet unfathomably complex nature of the problem to solve.

As soon as you start thinking about how to make a machine play chess, you come across a well worn term - "combinatorial explosion". If you try to work out the possible future moves in a game of chess, you quickly end up with more possibilities than there are atoms estimated in several universes. The problem therefore becomes one of applying human intelligence to help the machine appear to think.

"Appear to think" is a good term to us. Computers can't think - well, not yet anyway. They can however add stuff up incredibly quickly, and remember lots of small things perfectly. Here lies the problem for teaching a machine to play a game. Do you spend all your time getting the machine to calculate myriad rules, evaluations and comparisons to approximate "judgement", or do you build a very fast idiot (try every move rather than trying to decide on one).

The clever route towards making a good chess engine - and the one that has occupied brainy people for decades - is in finding cheap ways to make a fast idiot more selective.

You start to read research papers about "rotated bit boards", and "pruning algorithms". One of the pieces of research that came out of the IBM projects involved selective deepening of their high speed idiot's vision - kind of like teaching it to hedge it's bets ("this looks so promising, I'm going to spend more time than I should checking this particular idea out"). The idea won important awards from people who give awards to brainy people.

So here I am. Thinking about writing my chess engine again. I have written up the ideas from my head several times over the years - and got 50% of the way towards a working implementation in C once. At the same time as interesting me, it also scares me.

I've read "A Beautiful Mind". I know what happened to John Forbes Nash Jr. Perhaps the fact that I'm no genius will save me from his fate.