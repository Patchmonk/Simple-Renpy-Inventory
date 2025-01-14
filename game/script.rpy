# Some default background images
image Grassland = "Grassland.png"
image Grassland 2 = "Grassland_2.png"
image Forest = "Forest.png"

image ss1 = "ss1.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

default inventory = []
default gold = 100
# The game starts here.

label start:
    show Grassland
    # Introduction: A Simple Inventory System for Your Game

    "Hey there! Welcome to my simple inventory demo project."
    "DI cooked up this project with the goal of diving deep into the world of Ren'Py. You know what sparked the idea for this neat inventory system? It was none other than iceorfire.com."
    "Their tutorial got me all hyped up, so I put my own twist on it and polished it and added some new feature while maintaining the simplicity of the original project."
    "My goal is to craft an inventory system that's simple yet powerful, a system that could be seamlessly woven into any simple game."

    "I've kept things refreshingly uncomplicated here, relying on a trusty list for our inventory. Add or remove items, and you're set! No convoluted class-based shenanigans to worry about."
    "I firmly believe that simpler code equals fewer errors. It's a fantastic starting point, especially if you're new to the coding game. You can build upon this foundation and and make it even better."

    "Improve the existing inventory and customize it to your specific needs would be a great starting point."

    "Now, even though I had a boatload of awesome ideas to elevate this simple inventory system, I chose to stick to the basics. I Split the project into two flavors of inventory: we've got the simple system we're enjoying right now, and there's also an advanced version."
    "The one we're using is beginner-friendly and smooth as butter. If you're feeling adventurous and want to explore the advanced side, check out my Git repository or swing by my itch.io profile."

    "But enough chit-chat about the inventory system. Let's witness this baby in action."
    "Today, we're whipping up a slick heads-up display and a snazzy backpack image button that'll whisk us away to the inventory screen."

    show screen HUD
    show ss1
    "Awesome! Look at that snazzy heads-up display and the backpack icon. I bet you're already a pro at this, right? 😄"
    "Give that backpack icon a click!" 
    "Hmm, we've got ourselves an empty inventory. And let's be real, an empty inventory is no party. Time to spice things up!"
    "$ inventory.append('Banana') + adding all other item variables"
    
   
   
    $ inventory.append("Banana")
    $ inventory.append("Broccoli")
    $ inventory.append("Cabbage")
    $ inventory.append("Pear")
    $ inventory.append("Pepper")
    $ inventory.append("Potato")
    $ inventory.append("Pumpkin")
    $ inventory.append("Lemon")

    
    "Ta-da! Behold, the magic of Super basic inventory 😄" 
    "Yay! Our inventory is now overflowing with goodies. And guess what? Adding your own items or creating unique icon images is a breeze."
    "Just pop a few of your custom inventory PNG icons in the 'images/inventory' folder and use the add item code provided. It's that easy!"
    "We currently have 21 available slots in our demo inventory, If you want to reward your players and add more slots to the inventory to store more items."
    "You can easily add as many slots as you'd like by simply editing the slot variable. it's simple and flexible, so feel free to customize it and make it your own!"


    "And here's a neat trick, if you happen to throw in more than 21 slots, our current inventory version automatically springs into action with a dynamic scroll bar. How cool is that? The nitty-gritty details are in the screen code."

    "But hey, that's only the beginning. We've mastered the art of adding items. Let's switch gears and delve into the equally exciting world of removing items."
    "For instance, I'm not a huge fan of lemons, so..."

    $ inventory.remove("Lemon")
    "$ inventory.remove('Lemon')"
    "Poof! The 'Lemon' vanished into thin air. Feel free to toss out or snag items as you please. I trust your judgment. no need for me to spell that out!"

    "So, that's the lowdown on the basics of our simple inventory system. You've got the power to add and subtract items like a pro."

    "Think about it isn't that a solid set of features for a basic inventory system? Unless I'm having a brain freeze, I think we've covered all the essentials."

    "Hold on a sec! I almost skipped over the crown jewel of our simple inventory system, the ability to peek inside and see what's hiding in those virtual pockets."

    "Because let's be real, an inventory system is only as exciting as your ability to check its contents and build decision-making magic around it."

    "Ready to rock? Let's flip the page to a fresh label and dive right into mastering this pivotal feature."


    jump Forest
    # This ends the game.

    return
label Forest:
    show Forest
    "Alright, let's put our newfound inventory wisdom to the test in this lush forest setting."
    "Imagine you're designing a game, and your player is wandering through a forest when, out of the blue, they stumble upon a valuable item – an 'Apple'! That's a score!"
    $ inventory.append("Apple")

    "Now we have added this mystery apple to our inventory"
    "This is where your game design skills shine. You've given your player a life-changing reward that's sure to make their gaming experience better."
    "Not only did they receive it from the benevolent forest goddess, but they've also earned some extra love points. It's like hitting three birds with one stone!"

    "Now, let's get back to the tutorial. In simple terms, here's what we're doing: we're checking if your inventory contains a specific item. If it does, something special will happen in your game."

    if "Apple" in inventory:
        "You're nailing this game design thing! The apple is safely tucked in their inventory, and your player is in for a treat."
        "Now let's add 1000 gold and a mystical compass. Trust me; it'll come in handy!"
        $ gold += 1000
        $ inventory.append("Compass")
        "Take a quick look at the inventory in the HUD screen."
    else:
        "Oops, it seems the apple slipped away this time. No worries, we've got a backup plan."
        "Behold, a fish! Think of it as a consolation prize. But next time, don't forget to stock up on those apples."
        $ inventory.append('Fish')

    hide Forest

    jump End

return

label End:
    show Grassland2
    "Thanks for diving into my project with enthusiasm."
    "Want to dive deeper into game development? Explore my advanced inventory system and other cool projects on my Git repository or itch.io profile."
    "Thanks for checking out the simple inventory system demo."
    "And don't forget, if you liked the graphics assets in this demo, be sure to give credit to the amazing authors. You'll find the links in the script.rpy file and the GitHub repository readme."
    "Wishing you a fantastic day!"
   
return
 