There I was, sitting down to enjoy the rather pathetic lunch I had made as an afterthought before leaving the house this morning, leaning over the keyboard munching on a pretty rubbish bagel, when I tried to copy and paste the blog post I had written a minutes previously into a Google+ post.Hrmmf. It didn't work.

I tried two or three times. It didn't work two or three times. I wrote a comment on Google+ about it, wondering what on earth might be wrong.

I have this strange brain, that won't let things go when it knows they are not quite right. I ended up putting the remaining half of the bagel down, and opened a command prompt window. I couldn't ping the domain name. I ran over to cachecheck to see if any servers in the world could see the domain. Oh dear. They could not. It would appear I was seriously offline, all over the world.

Ok. Off to the domain registrar, to see what might be going on. Hmmm. The nameservers pointed at Cloudflare. I had obviously been "being clever". If history records anything about this technological age, it will record that "being clever" is the root cause of most of the world's problems.

I logged into Cloudflare, to see what was going on, and it became immediately apparentthe configuration for the domain was not there. Now I can't remember removing anything (unless I sleepwalk and reconfigure domains while sleepwalking), and I had no email notifications of anybody else hacking in and changing it (CloudFlare are very good at sending those), so it remains a mystery. I have opened a support call, but don't expect to hear anything back.

So. What to do? Given that I didn't actually needCloudFlare, I did the only sensible thingreverted the nameservers back to the registrar, and duplicated the settings. Over the next 24 hours the various domain name servers around the world will propogate the DNS server names, and (hopefully) all will be well again.

People who have read this far will fall into two campsthose that know what I'm talking about, and will be rolling their eyes, thinking "he just can't leave things alone, can he", and those that have no clue, and don't know what they're reading any more. I don't know why I'm writing this either, so they are at least in good company.

PostscriptI just received an email notification that an unknown IP address had logged into my Cloudflare accountI traced it to a server farm in central London. I also changed my password. This is all getting a bit James Bond for me