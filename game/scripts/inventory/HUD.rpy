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

# backpack icon  
image Backpack:
    "scripts/inventory/images/backpack.png"
    size(60,60) 
    
image Backpack_Hover:
    "scripts/inventory/images/backpack_hover.png"
    size(60,60) 

