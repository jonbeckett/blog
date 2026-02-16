I jumped down a rabbit hole of my own making today. Before describing the rabbit hole expedition however, it's probably worth filling in some back story.

I've been writing on the old Apple Mac for the last several weeks - sitting in the corner of the study at an old desk, with an angle-poise lamp, and a whirring heap of plastic and glass that appeared on billboards above the freeway through California in the late 1990s. There's something delightfully eccentric, reactionary, and anachronistic about using the Mac. It weighs more than the desk it sits on. Across the room, a Raspberry Pi sits on an adjacent desk - it's more powerful than the Mac, and yet weighs less than a small bar of chocolate.

While writing all manner of forgettable words into the Mac, an elephant has been sitting in the middle of the junk room. An elephant wearing a hat with a padlock on it. About a year ago the SSL standard began to change on the internet - the mechanism through which online services prove their veracity. Overnight, the Mac could no longer communicate with any secure services on the internet that had upgraded. Over days and weeks the internet slowly went dark.

And then I had an idea.

Before I can get to the idea I need to explain something else too though (I'm not a very good story teller, am I). For years and years, I have written blog posts in a plain text format called "Markdown", and then copied them into wherever I was publishing the blog. I have over four thousand text files, split into month and year folders - and saved in a "Git" repository on the internet.

If you're a fellow blogger, but not a software developer, you're probably thinking "what the hell is Git?". Git is the system invented by Linus Torvalds - the original creator of Linux - to store programming source code. Think of it as a database for files, that keeps versions for you. It comes into it's own when working in teams - you can each have a copy of everything you have all written, and push and pull changes between each other. I use Git to store the text of my blog posts, and push them up to a freebie account on the internet as a nerdy sort of backup.

The thing about Git - and this was my lightbulb moment - is that it's decentralised. Say you have the backup of your writing on a Git server on the internet (mine is at GitLab - you've probably heard of GitHub) - if you want a copy of it on your computer, you can tell Git to clone your writing to your computer. When you finish writing, you can push the words you have written back to the internet.

And there's the problem I needed to solve - it's all locked down with the padlocks that no longer work on the Mac - so the Mac can't push any words I write back up to the internet. BUT THE RASPBERRY PI CAN.

Therefore - bear with me - I cloned the backup to the Raspberry Pi, and then from the Mac cloned the backup from the Raspberry Pi to the Mac. The Mac can get away with it, because it doesn't need SSL (the padlock) to communicate with the Raspberry Pi.

What does this all mean? It means I can write on the Mac, push the words to the Raspberry Pi, and then tell the Pi to push the words up to the internet for me. If an auditor was reading this, they would start nodding - because I've unwittingly done an on-site backup, as well as an off-site backup. What does that mean? It means if the internet connection dies we have a copy here - and if the copy here dies, we have a copy on the internet.

If you made it this far, well done 

You're probably wondering what Git gives you that saving text files into a folder does not. Well... you don't actually SEE anything - it's just a folder full of your text files. You can ask Git questions about your files though - like "how is this text different than it was when I saved it two weeks ago" - complete with a full breakdown of the words, sentences, and paragraphs that have moved, changed, been added, or removed.

If you were working on some sort of experimental piece of writing, you could tell git to "branch" what you have saved - giving yourself the writing equivalent of a multi-verse - where you can suddenly work on several versions of the same file if you so wish, and then merge them back together in the future too.

It's all a bit mad, a bit abstract, but very useful too. I've often wondered how many writers use Git. I imagine I might be the only one - if you can class me as a "writer". I'm writing words - that makes me a writer, doesn't it ?