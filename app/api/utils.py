
def ok(key, obj):
    return {"success": True, key: obj}

def fail(errors):
    return {"success": False, "errors": errors}


def filter_none(d):
    return {key:val for key, val in d.items() if val is not None}

