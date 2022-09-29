import random

class Weapon():
    def __init__(self, burst, dmg, reload, effects=[], me=None, name="", enemy=None):
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
        
    def fast_forward_time_by(s):
        """
        speeds up reload by s seconds and fire if reload reaches 0
        """
        self.reload_wait -= s
        while self.reload_wait <= 0:
            self.reload_wait += self.reload
            self.shoot_at_enemy()
        
    def shoot_at_enemy():
        # Reduce enemy health
        for _ in range(self.burst):
            rng = random.uniform(0, 1)
            dmg = self.dmg
            for e in effects:
                dmg, rng = e(self, me, enemy, dmg, rng)
            if rng>enemy.evasion_chance:
                if enemy.shield>0:
                    enemy.shield -= dmg  # Question: what happens if more damage for shield but have left over?
                else:
                    enemy.hull -= dmg
    
    def add_owner(bf):
        self.me = bf
        
    def add_enemy(bf):
        self.enemy = bf
        
    def remove_enemy():
        self.enemy = None
    
class Utility():
    def __init__(self, effects=[], init_effects=[], name="", me=None):
        self.me = me
        self.effects = effects
        self.init_effects = init_effects
        self.name = name
            
    def apply_effects(elapsed_time):
        for e in self.effects:
            e(self.me, elapsed_time, self=e, effects=self.effects)
            
    def add_owner(bf):
        self.me = bf
        for e in self.init_effects:
            e(self.me, self.effects, self=e)
    
        
class Battlefly():
    def __init__(self, w1, w2, u1, u2, wins=0, battles=0):
        self.reset_stats()
        self.w1 = w1
        self.w2 = w2
        self.u1 = u1
        self.u2 = u2
        self.w1.add_owner(self)
        self.w2.add_owner(self)
        self.u1.add_owner(self)        
        self.u2.add_owner(self)
        self.wins = wins
        self.battles = battles
        self.traits = None
        
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
        self.hull = 400
        self.hull_regen_amt = 0
        self.shield = 200
        self.shield_regen = 0.01
        self.shield_regen_amt = self.shield * self.shield_regen
        self.armour = 0
        self.evasion_chance = 0.05
        self.dmg_multiplier = 1
        self.crit_chance = 0.05
        self.critdmg = 2
        self.add_traits()
        
    def add_traits(self, traits=None):
        if traits:
            self.traits = traits
        for t in traits:
            t(self)
    def get_name(self):
        name = self.w1.name + "_" + self.w2.name + "_" + self.u1.name + "_" + self.u2.name + "_"
        name += f"{len(self.traits)}"
        for t in self.traits:
            name += f"_{t.__name__}"
        return name
        
    

        
