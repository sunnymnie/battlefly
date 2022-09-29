UTILITY = {overclocking_protocols.__name__: overclocking_protocols}
WEAPON = {}
TRAIT = {}

def overclocking_protocols(bf, time, **kwargs):
    """requires self"""
    if bf.hull < 0.3:
        kwargs["effects"].remove(kwargs["self"])
        # buff me