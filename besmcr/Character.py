def Character(object):
    """Represents a BESM character configuration."""
    
    def __init__(self):
        # Character information
        self.name = u""
        self.age = u""
        self.notes = u""
                
        # Appearance attributes
        self.race = u""
        self.height = u""
        self.weight = u""
        
        # Available points
        self.character_points = 0
        self.skill_points = 0
        
        # Stats
        self.body = 0
        self.mind = 0
        self.soul = 0
        
        # Modifiers
        self.attributes = []
        self.skills = []
        
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
        
        Shock = (HP / 5) (rounded)
        """
        return int(round(self.get_health() / 5.0))
        
    def get_combat(self):
        """Returns combat value based on stats.
        
        Combat = (Body + Mind + Soul) / 3 (rounded)
        """
        return int(round((self.body + self.mind + self.soul) / 3.0))
        
    def get_defense(self):
        """Returns defense value based on stats.
        
        Defense = (Combat - 2)
        """
        return self.get_combat() - 2