import json

# recursive patch function
def apply_patch(source, patch):
    for key, value in patch.items():

        # remove key if value is null
        if value is None:
            source.pop(key, None)

        # if both are dicts -> recursive patch
        elif key in source and isinstance(source[key], dict) and isinstance(value, dict):
            apply_patch(source[key], value)

        # otherwise replace/add
        else:
            source[key] = value

    return source


# read input
source = json.loads(input())
patch = json.loads(input())

# apply patch
result = apply_patch(source, patch)

# print compact JSON with sorted keys
print(json.dumps(result, separators=(',', ':'), sort_keys=True))