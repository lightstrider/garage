# Escape Room
This fun little game is built mostly off of simple logic patterns.  It does have a few interesting features such as:
* An inventory system that can add and remove objects
* An item dictionary that updates as new items become available
* Dynamic sleep functions that can be removed to 'speed up' the game


As a big fan of escape rooms, I really enjoyed coding this.  Although I initially tried to make it a route, standard, highly structured escape room game, it ended up becoming a parody of all of those features.  The game can be won by doing the standard escape room route...or by other means!

One of the most technical things I needed to deal with was once I had included the axe.  I needed to make it so any object could be removed from the game and then wouldn't show up again due to some other section of the code.  I fixed this by creating a removed_object_list and then making it so nothing from that list could be found again.  It worked out pretty well!
