"""
zelf geschreven maar geinspireerd door ChatGPT
"""

import secrets

weapon_dict = {0:"auto rifle", 1:"dual shotgun", 2:"dual pistols", 3:"auto shotgun", 4:"burst pistol", 5:"sniper", 6:"flamethrower", 7:"seagle",
               8:"laser cannon", 9:"crossbow", 10:"orb launcher", 11:"rocket launcher", 12:"minigun", 13:"blade launcher",
               14:"cluster launcher", 15:"marksman rifle", 16:"arcane wand", 17:"ice staff", 18:"lightning scepter"}

nade_dict = {0:"grenade", 1:"grappling hook", 2:"black hole", 3:"laser beam", 4:"ice blast", 5:"electro globe", 6:"air strike"}

melee_dict = {0:"claw", 1:"dagger", 2:"hammer", 3:"pickaxe", 4:"katana"}

def laurens():
    print("skill issue")

def weapon():
    n = secrets.randbelow(19)
    return print("weapon: ", weapon_dict[n])

def nade():
    n = secrets.randbelow(7)
    return print("nade: ", nade_dict[n])

def melee():
    n = secrets.randbelow(5)
    return print("melee: ", melee_dict[n])

weapon()
nade()
melee()
# laurens()

