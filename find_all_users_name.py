from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    names = []
    for msg in data['messages']:
        name = msg.get('actor', False)
        if name:
            if name not in names:
                names.append(name)
        name = msg.get('from', False)
        if name:
            if name not in names:
                names.append(name)
            
    return (names)
        
   
    return i
print(find_all_users_name(read_data('data/result.json')))