from battlefly import Battlefly
import mods
import random

WEAPONS = mods.get_weapons_list()
UTILITIES = mods.get_utilities_list()
DEFENSES = mods.get_defenses_list()
MAX_LVL = mods.MAX_LVL


def generate_random_bf(lvl=MAX_LVL):
    return Battlefly(mods.get_weapon(WEAPONS[random.randint(0, len(WEAPONS)-1)], lvl), 
                     mods.get_weapon(WEAPONS[random.randint(0, len(WEAPONS)-1)], lvl), 
                     mods.get_defense(DEFENSES[random.randint(0, len(DEFENSES)-1)], lvl),
                     mods.get_utility(UTILITIES[random.randint(0, len(UTILITIES)-1)], lvl))

def generate_random_bfs(num, lvl=MAX_LVL):
    """generates num unique bfs with armaments with lvl"""
    bfs = []
    bfs_names = []
    while len(bfs)<num:
        bf = generate_random_bf(lvl=lvl)
        if bf.get_name() not in bfs_names:
            bfs.append(bf)
            bfs_names.append(bf.get_name())
    return bfs

def generate_all_bf_combinations(lvl=MAX_LVL):
    """generates all possible BFs with lvl"""
    bfs = []
    for w1 in WEAPONS:
        for w2 in WEAPONS:
            for d in DEFENSES:
                for u in UTILITIES:
                    bfs.append(Battlefly(mods.get_weapon(w1, lvl), 
                                         mods.get_weapon(w2, lvl), 
                                         mods.get_defense(d, lvl),
                                         mods.get_utility(u, lvl)))
    return bfs
