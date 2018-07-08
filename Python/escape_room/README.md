# Escape Room
This fun little game is built mostly off of simple logic patterns.  It does have a few interesting features such as:
* An inventory system that can add and remove objects
* An item dictionary that updates as new items become available
* Dynamic sleep functions that can be removed to 'speed up' the game


As a big fan of escape rooms, I really enjoyed coding this.  Although I initially tried to make it a route, standard, highly structured escape room game, it ended up becoming a parody of all of those features.  The game can be won by doing the standard escape room route...or by other means!

One of the interesting technical things I needed to address came about when I introduced the 'axe'.  The game allowed for objects to be 'found' by searching.  I needed to make the game be able to handle any object being removed without showing up again due to another part of the code allowing that object to be found.  I fixed this by creating a removed_object_list and then making it so nothing from that list could be found again.  It worked out pretty well!
