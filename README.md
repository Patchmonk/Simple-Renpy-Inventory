## Simple Renpy Inventory

Driven by a desire to explore Ren'Py, I embarked on this project. The idea for our simple yet marvelous inventory system was sparked by a tutorial from iceorfire.com that captured my interest. Inspired, I created my own version, enhanced with additional features. The charm of this inventory system lies in its simplicity. Built on the solid foundation of a straightforward empty list, it is an ideal starting point for beginners. It avoids the complexities often associated with other inventory systems, making it perfect for those new to game development.

Despite its simplicity, it possesses a surprising amount of power, suitable for creating engaging simple games. Additionally, I developed an advanced version using an object-oriented approach. You are welcome to explore my other repositories for more. This project is just a small part of the grand scheme of learning and creation. If you'd like to expand your knowledge and experience, please consider this venture a stepping stone. Here's to growth, innovation, and the joy of creation. Cheers!


 ![1](https://github.com/Patchmonk/Simple-Renpy-Inventory/assets/7914321/e176ed5e-9ee5-4413-ac6f-3f5885e32278)


 ![2](https://github.com/Patchmonk/Simple-Renpy-Inventory/assets/7914321/d669dc11-bbb8-4ddc-ac82-7003768710e0)



## Features

* by default currently we have 21 slots in the inventory but you can change the slot count by modifying the default slot_count variable.
* Items can be added, or removed.
* The inventory can be customized with different themes and colors.
* You can increase or decrease the slot based on your game needs.
* You can use a conditional argument to check whether a certain item is in the inventory or not.

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

* The simple inventory is stable now, I managed to track down all the known bugs and fix them.
* If you find any new bugs please report.

 

## Contact

If you have any questions or feedback, please open an issue on the project's GitHub repository.

## Graphics resources

pixiv.net/en/users/12597768

arcsine-technologies.itch.io/veggie-pack-volume-i

## License
This project is licensed under the MIT License.
