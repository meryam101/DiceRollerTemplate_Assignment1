# put your dice_roll() function in this file
import random

def roll_dice(type_d):
    dice_range = range(1, type_d + 1)
    face_value = random.choice(dice_range)
    return face_value

