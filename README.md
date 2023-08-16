# Simple-Renpy-Inventory
# Inventory System

This is a simple inventory system that allows users to store and manage items.

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
To modify the slot counts in the inventory, change the variable default slot_count. For example, if you want to give more slots to the player, you can add seven more slots to the game 
while maintaining the grid structure. After increasing the slot count and adding seven more slots to the inventory, the default slot_count will be equal to 28.
To add or remove items you can see the example demo code inside the script.rpy file
To add an item to the inventory, for example, you can define it like this: $ inventory.append("Apple") as long as you have the Apple icon inside your designated folder able to create a new item in your game.
To remove an item from the inventory, $ inventory.remove("Log")
 

## Bugs

* When you add more than 21 slots to your inventory, the inventory system will dynamically activate the scroll bar. As a result, your inventory screen may look slightly different.
  If you encounter similar problems, feel free to modify the styles.

 

## Contact

If you have any questions or feedback, please open an issue on the project's GitHub repository.

## License
This project is licensed under the MIT License.
