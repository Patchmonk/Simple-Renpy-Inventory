# # Simple Renpy Inventory

I specifically created this project because I wanted to learn more about Renpy. I originally got the idea of the simple inventory system from iceorfire.com After reading their tutorial, I was super excited, so I made my own version of it and improved it. Because the inventory system is based on a simple dictionary, it’s easy to handle for beginners. You don’t have to worry about all those complex inventory systems out there. This is a good starting point for anyone who wants to gain experience developing games. While it may be simple, it’s powerful enough for a simple game. I also created an advanced version of the inventory system which is based on the object-oriented method. If you’re interested, please check out my other repositories. Thanks!

 

![Screenshot 2023-08-16 210459](https://github.com/Patchmonk/Simple-Renpy-Inventory/assets/7914321/8ed36737-4066-471f-a2ee-002d094ec2be)

![Screenshot 2023-08-16 210624](https://github.com/Patchmonk/Simple-Renpy-Inventory/assets/7914321/138d4ac6-c7e7-42fa-8588-4145facf64e0)

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

## License
This project is licensed under the MIT License.
