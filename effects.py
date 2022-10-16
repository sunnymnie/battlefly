import e_utility
import e_weapon
import e_defense


utilities = list(filter(lambda x: x[:2] != "__", dir(e_utility)))
weapons = list(filter(lambda x: x[:2] != "__", dir(e_weapon)))
defenses = list(filter(lambda x: x[:2] != "__", dir(e_defense)))


UTILITY = dict(zip(utilities, list(map(lambda x: eval("e_utility." + x), utilities))))
WEAPON = dict(zip(weapons, list(map(lambda x: eval("e_weapon." + x), weapons))))
DEFENSE = dict(zip(defenses, list(map(lambda x: eval("e_defense." + x), defenses))))
TRAIT = {}
# class Effect():
#     def __init__(self, name, lvl, 

# def get_weapon(w):
#     return WEAPON[w[:-1]][int(w[-1])]

# def get_utility(u):
#     return UTILITY[u[:-1]][int(u[-1])]

# def overclocking_protocols(bf, time, **kwargs):
#     """requires self"""
#     if bf.hull < 0.3:
#         kwargs["effects"].remove(kwargs["self"])
#         # buff me