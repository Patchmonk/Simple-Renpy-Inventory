screen inventory:
    modal True
    frame style style["Inventory_frame"]: # This frame contains the inventory buttons and the scrollbar.
        imagebutton style style["Inv_close_btn"]: # This button closes the inventory screen.
            idle "Close"
            hover "Close_hover"
            action Hide("inventory")

        

        vbox style style["Inv_vbox"]:  # This vbox contains the title and the grid of inventory slots.
            frame style style["Inv_title_frame"]:
                text "Inventory" style style["Inv_title"]

            viewport id "vp":
                # The original dynamics vscrollbar bar argument is removed here, In this version we are using the Renpy function, If you want to use the previous version you can always check the previous git version.
                ysize 475
                xsize 1160
                draggable True
                mousewheel True
                scrollbars "vertical"  
                vscrollbar_xsize 10
                vscrollbar_ysize 475  
                vscrollbar_ypos 0
                vscrollbar_xpos -21
                vscrollbar_base_bar "components/inventory/images/gui/inv_vscrollbar_base_bar.png" 
                vscrollbar_thumb "components/inventory/images/gui/inv_vscrollbar_thumb.png"
                vscrollbar_unscrollable "hide"

                vpgrid cols 7 style style["Inv_grid"]: # This vpgrid displays the inventory slots.
        
                    for slot in range(inventory_slot_count):  # This loop iterates over all the inventory slots. 
                        
                        frame: # This frame contains the inventory slot item.
                            maximum(155, 155)
                            if slot < len(inventory): # If the slot is not empty, the slot background image will display.
                                background Image("components/inventory/images/gui/slot_bg.png") xalign 0.5 yalign 0.5
                                add Image("components/inventory/images/icons/" + inventory[slot] + ".png", xalign=0.5, yalign=0.5) size (120, 120)
                                $ Inv_item_name = inventory[slot].replace('_', ' ')
                                text Inv_item_name style style["Inv_item_name"]
                            else:
                                # If the slot is empty, the background is displayed.
                                background Image("components/inventory/images/gui/slot_bg.png") xalign 0.5 yalign 0.5


 