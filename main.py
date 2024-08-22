from pyscript import document # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "2"


def select_face_option(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code
    dice_type = document.querySelector("#dice_type").value

def roll_all_dice(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code

    rolls = int(document.querySelector("#rolls").value)
    while rolls > 0:
        result = dice.roll_dice(int(dice_type))
        res_string = str(result)
        document.querySelector("div#roll-history").innerHTML += "<p>" + res_string + "</p>"
        rolls -= 1







def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""
