screen inventory:
    modal True
    frame style style["Inventory_frame"]:
        imagebutton style style["Inv_close_btn"]:
            idle "Close"
            hover "Close_hover"
            action Hide("inventory")     
        
        vbox style style["Inv_vbox"]:
            text "Inventory"style style["Inv_vbox_text"]
            vpgrid cols 7 style style["Inv_grid"]:
                if slot_count > 30:
                    draggable True mousewheel True scrollbars "vertical" 
                else:
                    draggable False mousewheel False
                for slot in range(slot_count):
                            
                    frame:
                        maximum(155, 155)
                        if slot < len(inventory):
                            background Image("images/inventory/inventory_hud/slot_bg.png") xalign 0.5 yalign 0.5
                            add Image("images/inventory/" + inventory[slot] + ".png", xalign=0.5, yalign=0.5)
                            $ Inv_item_name = inventory[slot].replace('_', ' ')
                            text Inv_item_name style style["Inv_item_name"]
                        else:
                            background Image("images/inventory/inventory_hud/slot_bg.png") xalign 0.5 yalign 0.5



            