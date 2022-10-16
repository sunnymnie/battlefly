from effects import WEAPON as w_effects
from effects import UTILITY as u_effects
from effects import DEFENSE as d_effects
from battlefly import Weapon, Utility
from copy import deepcopy

MAX_LVL = 1

WEAPON = {
    "proton_blaster": [
        Weapon(1, int(32*1e3), int(2*1e3), [w_effects["proton_blaster"]], name="pho1")
    ],
    "hunter_missiles":[
        Weapon(1, int(54*1e3), int(4.5*1e3), [w_effects["hunter_missles"]], name="hunt1")
    ],
    "mining_laser":[
        Weapon(2, int(24*1e3), int(4*1e3), [w_effects["mining_laser"]], name="las1")
    ],
    "autocannon":[
        Weapon(2, int(13*1e3), int(2*1e3), [w_effects["autocannon"]], name="auto1")
    ],
    "micro_rocket_pods":[
        Weapon(16, int(7.5*1e3), int(8*1e3), [w_effects["micro_rocket_pods"]], name="micro1")
    ],
    "howitzer":[
        Weapon(2, int(52*1e3), int(4*1e3), [w_effects["howitzer"]], name="how1")
    ]
}

UTILITY = {
    "overclocking_protocols": [
        Utility([u_effects["overclocking_protocols"]], name="over1")
    ],
    "regenerative_nanobot": [
        Utility([u_effects["regenerative_nanobot"]], name="reg1")
    ],
    "combat_algorithms_processor": [
        Utility([u_effects["combat_algorithms_processor"]], name="cbt1")
    ],
    "rage_against_the_nano_machines": [
        Utility([u_effects["rage_against_the_nano_machines"]], name="rage1")
    ],
    "auto_reloaders": [
        Utility([u_effects["auto_reloaders"]], name="auto1")
    ],
    "cryo_ammo": [
        Utility([u_effects["cryo_ammo"]], name="cryo1")
    ],
}

DEFENSE = {
    "force_shield_warp": [
        Utility([d_effects["force_shield_warp"]], name="warp1")
    ],
    "ceramo_armor": [
        Utility([d_effects["ceramo_armor"]], name="cer1")
    ],
    "plasteel_hull": [
        Utility([d_effects["plasteel_hull"]], name="pla1")
    ],
    "force_shield_at": [
        Utility([d_effects["force_shield_at"]], name="at1")
    ],
    "force_shield_nx": [
        Utility([d_effects["force_shield_nx"]], name="nx1")
    ],
    "boosters_thrusters": [
        Utility([d_effects["boosters_thrusters"]], name="boost1")
    ],
}

def get_weapon(name, lvl):
    return deepcopy(WEAPON[name][lvl-1])

def get_utility(name, lvl):
    return deepcopy(UTILITY[name][lvl-1])

def get_defense(name, lvl):
    return deepcopy(DEFENSE[name][lvl-1])

def get_weapons_list():
    return list(WEAPON.keys())

def get_utilities_list():
    return list(UTILITY.keys())

def get_defenses_list():
    return list(DEFENSE.keys())
