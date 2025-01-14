# Some default background images
image Grassland = "Grassland.png"
image Grassland 2 = "Grassland_2.png"
image Forest = "Forest.png"
image backpack_arrow = "backpack arrow.png"
image Screenshot_1 = "Screenshot_1.png"
image Screenshot_2 = "Screenshot_2.png"
image Screenshot_3 = "Screenshot_3.png"
image Screenshot_4 = "Screenshot_4.png"
image Screenshot_5 = "Screenshot_5.png"
image Screenshot_6 = "Screenshot_6.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

default inventory = []
default inventory_slot_count = 21 # The number of slots is set to 21 by default but can be changed by setting the inventory_slot_count variable.
default gold = 100
# The game starts here.

label start:
    show Grassland
    # Introduction: A Simple Inventory System for Your Game

    "Hey there! Welcome to my simple inventory demo project."
    "I cooked up this project to dive deep into the world of Ren'Py. You know what sparked the idea for this neat inventory system? It was none other than iceorfire.com."
    "Their tutorial got me hyped, so I put my own twist on it, polished it, and added some new features while keeping the simplicity of the original project."
    "My goal? Craft an inventory system that's simple yet powerful—a system that can slide seamlessly into any basic game."

    "Here, simplicity reigns supreme. We're rocking a trusty list for our inventory. Add or remove items, and you're golden! No convoluted class-based shenanigans here."
    "Simpler code = fewer bugs. It's the perfect starting point, especially if you're new to coding. You can take this foundation and build something even better."

    "Improving the existing inventory and customizing it to fit your needs is a great way to level up your skills."

    "Now, I had a boatload of cool ideas to elevate this inventory system, but I decided to stick to the basics. I split the project into two flavors: the simple version we're using now and an advanced one."
    "The simple system is beginner-friendly and smooth as butter. If you're feeling adventurous, check out my Git repository or my itch.io profile for the advanced version."

    "But enough talk—let's see this baby in action."
    "Today, we're whipping up a slick heads-up display and a snazzy backpack button to access the inventory screen."

    show screen HUD

    "Awesome! Check out that snazzy HUD and the backpack icon. I bet you're already feeling like a pro! 😄"
    show Screenshot_1
    "Here's a screenshot of the editor showing how I call the HUD screen. It's predefined, so no fuss."
    hide Screenshot_1
    "Alright, let's open the inventory!"
    show screen inventory
    "You can open the inventory by clicking the backpack icon in the HUD and close it by clicking the red cross button in the top-right corner! Try it out."

    "Awesome, you clicked it! Now you know how to open and close the inventory."
    show Screenshot_2
    "Hmm, an empty inventory—and let's be honest, an empty inventory is no fun. Let's spice it up!"
    hide Screenshot_2
    "Time to add some items. How do we do that? Super simple!"
    "Step 1: Go to the icon folder inside the inventory folder. That's where the dummy item icons are."
    show Screenshot_3
    "Create your own items by designing a 100px by 100px icon image and naming it the same way I've named my items. This step is crucial."
    hide Screenshot_3
    "The inventory system uses the icon name to display items in the grid."
    "Step 2: After adding your icon, tell the inventory to include it with a variable."
    show Screenshot_4
    "For example: $ inventory.append('Banana')"

    $ inventory.append("Banana")
    $ inventory.append("Broccoli")
    $ inventory.append("Cabbage")
    $ inventory.append("Pear")
    $ inventory.append("Pepper")
    $ inventory.append("Potato")
    $ inventory.append("Pumpkin")
    $ inventory.append("Lemon")
    
    "Let's fill up the inventory with goodies!"
    hide Screenshot_4

    show screen inventory
    "Yay! Our inventory is now brimming with items. Adding your custom items is a breeze!"
    "Just drop your custom PNG icons into the 'inventory/images/icons' folder and use $ inventory.append('ItemName'). Easy peasy!"
    "Let's talk more about our simple inventory system."
    show Screenshot_2
    "In this demo, we have 21 available slots. Want more? Just edit the inventory_slot_count variable to add as many slots as you like."
    "Let's increase the total inventory slots capacity by editing the inventory slot count variable. Increase the slot number to 35 so we have more space to store additional items."
    hide Screenshot_2
    show Screenshot_6
    "At this moment, we have seven slots in each row. If we want to increase by two more rows, we need to add 14 more slots. "
    "Let's do this by editing the inventory slot count variable as follows: $ inventory_slot_count += 14"
    hide Screenshot_6
    $ inventory_slot_count += 14
   
    show screen inventory
    "The system now automatically adds a dynamic scrollbar. How cool is that? You can drag the inventory scrollbar and explore the extended slot like a pro!"
    "Now, let's dive into removing items."
    "For instance, I'm not a huge fan of lemons, so..."

    $ inventory.remove("Lemon")


    show Screenshot_5
    "To remove the item lemon you have to declare it like this : $ inventory.remove('Lemon')"
    hide Screenshot_5
    show screen inventory
    "Poof! The 'Lemon' is gone. Add or remove items as you please."
   

    "So, that's the gist of our simple inventory system. It's got all the essentials."

    "Wait, there's more! Let's learn how to check what's in the inventory and create game-changing features around it."

    jump Forest

label Forest:
    show Forest
    "Time to test our inventory skills in this lush forest."
    "Imagine your player stumbles upon an 'Apple' in the wild. Jackpot!"

    $ inventory.append("Apple")
    show screen inventory
    "The apple is now in our inventory. It's a simple reward that can elevate your game's experience."

    if "Apple" in inventory:
        "Now we have the apple in our inventory let's add some more goodies. Let's add 1000 gold and a mystical compass."
        $ gold += 1000
        $ inventory.append("Compass")
        show screen inventory
        "Yay more items."
    else:
        "No apple? No worries! Here's a fish instead."
        $ inventory.append("Fish")

    hide Forest

    jump End

label End:
    show Grassland2
    "Thank you for checking out my Simple inventory system demo!"
    "Before I go, I wish you success with your own project. I am sure you can do even better than mine."
    "I created this project when I was a beginner and knew nothing about game development, especially in relation to visual novels."
    "This project is based on a tutorial. In the original project, some of the features I wanted were not included, so I made my own improvements. I am confident that you can create your own version and make it even better."
    "For more projects, visit my Git repository or itch.io profile."
    "I wish you all the best. This project is a small gift from me to you so that you can focus on the most important parts: storytelling and artwork."
    "Please remember to credit the asset creators—details are in the description and the GitHub readme."
    "Have a fantastic day!"
return
