style Inventory_frame is frame:
    background  "components/inventory/images/gui/inventoryBG.png"
    xsize 1160
    ysize 570
    xalign 0.5
    yalign 0.4

style Inv_close_btn:
    xpos 1115
    ypos 5
    
style Inv_vbox is vbox:
    xpos 20
 
style Inv_title_frame is frame:
    padding (0,14)
    background None
    
style Inv_title is text:
    size 35
    pos (0, -12)
   
    
style Inv_grid is vpgrid:
    spacing 5
    
 
style Inv_item_name is text:
    size 16
    bold True
    color  "#f3f3f3"
    pos (0,120) 

# Close Icon
image Close:
    "components/inventory/images/gui/close.png"
    size(30,30) 

# backpack icon     
image Close_hover:
    "components/inventory/images/gui/close_hover.png"
    size(30,30)  

 
# Update the default scrollbar images
style inventor_scrollbar:
    ysize 24
    left_bar Frame("components/inventory/images/gui/vertical_idle_bar.png", tile=gui.bar_tile)
    right_bar Frame("components/inventory/images/gui/vertical_hover_bar.png", tile=gui.bar_tile)
    thumb Frame("components/inventory/images/gui/vertical_thumb.png", tile=gui.bar_tile)

 
    