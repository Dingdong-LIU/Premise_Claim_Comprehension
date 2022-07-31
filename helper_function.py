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
    claim_object_list = []
    for i in x['answers']:
        if i: # filter out empty objects
            claim_object_list.append(i['claim'])
    if return_list_of_strings:
        return [m['content'] for n in claim_object_list for m in n]
    return claim_object_list


