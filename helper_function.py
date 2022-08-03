def count_valid_posts(x):
    """count non-empty post blocks from the json file

    Args:
        x (dict): Json file load by json package. Json should have format:
        question -> str
        answers -> list of dicts
    """

    count = 0
    for i in x['answers']:
        if i:
            count += 1
    return count, len(x['answers'])

def get_claims(x, return_list_of_strings=True):
    """Get claims from Json file as described in Quora page

    Args:
        x (dict): Json file load by json package. Json should have format:
        question --> str
        answers --> list of dicts --> "claim"
        return_list (bool, optional): If true, return a list of claims. If false, return a list of dictionary objects. Defaults to True.

    Returns:
        list: a list of strings or a list of dict object (return_list=True)
    """
    # claim_object_list = []
    # for i in x['answers']:
    #     if i and i['claim'] != '': # filter out empty objects
    #         claim_object_list.append(i['claim'])
    # if return_list_of_strings:
    #     return [m['content'] for n in claim_object_list for m in n]
    # return claim_object_list
    return get_objects(x, return_list_of_string=return_list_of_strings, objects_type="claim")


def get_premises(x, return_list_of_strings=True):
    """Get premises from Json file as described in Quora pag

    Args:
        x (dict): Json file load by json package. Json should have the following format:
        'question' --> str
        'answers' --> <list of dicts> --> 'premise' --> <list of dicts>
        return_list_of_strings (bool, optional): If True, return a list of claims. If False, return a list of dict objects. Defaults to True.
    """
    return get_objects(x, return_list_of_string=return_list_of_strings, objects_type='premise')
    # premises_object_list = []
    # for i in x['answers']:
    #     if i:
    #         premises_object_list.append(i['premise'])
    # if return_list_of_strings:
    #     return [m['content'] for n in premises_object_list for m in n]
    # return premises_object_list

def get_objects(x, return_list_of_string=True, objects_type="claim"):
    """Retrive given objects from the Json file downloaded from Quora page

    Args:
        x (dict): Json file loaded by json package.
        return_list_of_string (bool, optional): If True, return a list of string; else, return a list of dict objects. Defaults to True.
        objects_type (str, optional): Should be "claim" or "premises". The type of string to extract. Defaults to "claim".
    """
    assert objects_type in ['claim', 'premise'], f"Your choise '{objects_type}' is not one of 'claim' or 'premise' "
    object_list = []
    for i in x['answers']:
        if i:
            object_list.append(i[objects_type])
    if return_list_of_string:
        return [m['content'] for n in object_list for m in n]
    return object_list
