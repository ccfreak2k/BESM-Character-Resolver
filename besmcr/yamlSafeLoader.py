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
    
    stream = file(filename, 'r')
    yaml_obj = yaml.load(stream)
    
    return safe_copy_attributes(yaml_obj, cls, whitelist)

# ------------------------------------------------------------------------------
    
def safe_copy_attributes(unsafe_obj, cls, whitelist=None):
    """Cleanly copies attributes from one object to another.
    
    Copies attributes from one instance of some type to another. However it only
    copies attributes specified in the whitelist, or if no whitelist is
    specified; copies only the attributes which the specified class has.
    """
   
    clean_obj = cls()
    
    # Loop through everything in the unsafe object's namespace.
    for attr in dir(unsafe_obj):
        if whitelist:
            if not attr in whitelist:
                continue
             
        # Check if it's supposed to be a private attribute.
        if attr[:2] == "__":
            continue

        if not hasattr(clean_obj, attr):
            continue      
        if callable(unsafe_obj.__getattribute__(attr)):
            continue
        if not type(clean_obj.__getattribute__(attr)) == type(
            unsafe_obj.__getattribute__(attr)):
            continue
                
        # Copy it into our cleaned object using the most horrible looking
        # functions ever.
        clean_obj.__setattr__(attr, 
            unsafe_obj.__getattribute__(attr))
            
    return clean_obj