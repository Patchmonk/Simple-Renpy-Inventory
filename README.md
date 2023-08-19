## Simple Renpy Inventory

I embarked on this project driven by my eagerness to explore the realms of Ren'Py. The spark that ignited the creation of our simple yet marvelous inventory system came from none other than iceorfire.com. Their tutorial caught my attention, and I couldn't help but get swept up in a wave of excitement. With that inspiration as my guide, I crafted my own rendition, injecting it with a healthy dose of enhancements.

The beauty of this inventory system lies in its simplicity. It's built upon the solid foundation of a straightforward empty list., making it an ideal starting point for those new to the scene. Say goodbye to the complexities that often accompany other inventory systems – this one's tailor-made for beginners looking to gain a foothold in game development.

Don't let its simplicity fool you, though. Beneath that user-friendly exterior, it holds a surprising amount of power, well-suited for crafting engaging simple games. And guess what? I didn't stop at the basics. I also rolled out an advanced version, fueled by the object-oriented approach. You're invited to delve into my other repositories to check out the goodies.

In the grand tapestry of learning and creation, this project is but a thread. If you're seeking to expand your knowledge and experience, consider this venture a stepping stone. Here's to growth, innovation, and the joy of creation. Cheers!
 
![Screenshot 2023-08-18 035418](https://github.com/Patchmonk/Simple-Renpy-Inventory/assets/7914321/75dc5468-86f6-4921-9235-ef7d1ee9cef7)

![Screenshot 2023-08-18 035510](https://github.com/Patchmonk/Simple-Renpy-Inventory/assets/7914321/0e1e212d-2b1b-4b78-a8a9-b2aebc3008ba)

## Features

* by default currently we have 21 slots in the inventory but you can change the slot count by modifying the default slot_count variable.
* Items can be added, or removed.
* The inventory can be customized with different themes and colors.
* This simple inventory system has the capability to activate the dynamic scroll bar if it exists more than 21 slots.
* You can increase or decrease the slot based on your game needs.

## Requirements
* Ren'Py 8.0 or higher

## Installation

1. Clone the repository to your local machine.
2. To merge it with your own game all you have to do is copy two different folders the first folder is the images folder and the second folder is the script folder.
3. If you want to change the folder structure based on your own preference please make sure you modify the screen code and define the folder location otherwise the inventory system will break.

## Usage
If you want to use all the features of the simple inventory I highly recommend you check the demo script.rpy file. In there, you will find the basic uses of the inventory system.

To modify the slot counts in the inventory, change the variable default slot_count. For example, if you want to give more slots to the player, you can add seven more slots to the game 
while maintaining the grid structure. After increasing the slot count and adding seven more slots to the inventory, the default slot_count will be equal to 28.

To add an item to the inventory, for example, you can define it like this: $ inventory.append("Apple") as long as you have the Apple icon inside your designated folder able to create a new item in your game.
To remove an item from the inventory, $ inventory.remove("Log")
 

## Bugs

* When you add more than 21 slots to your inventory, the inventory system will dynamically activate the scroll bar. As a result, your inventory screen may look slightly different.
  If you encounter similar problems, feel free to modify the styles.

 

## Contact

If you have any questions or feedback, please open an issue on the project's GitHub repository.

## Graphics resources

pixiv.net/en/users/12597768

arcsine-technologies.itch.io/veggie-pack-volume-i

## License
This project is licensed under the MIT License.
