# Some default background images
image Grassland = "Grassland.png"
image Grassland 2 = "Grassland_2.png"
image Forest = "Forest.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

default inventory = []
default gold = 0
# The game starts here.

label start:
    show Grassland
    "Hey there! Welcome to my simple inventory demo project."
    "I cooked up this project with the goal of diving deep into the world of Ren'Py. You know what sparked the idea for this neat inventory system? It was none other than iceorfire.com."
    "Their tutorial got me all hyped up, so I put my own twist on it and polished it and added some new feature while maintaining the simplicity of the original project."
    "My goal is to craft an inventory system that's simple yet powerful, a system that could be seamlessly woven into any simple game."

    "I've kept things refreshingly uncomplicated here, relying on a trusty Dictionary for our inventory. Add or remove items, and you're set! No convoluted class-based shenanigans to worry about."
    "I firmly believe that simpler code equals fewer errors. It's a fantastic starting point, especially if you're new to the coding game. You can build upon this foundation and and make it even better."

    "Improve the existing inventory and customize it to your specific needs would be a great starting point."

    "Now, even though I had a boatload of awesome ideas to elevate this simple inventory system, I chose to stick to the basics. I Split the project into two flavors of inventory: we've got the simple system we're enjoying right now, and there's also an advanced version."
    "The one we're using is beginner-friendly and smooth as butter. If you're feeling adventurous and want to explore the advanced side, check out my Git repository or swing by my itch.io profile."

    "But enough chit-chat about the inventory system. Let's witness this baby in action."
    "Today, we're whipping up a slick heads-up display and a snazzy backpack image button that'll whisk us away to the inventory screen."

    show screen HUD
    "Awesome! Look at that snazzy heads-up display and the backpack icon. I bet you're already a pro at this, right? 😄"
    "Give that backpack icon a click!" 
    "Hmm, we've got ourselves an empty inventory. And let's be real, an empty inventory is no party. Time to spice things up!"
    "$ inventory.append('Apple') + adding all other variables"
    
   
    $ inventory.append("Lemon")
    $ inventory.append("Banana")
    $ inventory.append("Broccoli")
    $ inventory.append("Cabbage")
    $ inventory.append("Pear")
    $ inventory.append("Pepper")
    $ inventory.append("Potato")
    $ inventory.append("Pumpkin")

    
    "Ta-da! Behold, the magic of Super basic inventory 😄"
    "Boom! We've now got a treasure trove of items filling up our inventory. Don't worry if it looks a bit snug; you can always treat your players and toss in more slots manually."
    "And here's a neat trick: if you happen to throw in more than 21 slots, our current inventory version automatically springs into action with a dynamic scroll bar. How cool is that? The nitty-gritty details are in the screen code."

    "But hey, that's only the beginning. We've mastered the art of adding items. Let's switch gears and delve into the equally exciting world of removing items."
    "For instance, I'm not a huge fan of lemons, so..."

    $ inventory.remove("Lemon")
    "$ inventory.remove('Lemon')"
    "Poof! The 'Lemon' vanished into thin air. Feel free to toss out or snag items as you please. I trust your judgment – no need for me to spell that out!"

    "So, that's the lowdown on the basics of our simple inventory system. You've got the power to add and subtract items like a pro."

    "Think about it – isn't that a solid set of features for a basic inventory system? Unless I'm having a brain freeze, I think we've covered all the essentials."

    "Hold on a sec! I almost skipped over the crown jewel of our simple inventory system – the ability to peek inside and see what's hiding in those virtual pockets."

    "Because let's be real, an inventory system is only as exciting as your ability to check its contents and build decision-making magic around it."

    "Ready to rock? Let's flip the page to a fresh label and dive right into mastering this pivotal feature."


    jump Forest
    # This ends the game.

    return

label Forest:
    show Forest
    "Alright, let's put our newfound inventory wisdom to the test amidst the lush forest setting."
    "Picture this: you're wandering through the trees when suddenly you stumble upon something. An 'Apple'! Score!"
    $ inventory.append("Apple")
    "Time to work some code magic. We're about to determine if that juicy 'Apple' is snuggled up in your inventory. Brace yourself!"
    "The example code's chilling in the demo script.rpy file, ready for its moment in the spotlight."
 
        
    if "Apple" in inventory:
        "You're a legend! An apple is indeed chillin' in your inventory, and you're in for a treat."
        "As a token of appreciation, I'm sliding 1000 gold your way along with a mystical compass. My gut says it'll come in handy!"
        $ gold += 1000
        $ inventory.append("Compass")
        "Oh, and do a quick check of your inventory and the HUD screen – who knows what treasures you might find!"
    else:
        "Uh-oh, it seems the apple eludes your grasp. Don't fret! I've got your back with a little something else."
        "Behold, a fish! Consider it a consolation prize. But hey, next time, don't forget to pack those apples."
        $ inventory.append('fish')
    
    hide Forest
    jump End

return

label End:
    show Grassland 2  
    "Hey there, big thanks for diving into my project with such enthusiasm."
    "Hungry for more knowledge? Feel free to explore my advanced inventory system and other cool projects on my git repository or itch.io profile."
    "Thanks for checking out the simple inventory system demo."
    "By the way, if the graphics assets caught your eye in this demo, remember to give credit to the amazing authors. Links are hiding in script.rpy and the GitHub repository readme file."
    "Wishing you a fantastic day!"
   
return
# Graphics resources
# https://www.pixiv.net/en/users/12597768
# https://arcsine-technologies.itch.io/veggie-pack-volume-i

