def plasteel_hull(bf, time, self, effects):
    effects.remove(self)
    bf.armor = 1*1e3
    bf.hull = int(bf.hull*1.04)
    
def force_shield_at(bf, time, self, effects):
    effects.remove(self)
    bf.max_shield += 50*1e3
    bf.shield = bf.max_shield
    
def force_shield_nx(bf, time, self, effects):
    effects.remove(self)
    bf.max_shield += int(25*1e3)
    bf.shield = bf.max_shield
    bf.shield_regen += 0.005
    
def force_shield_warp(bf, time, self, effects):
    effects.remove(self)
    bf.max_shield += int(12.5*1e3)
    bf.shield = bf.max_shield
    bf.shield_regen += 0.01
    # def force_shield_warp(bf, time, self, effects):
    #     regen = 0.01
    #     bf.shield = min(bf.max_shield, bf.sheild + int(time/1e3*(regen*bf.max_shield)))
    # effects.append(force_shield_warp)
    
def boosters_thrusters(bf, time, self, effects):
    effects.remove(self)
    bf.evasion_chance += 0.03
    
def ceramo_armor(bf, time, self, effects):
    effects.remove(self)
    bf.armor = 4*1e3
    