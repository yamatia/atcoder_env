def is_ok(vec,idx,key):
    '''
    条件を満たすかどうか定義する
    '''
    if vec[idx]>=key:
        return True
    else:
        return False

def binarySearch(vec,key):
    ng = -1
    ok = len(vec)

    while (abs(ok-ng)>1):
        mid = (ok+ng)/2
        if is_ok(mid,key):
            ok = mid
        else:
            ng = mid

    return ok