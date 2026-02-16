I debated about writing this in a different place on the internet, but seeing as this blog has become a drop box for anything and everything that enters my head and exits via my fingers, I thought "what the hell".

I tripped over something in programming today while wrestling with an insanely complex problemsomething I have seen before, and something I should have remembered. I remember thinking the same last time I came across it too.

Here goes feel free to stop reading if you're not (a) a software developer, or (b) studying to be a software developer.

When you write a C# program, you often write classes, and create objects that are based on those classes. Sometimes you will want to make a copy of an existing object. There's a gotcha involved though.

Example code

public class Starship

{

public string Captain = "";

}

// we'll make a starship

Starship enterprise = new Starship();

enterprise.

Captain = "Kirk";

// and then we'll make another one based on the first

Starship excelsior = enterprise;

excelsior.

Caption = "Sulu";

The catch here is that now "enterprise" captain is also Sulu. Even after being a developer for over 10 years now, I still forget that objects are always referred by referenceonly scope of methods they are passed into will interfere with that.

What I should have done is implemented a "Clone" method on the Starship class that specifically made a new one, and returned it.

Example

public class Starship

{

public string Captain = "";

public object Clone()

{

Starship result = new Starship();

result.

Captain = this.

Captain;

return result;

}

}

// and the calling code

Starship enterprise = new Starship();

enterprise.

Captain = "Kirk";

// now make the clone

Starship excelsior = (Starship)enterprise.

Clone();

excelsior.

Captain = "Sulu";

Implementing a clone method makes sure we do exactly what we intended to do. It turns out that the .

NET "ICloneable" interface is really nasty too, because it performs a "shallow copy" by defaultmeaning any deep data structures within an object being cloned continue to be copied by reference unless you are very carefulbut the syntax to do that is a bigger subject than I want to get into right now.

Apparently there are discussions under way to drop "ICloneable" from the .

NET framework. After seeing the results of it's default implementation today, I can understand why.