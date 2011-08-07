import yaml

from math import ceil

# ------------------------------------------------------------------------------

import yamlSafeLoader

# ==============================================================================

class Character(object):
    """Represents a BESM character configuration."""
    
    # Our whitelist for yamlSafeLoader.
    yaml_whitelist = [
        "name",
        "age",
        "genre",
        "notes",
        
        "race",
        "height",
        "weight",
        
        "character_points",
        "skill_points",
        
        "body",
        "mind",
        "soul"
    ]
    
    # -------------------------------------------------------------------------
    
    def __init__(self):
        # Character information
        self.name = ""
        self.age = ""
        self.genre = "Cyberpunk"
        self.notes = ""
                
        # Appearance attributes
        self.race = ""
        self.height = ""
        self.weight = ""
        
        # Points
        self.character_points = 20
        self.skill_points = 20
        
        # Stats
        self.body = 1
        self.mind = 1
        self.soul = 1
        
        # Modifiers
        self.skills = []
    
    # --------------------------------------------------------------------------
    
    def get_remaining_character_points(self):
        """Returns the remaining character points, as the name suggests"""
        return self.character_points - (self.body + self.mind + self.soul)
        
    # --------------------------------------------------------------------------
    
    def get_health(self):
        """Returns HP based on stats.
        
        HP = (Body + Soul) * 5
        """
        return (self.body + self.soul) * 5
        
    def get_energy(self):
        """Returns energy based on stats.
        
        Energy = (Mind + Soul) * 5
        """
        return (self.mind + self.soul) * 5
        
    def get_shock(self):
        """Returns shock value based on stats.
        
        Shock = (HP / 5) (rounded up)
        """
        return int(ceil(self.get_health() / 5.0))
        
    def get_combat(self):
        """Returns combat value based on stats.
        
        Combat = (Body + Mind + Soul) / 3 (rounded up)
        """
        return int(ceil((self.body + self.mind + self.soul) / 3.0))
        
    def get_defense(self):
        """Returns defense value based on stats.
        
        Defense = (Combat - 2)
        """
        return self.get_combat() - 2
        
    # --------------------------------------------------------------------------
    
    def save(self, filename):
        """Saves the character as a YAML file"""     
        stream = file(filename, 'w')
        yaml.dump(self, stream)

# ==============================================================================

def load(filename):
    """A wrapper for yamlSafeLoader, passes our class to it."""
    return yamlSafeLoader.load(filename, Character, Character.yaml_whitelist)
        