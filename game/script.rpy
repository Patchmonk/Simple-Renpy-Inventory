﻿# Some default background images
image Grassland = "Grassland.png"
image Grassland_2 = "Grassland_2.png"
image initialise_variables = "initialise the variables.png"
image Forest = "Forest.png"
image backpack_arrow = "backpack arrow.png"
image Screenshot_0 = "Screenshot_0.png"
image Screenshot_1 = "Screenshot_1.png"
image Screenshot_2 = "Screenshot_2.png"
image Screenshot_3 = "Screenshot_3.png"
image Screenshot_4 = "Screenshot_4.png"
image Screenshot_5 = "Screenshot_5.png"
image Screenshot_6 = "Screenshot_6.png"
image Screenshot_7 = "Screenshot_7.png"
image Screenshot_8 = "Screenshot_8.png"
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

    "Hey there! Welcome to the tutorial for building a simple inventory system in Ren'Py. 😊"
    "I'm excited to guide you through this project, where we'll take a look at how to create a simple yet powerful inventory system. This isn't just a demo; it's a full tutorial, where I'll show you how to integrate the system into your own games."


    "I cooked up this project to dive deep into the world of Ren'Py. You know what sparked the idea for this neat inventory system? It was none other than iceorfire.com inventory tutorial."
    "Their tutorial got me hyped, so I put my own twist on it, polished it, and added some new features while keeping the simplicity of the original project."
    "My goal with this tutorial is simple: I want to help you create an inventory system that's both easy to use and versatile enough for most Ren'Py games. Whether you're working on a visual novel or an interactive story, you'll have something solid to build on."

    "And I promise you, this won't be one of those boring documentation dumps. I'll walk you through each step with explanations, tips, and tricks that'll make the process smooth and hopefully, a little fun, too!"



    "Here, simplicity reigns supreme. We're rocking a trusty list for our inventory. Add or remove items, and you're golden! No convoluted class-based shenanigans here."
    "Simpler code = fewer bugs. It's the perfect starting point, especially if you're new to coding. You can take this foundation and build something even better."

    "Improving the existing inventory and customizing it to fit your needs is a great way to level up your skills."

    "Now, I had a boatload of cool ideas to elevate this inventory system, but I decided to stick to the basics. I split the project into two flavors: the simple version we're using now and an advanced one."
    "The simple system is beginner-friendly and smooth as butter. If you're feeling adventurous, check out my Git repository or my itch.io profile for the advanced version."

    "But enough chit-chat! Let's see this beauty in action."

    "First things first, we need to set things up!"
    "First drag the component folder in to your game root directory like in the demo project. Next you need to initiate the Default variables."
    show Screenshot_0

    "The screenshot shows the desired folder structure. Just drag and drop it into your root folder, as demonstrated. It's easy and straightforward."
    hide Screenshot_0
    show initialise_variables
    "To integrate the inventory into your game, just copy and paste these magic spells er, variables. 🪄"
    hide initialise_variables
    "Let's make a slick heads-up display and a snazzy backpack button to access the inventory screen. ✨"
    show screen HUD
    show backpack_arrow
    "Check out that snazzy HUD and the backpack icon. Bet you feel like a pro already! 😄"
    hide backpack_arrow
    show Screenshot_1
    "Here's a screenshot of the editor showing how I call the HUD screen. Predefined and fuss-free!"
    hide Screenshot_1
    "Alright, let's crack open the inventory!"
    show screen inventory
    "You can open the inventory by clicking the backpack icon in the HUD and close it by clicking the red cross button in the top-right corner. Give it a try!"

    "Nice click! Now you know how to open and close the inventory."
    "One last thing before we move on with the tutorial: I'll automatically open the inventory for a quick explanation. But you have to close it to proceed. Otherwise, you cannot continue the tutorial. Alright, let's get this show on the road!"
    show Screenshot_2
    "Yikes, an empty inventory? Let's spice things up a bit!"
    hide Screenshot_2
    "Time to add some items. It's super simple!"
    "Step 1: Navigate to the icon folder inside the inventory folder. That's where the dummy item icons are hiding."
    show Screenshot_3
    "Create your own items by designing a 100px by 100px icon image and naming it just like I've named my items. This part is crucial."
    hide Screenshot_3
    "The inventory system uses the icon names to show items in the grid."
    "Step 2: After adding your icon, tell the inventory to include it with a variable."
    show Screenshot_4
    "For example: $ inventory.append('Banana')"
    "If you're scratching your head wondering what's going on, don't worry, it's a piece of cake. Remember the inventory folder with all the icons?"
    "We're just creating variables named after these icons and telling our inventory that these icons are now officially Inventory items. Easy peasy!"
    "When creating your own item, it's essential to follow these specific steps. First, place your icons into the designated folder that contains all of my dummy icons. "
    "Then, create variables using the default Python .append function shown in the screenshot. Like this:  $ inventory.append('Mango') "
    "It's crucial to name your variables based on your icon names. If you get these steps, we're golden!"
    "The screenshot clearly shows that numerous icons have been defined. We should now verify if these icons are present in our inventory."
   
    $ inventory.append("Banana")
    $ inventory.append("Lemon")
    $ inventory.append("Orange")
    $ inventory.append("Peach")
    $ inventory.append("Pear")
    $ inventory.append("Pumpkin")
    $ inventory.append("Strawberry")
    $ inventory.append("Watermelon")
    $ inventory.append("Pomegranate")
     
    hide Screenshot_4 

    show screen inventory
    "Hooray! Our inventory is now overflowing with items. Adding your custom ones is a breeze! 🍎🥦"
    "Just drop your custom PNG icons into the 'components/inventory/images/icons' folder and use $ inventory.append('ItemName'). Easy peasy!"
    "Now, let's chat more about our simple inventory system."
    show Screenshot_2
    "In this demo, we have 21 available slots. Want more? Simply tweak the inventory_slot_count variable to add as many slots as your heart desires."
    "Let's increase the total inventory slots by editing the inventory_slot_count variable. Lets, bump that number up to 35!"
    hide Screenshot_2
    show Screenshot_6
    "Right now, we've got seven slots per row. Adding two more rows means 14 more slots."
    "Do this by editing the inventory_slot_count variable like this: $ inventory_slot_count += 14"
    hide Screenshot_6

    $ inventory_slot_count += 14
 
    show screen inventory
    "System's got a new trick up its sleeve a dynamic scrollbar! Fancy, right? Drag it around like a rockstar and show that inventory who's boss!"
    "Alright, let's dive into the inventory's greatest hits! You've nailed adding items, now for the thrilling sequel removing them! Let's roll!"
    "So, let's crack open the inventory and see if there's any junk we can toss out. Any takers?"
    show screen inventory
    "Wow, we're hoarding a mini farmers' market in here! Bananas, apples, pears, and even Pumpkin. But, oof, lemons? Hard pass. Let's do some citrus decluttering!"
    $ inventory.remove("Lemon")

    show Screenshot_5
    "Here's the magic spell for lemon banishment: $ inventory.remove('Lemon')."
    hide Screenshot_5
    show screen inventory
    "And just like that poof! The lemon's history. Feel free to shuffle your stash as you please."

    "So, that's the gist of our simple inventory system. Basic, but it covers the essentials!"
    "Hold up, there's more up my sleeve! Let's dive into checking what's in the inventory and crafting some game-changing features."
    hide Grassland
    jump Forest

