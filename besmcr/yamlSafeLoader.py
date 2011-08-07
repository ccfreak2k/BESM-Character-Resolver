import yaml

# ==============================================================================

def load(filename, cls, whitelist=None):
    """Safely loads a YAML object of type cls
    
    Loads the YAML file passes by filename, which is assumed to contain
    serialised cls instance. It then makes a new real instance of cls and copies
    over whitelisted attributes if specified, and only if the real class has
    them.
    
    The result is a clean, safely loaded object, in theory.
    """
    
    # load the file for reading and grab the yaml version
    stream = file(filename, 'r')
    yaml_obj = yaml.load(stream)
    
    # make an instance of the object we actually want
    real_obj = cls()
    
    # loop through everything in it's namespace
    for attr in dir(yaml_obj):
        if whitelist:
            if not attr in whitelist:
                continue
                
        # check if it's in our own version, ignore otherwise
        if not hasattr(real_obj, attr):
            continue
            
        # check if it's not a function or private or if it's not the
        # same type as ours, ignore otherwise
        if attr[:2] == "__":
            continue
        if callable(yaml_obj.__getattribute__(attr)):
            continue
        if not type(real_obj.__getattribute__(attr)) == type(
            yaml_obj.__getattribute__(attr)):
            continue
                
        # basically copy it into our version of character
        real_obj.__setattr__(attr, 
            yaml_obj.__getattribute__(attr))
            
    # return dat new shiny object
    return real_obj