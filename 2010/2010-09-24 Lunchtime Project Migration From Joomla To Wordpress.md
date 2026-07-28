I have been helping somebody move their blog from Joomla to WordPress over the last couple of days. The final "big" thing to do was move their old posts and comments in.

WordPress has a handy migration plugin thatfor the most partdid what was required of it. It didn't migrate the comments though

Here's the SQL that did the job for me;

INSERT INTO wordpress.wp_comments (comment_post_ID, comment_author, comment_author_email, comment_author_url, comment_date, comment_date_gmt, comment_content)SELECT wpp.

ID, c.name, c.email, c.website, c.date, c.date, c.commentFROM joomla.jos_jomcomment cINNER JOIN joomla.jos_content p ON c.contentid=p.idINNER JOIN wordpress.wp_posts wpp ON wpp.post_title = p.title

which was fine except none of the post comment counts got updated. Hence this command to force them to behave;

UPDATE wp_posts SET comment_count = SELECT COUNT(wp_comments.id) FROM wp_comments WHERE wp_comments.post_id = wp_posts.id

And before you start, I knowthe code takes no notice of published status, or anything like that