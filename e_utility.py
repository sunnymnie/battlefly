def overclocking_protocols(bf, time, self, effects):
    if bf.hull/bf.max_hull < 0.3:
        effects.remove(self)
        bf.w1.dmg = int(bf.w1.dmg*1.06)
        bf.w2.dmg = int(bf.w2.dmg*1.06)
        bf.w1.reload = int(bf.w1.reload*0.94)
        bf.w2.reload = int(bf.w2.reload*0.94)
        
def regenerative_nanobot(bf, time, self, effects):
    regen = 0.002
    bf.hull = min(bf.max_hull, bf.hull + int(time/1e3*(regen*bf.max_hull)))
    
def combat_algorithms_processor(bf, time, self, effects):
    effects.remove(self)
    bf.crit_chance += 0.03
    bf.crit_dmg += 0.05
    
def rage_against_the_nano_machines(bf, time, self, effects):
    effects.remove(self)
    bf.w1.dmg = int(bf.w1.dmg*1.03)
    bf.w2.dmg = int(bf.w2.dmg*1.03)
    
def auto_reloaders(bf, time, self, effects):
    effects.remove(self)
    bf.w1.reload = int(bf.w1.reload*0.97)
    bf.w2.reload = int(bf.w2.reload*0.97)
    bf.w1.reload_wait = bf.w1.reload
    bf.w2.reload_wait = bf.w2.reload

    
def cryo_ammo(bf, time, self, effects): #per shot? 
    effects.remove(self)
    def cryo_ammo(weapon, bf, enemy, dmg, hit):
        if hit:
            enemy.w1.reload_wait += int(0.25*1e3)
            enemy.w2.reload_wait += int(0.25*1e3)
    bf.w1.effects.append(cryo_ammo)
    bf.w2.effects.append(cryo_ammo)