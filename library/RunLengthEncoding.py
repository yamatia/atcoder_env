from itertools import groupby
def runLengthEncode(S: str)->list:
    '''
    str to list(tuple).required itertools.groupby
    '''
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, len(list(v))))
    return res