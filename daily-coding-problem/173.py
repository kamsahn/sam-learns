"""
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""

# if value is dictionary -> append key to parent key -> assign new value and repeat
# if value is not a dictionary -> do nothing




def flatten_dictionary(og: dict) -> dict:
    def helper(k: str, v: any) -> dict:
        ans = dict()
        if isinstance(v, dict):
            for subk, subv in v.items():
                newk = k + "." + subk
                subd = helper(newk, subv)
                for newsubk, newsubv in subd.items():
                    ans[newsubk] = newsubv
        else:
            ans[k] = v
        
        return ans
                    
    ans = dict()
    for k, v in og.items():
        newd = helper(k, v)
        for newk, newv in newd.items():
            ans[newk] = newv
    
    return ans


if __name__ == "__main__":
    d = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8,
                "ball": {
                    "d": 4
                }
            }
        }
    }
    print(flatten_dictionary(d))
