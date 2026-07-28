I just spent the best part of an hour trying to solve the infamous "Apache Trailing Slash Problem", and then found salvation in an O'Reilly Book excert that I turned up on Google...

Apache Cookbook Excert

The gist of the story is that if you don't set the apache server name, Apache doesn't know how to try and re-write your URLs to append trailing slashes. Hence if you put a URL in without a trailing slash, it tries to redirect to 127.0.0.1 (the default server), and cannot find the path you are looking for - particularly if you have installed aliases and virtual servers...

If you wondering about the geeky entry in my blog, it's for my own reference in the future.