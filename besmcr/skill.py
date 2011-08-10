import yaml

# ==============================================================================

class Skill(object):
    """Represents a skill in BESM."""
    
    def __init__(self, name, cost):        
        self.name = name
        self.cost = cost
        
# ------------------------------------------------------------------------------

class SkillList(list):
    """Represents a list of BESM skills."""
    
    def __init__(self, x):
        """Overridden constructor for our class."""  
        super(SkillList, self).__init__(x)
        
    # --------------------------------------------------------------------------
        
    def save(self, filename):
        """Saves the list of skills to a YAML file."""
        pass
        
# ==============================================================================

def load(filename):
    """Loads a skill list from a YAML file and returns it."""
    pass
    