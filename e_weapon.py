def proton_blaster(w, bf, enemy, dmg, hit):
    if hit:
        enemy.armor = max(0, int(enemy.armor - 0.5*1e3))
        
def hunter_missles(w, bf, enemy, dmg, hit):
    if not hit:
        dmg["rng"] += 1
        
def micro_rocket_pods(w, bf, enemy, dmg, hit):
    if not hit:
        dmg["rng"] += 0.1
        
def howitzer(w, bf, enemy, dmg, hit):
    if not hit and bf.shield > 0:
        dmg["dmg"] = int(dmg["dmg"]*1.15)
        
def mining_laser(w, bf, enemy, dmg, hit):
    if hit:
        enemy.armor = max(0, int(enemy.armor - 0.5*1e3))
        
def autocannon(w, bf, enemy, dmg, hit):
    if not hit and bf.shield > 0:
        dmg["dmg"] = int(dmg["dmg"]*1.5)