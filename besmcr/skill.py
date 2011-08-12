import yaml

# ==============================================================================

class Skill(yaml.YAMLObject):
    """Represents a skill in BESM."""

    yaml_tag = "Skill"
    
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# ------------------------------------------------------------------------------

class SkillList(yaml.YAMLObject):
    """Represents a list of BESM skills."""

    yaml_tag = "SkillList"
    
    def __init__(self, x):
        self.container = []

    # --------------------------------------------------------------------------

    def add(self, item):
        self.container.append(item)
        
    def find_by_name(self, name):
        for s in self.container:
            if s.name == name:
                return s
            
    # --------------------------------------------------------------------------
        
    def __getitem__(self, key):
        return self.container[key]
        
    def __setitem__(self, key, value):
        self.container[key] = value
        
    def __delitem__(self, key):
        del self.container[key]
        
    def __iter__(self):
        return iter(self.container)
        
    def __reversed__(self):
        return reversed(self.container)
        
    def __contains__(self, item):
        return item in self.container
        
    # --------------------------------------------------------------------------

    def save(self, filename):
        """Saves the list of skills to a YAML file."""
        stream = file(filename, 'w')
        yaml.dump(self, stream)

# ==============================================================================

def load_list(filename):
    """Loads a skill list from a YAML file and returns it."""
    stream = file(filename, 'w')
    return yaml.load(stream)