label Forest:
    show Forest
    "Welcome to the magical forest! 🌳 Time to put our inventory skills to the test in this lush adventure land."
    "Picture this: Your player stumbles across an 'Apple' in the wild. Score!"

    $ inventory.append("Apple")
    
    show screen inventory
    "Congratulations! You've just added an apple to your treasure trove. It's a little win that can sweeten your game experience."
    "For the sake of gameplay, let's create a condition. If you have that mysterious apple, you will be rewarded with extra rewards. Yeah, not very creative, I know. "
    show Screenshot_8
    "This is just a simple demonstration to show you how you can trigger event based on inventory items."
    "As you can see, I'm just tossing in some coins and items to reward the player, but you can hop into a different event or label if you prefer. It's just a simple logic. Easy peasy, right?"
    hide Screenshot_8

    if "Apple" in inventory:
        "Now that we've snagged the apple, let's go on a spree! Adding 1000 gold coins and a Magical Mana Gem to our haul."
        $ gold += 1000
        $ inventory.append("Mana Gem")
        show screen inventory
        "Jackpot! We've got more treasures now. Happy adventuring!"
    else:
        "No apple? No problem! Here's a potato instead because who can resist a tasty, delicious potato? You know it's the underdog of snacks!"
        $ inventory.append("Potato")

    hide Forest

    jump End
# Define the transformation
transform my_dissolve:
    alpha 0.0
    linear 1.0 alpha 1.0

# Use the transformation in your dialogue

label End:
    show Grassland_2
    "Thanks for checking out my Simple Inventory System demo!"
    "Before I go, I wish you all the success with your own project. I bet you'll make something even cooler than mine!"
    "When I created this project, I was just a beginner learning the ropes of game development and visual novels."
    "This project is based on a tutorial. Some features I wanted weren't covered, so I added my own spin to it. I believe you can take this and create something uniquely yours."
    "For more projects, feel free to visit my Git repository or itch.io profile."
    "Wishing you all the best. Consider this project a little gift to help you focus on what matters most: storytelling and artwork."
    "If you find Simple Renpy Inventory useful, please consider giving credit to {b}{color=#00ff88}Arham or Patchmonk{/color}{/b}. Thank you!"

    "Have an awesome day!"
return

