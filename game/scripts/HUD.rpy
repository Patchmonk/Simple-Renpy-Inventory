screen HUD():
    frame:
        xpos 0 ypos 0
        xminimum 1920
        yminimum  60
      
        background "#0000005e"
        has hbox
        
        # text " Gold : [gold]" xpos 10 ypos 20 
        text " Gold : [gold]" xpos 5 ypos 15 
        imagebutton:
            xpos 0 ypos 0
            idle "Backpack"
            hover "Backpack_Hover"
            action Show("inventory")
            padding (10,3,5,5)

image Backpack:
    "images/inventory/inventory_hud/backpack.png"
    size(60,60) 

# backpack icon     
image Backpack_Hover:
    "images/inventory/inventory_hud/backpack_hover.png"
    size(60,60) 


image Close:
    "images/inventory/inventory_hud/close.png"
    size(30,30) 

# backpack icon     
image Close_hover:
    "images/inventory/inventory_hud/close_hover.png"
    size(30,30) 