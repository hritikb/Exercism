def is_isogram(string):
    string = string.lower()
    
    string = string.replace('-', '').replace(' ', '')       # Replacing all hyphens and spaces with ''
    
    check = list(set(string))                   # set() returns a set object, 
                                                # so every element occurs only once in that
    
    if len(string) == len(check):
        return True
    
    return False