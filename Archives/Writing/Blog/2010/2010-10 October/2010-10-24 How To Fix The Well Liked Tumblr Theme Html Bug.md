If you've noticed the "Well Liked" theme layout breaks sometimes, I saw it happen again this morning, and decided to find out what was wrong with it.

After saving the source of the rendered page out to a text file, I stripped it back until I found out what was going wrong it's the question and answer section (as I suspected) - it's using an LI tag to output questions, but not wrapping it in a UL tag.

If you're using the "Well Liked" theme, find the HTML that looks like this;

{block:Answer}

 * {Asker}:{Question}

{Answer}

{/block:Answer}

and change it to look like this

{block:Answer}

 * {Asker}:{Question}

{Answer}

{/block:Answer}