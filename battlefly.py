import random

class Weapon():
    def __init__(self, burst, dmg, reload, effects, me=None, name="", enemy=None):
        """
        - me: BF with this weapon
        - enemy: The BF this weapon is firing upon
        - effects: list of functions with signature (me, enemy) 
        """
        self.reload = reload
        self.reload_wait = reload
        self.me = me
        self.enemy = enemy
        self.burst = burst
        self.dmg = dmg
        self.effects = effects
        self.name = name
        
    def fast_forward_time_by(self, s):
        """
        speeds up reload by s seconds and fire if reload reaches 0
        """
        self.reload_wait -= s
        while self.reload_wait <= 0:
            self.reload_wait += self.reload
            self.shoot_at_enemy()
        
    def shoot_at_enemy(self):
        # Reduce enemy health
        attacked = False
        for _ in range(self.burst):
            dmg_obj = {"dmg":self.dmg, "rng":random.uniform(0, 1)}
            for e in effects:
                e(self, me, enemy, dmg_obj, False)
            if dmg_obj["rng"]>enemy.evasion_chance:
                attacked = True
                if enemy.shield>0:
                    enemy.shield -= (dmg_obj["dmg"]-enemy.armor*1e3)  # Question: what happens if more damage for shield but have left over?
                else:
                    enemy.hull -= (dmg_obj["dmg"]-enemy.armor*1e3)
        e(self, me, enemy, {"dmg":0, "rng":0}, attacked)
    
    def add_owner(self, bf):
        self.me = bf
        
    def add_enemy(self, bf):
        self.enemy = bf
        
    def remove_enemy(self):
        self.enemy = None
    
class Utility():
    def __init__(self, effects, name="", me=None):
        self.me = me
        self.effects = effects[:]
        self.active_effects = effects[:]
        self.name = name
            
    def apply_effects(self, elapsed_time):
        for e in self.active_effects:
            e(self.me, elapsed_time, e, self.active_effects)
            
    def add_owner(self, bf):
        self.me = bf
        for e in self.active_effects:
            e(self.me, 0, e, self.active_effects)
            
    def reset_effects(self):
        self.active_effects = self.effects[:]
    
        
class Battlefly():
    def __init__(self, w1, w2, u1, u2, traits=[], wins=0, battles=0):
        self.max_hull = 400
        self.max_shield = 200
        self.traits = traits
        self.w1 = w1
        self.w2 = w2
        self.u1 = u1
        self.u2 = u2
        self.reset_stats()
        self.wins = wins
        self.battles = battles
        
    def reloading_for(self):
        """returns how long till one weapon finishes reloading"""
        return min(self.w1.reload_wait, self.w2.reload_wait)
    
    def fast_forward_weapons(self, time):
        self.w1.fast_forward_time_by(time)
        self.w2.fast_forward_time_by(time)
        
    def fast_forward_utilities(self, time):
        self.u1.apply_effects(time)
        self.u2.apply_effects(time)
        
    def aim_at_enemy(self, enemy):
        self.w1.set_enemy(enemy)
        self.w2.set_enemy(enemy)
        
    def won_battle(self, times=1):
        self.wins += times
        self.battles += times
        
    def lost_battle(self, times=1):
        self.battles += times
        
    def reset_stats(self):
        self.hull = self.max_hull
        self.hull_regen_amt = 0
        self.shield = self.max_shield
        self.shield_regen = 0.01
        self.shield_regen_amt = self.shield * self.shield_regen
        self.armor = 0
        self.evasion_chance = 0.05
        self.dmg_multiplier = 1
        self.crit_chance = 0.05
        self.crit_dmg = 2
        self.u1.reset_effects()
        self.u2.reset_effects()
        self.w1.add_owner(self)
        self.w2.add_owner(self)
        self.u1.add_owner(self)        
        self.u2.add_owner(self)
        self.add_traits()
        
    def add_traits(self, traits=None):
        if traits:
            self.traits = traits
        for t in self.traits:
            t(self)

    def get_name(self):
        name = self.w1.name + "_" + self.w2.name + "_" + self.u1.name + "_" + self.u2.name + "_"
        name += f"{len(self.traits)}"
        for t in self.traits:
            name += f"_{t.__name__}"
        return name
        
    

        
