# Some default background images
image Grassland = "Grassland.png"
image Grassland_2 = "Grassland_2.png"
image initialise_variables = "initialise the variables.png"
image Forest = "Forest.png"
image backpack_arrow = "backpack arrow.png"
image Screenshot_1 = "Screenshot_1.png"
image Screenshot_2 = "Screenshot_2.png"
image Screenshot_3 = "Screenshot_3.png"
image Screenshot_4 = "Screenshot_4.png"
image Screenshot_5 = "Screenshot_5.png"
image Screenshot_6 = "Screenshot_6.png"
image Screenshot_7 = "Screenshot_7.png"
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
    "I cooked up this project to dive deep into the world of Ren'Py. You know what sparked the idea for this neat inventory system? It was none other than iceorfire.com inventory tutorial."
    "Their tutorial got me hyped, so I put my own twist on it, polished it, and added some new features while keeping the simplicity of the original project."
    "My goal? Craft an inventory system that's simple yet powerful a system that can slide seamlessly into any basic game."

    "Here, simplicity reigns supreme. We're rocking a trusty list for our inventory. Add or remove items, and you're golden! No convoluted class-based shenanigans here."
    "Simpler code = fewer bugs. It's the perfect starting point, especially if you're new to coding. You can take this foundation and build something even better."

    "Improving the existing inventory and customizing it to fit your needs is a great way to level up your skills."

    "Now, I had a boatload of cool ideas to elevate this inventory system, but I decided to stick to the basics. I split the project into two flavors: the simple version we're using now and an advanced one."
    "The simple system is beginner-friendly and smooth as butter. If you're feeling adventurous, check out my Git repository or my itch.io profile for the advanced version."

    "But enough chit-chat! Let's see this beauty in action."

    "First things first, we need to set things up!"
    "First drag the component folder in to your game root directory like in the demo project. Next you need to initiate the Default variables."
    show initialise_variables
    "To integrate the inventory into your game, just copy and paste these magic spells er, variables. 🪄"
    hide initialise_variables
    "Today, we'll conjure up a slick heads-up display and a snazzy backpack button to access the inventory screen. ✨"

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

    $ inventory.append("Banana")
    $ inventory.append("Broccoli")
    $ inventory.append("Cabbage")
    $ inventory.append("Pear")
    $ inventory.append("Pepper")
    $ inventory.append("Potato")
    $ inventory.append("Pumpkin")
    $ inventory.append("Lemon")

    "Let's fill up that inventory with some goodies!"
    hide Screenshot_4

    show screen inventory
    "Hooray! Our inventory is now overflowing with items. Adding your custom ones is a breeze! 🍎🥦"
    "Just drop your custom PNG icons into the 'inventory/images/icons' folder and use $ inventory.append('ItemName'). Easy peasy!"
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
    "Wow, we're hoarding a mini farmers' market in here! Bananas, apples, pears, and even potatoes. But, oof, lemons? Hard pass. Let's do some citrus decluttering!"
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

    if "Apple" in inventory:
        "Now that we've snagged the apple, let's go on a spree! Adding 1000 gold coins and a mystical compass to our haul."
        $ gold += 1000
        $ inventory.append("Compass")
        show screen inventory
        "Jackpot! We've got more treasures now. Happy adventuring!"
    else:
        "No apple? Never fear! Here's a fish instead, because every adventurer needs a snack!"
        $ inventory.append("Fish")

    hide Forest

    jump End

label End:
    show Grassland_2
    "Thanks for checking out my Simple Inventory System demo!"
    "Before I go, I wish you all the success with your own project. I bet you'll make something even cooler than mine!"
    "When I created this project, I was just a beginner learning the ropes of game development and visual novels."
    "This project is based on a tutorial. Some features I wanted weren't covered, so I added my own spin to it. I believe you can take this and create something uniquely yours."
    "For more projects, feel free to visit my Git repository or itch.io profile."
    "Wishing you all the best. Consider this project a little gift to help you focus on what matters most: storytelling and artwork."
    "And don't forget to credit Me and other asset creators details are in the description and the GitHub readme."
    "Have an awesome day!"
return

