import json
from battlefly import Battlefly, Weapon, Utility
from effects import WEAPON, UTILITY, TRAIT

def test():
    print("WOrks")

def get_battleflies():
    with open('battleflies.json') as json_file:
        data = json.load(json_file)
        return data
    
def save_battleflies(bf):
    with open('battleflies.json', 'w', encoding='utf-8') as f:
        json.dump(bf, f, ensure_ascii=False, indent=4)
        
def convert_bf_to_json(bf):
    res = {"name": bf.get_name(),
           "mods":{"w1":convert_weapon_to_json(bf.w1), 
                   "w2":convert_weapon_to_json(bf.w2), 
                   "u1":convert_utility_to_json(bf.u1),
                   "u2":convert_utility_to_json(bf.u2),
                  },
           "stats":{"wins":bf.wins, "battles":bf.battles},
           "traits": []}
    for t in bf.traits:
        res["traits"].append(TRAIT[t])
    return res
    
def convert_weapon_to_json(w):
    res = {"reload": w.reload, "burst":w.burst, "dmg":w.dmg, "effects": [], "name":w.name}
    for e in w.effects:
        res["effects"].append(e.__name__)
    return res

def convert_utility_to_json(u):
    res = {"name":name, "effects":[], "init_effects":[]}
    for e in u.effects:
        res["effects"].append(e.__name__)
    for e in u.init_effects:
        res["init_effects"].append(e.__name__)
    return res

def convert_json_to_bf(bf):
    w1 = convert_json_to_weapon(bf["mods"]["w1"])
    w2 = convert_json_to_weapon(bf["mods"]["w2"])
    u1 = convert_json_to_utility(bf["mods"]["u1"])
    u2 = convert_json_to_utility(bf["mods"]["u2"])
    new = Battlefly(w1, w2, u1, u2, wins=bf["stats"]["wins"], battles=bf["stats"]["battles"])
    traits = []
    for t in bf["traits"]:
        traits.append(TRAIT[t])
    new.add_traits(traits)
    return new
    

def convert_json_to_weapon(w, bf=None):
    effects = []
    for e in w["effects"]:
        effects.append(WEAPON[e])
    new = Weapon(w["burst"], w["dmg"], w["reload"], effects, name=w["name"])
    if bf: new.add_owner(bf)
    return new

def convert_json_to_utility(u, bf=None):
    effects = []
    init_effects = []
    for e in u["effects"]:
        effects.append(UTILITY[e])
    for e in u["init_effects"]:
        init_effects.append(UTILITY[e])
    new = Utility(effects, init_effects, u["name"])
    if bf: new.add_owner(bf)
    return new
