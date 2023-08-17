style Inventory_frame is frame:
    background  "#030003b9"
    xsize 1160
    ysize 560
    xalign 0.5
    yalign 0.4


style Inv_close_btn:
    xpos 1115
    ypos 5
    
style Inv_vbox is vbox:
    xalign 0.5
    yalign 0.5
 

style Inv_vbox_title is text:
    size 35
    color Color((255, 255, 255, 255))
    pos (0,-10) 
 
style Inv_grid is vpgrid:
    spacing 5
    xalign 0.5
    yalign 0.5

style Inv_item_name is text:
    size 16
    bold True
    color Color((100, 245, 4, 255))
    pos (0,118) 

style inv_scrollbar is scrollbar: 
    xsize 1100
    ysize 450