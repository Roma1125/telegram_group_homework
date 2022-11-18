from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    a = []
    for d in data['messages']:
        aa = d.get('actor', False)
        if a:
            if aa not in a:
                a.append(aa)
        aa = d.get('from', False)
        if aa:
            if aa not in a:
                a.append(aa)
            
    return (a)


    
print(find_number_of_messages(read_data('data/result.json')))