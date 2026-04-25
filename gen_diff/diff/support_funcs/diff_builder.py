

def build_diff(dict1, dict2):
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = []
    
    for key in all_keys:
        if key not in dict1:
            result.append({'key': key, 'type': 'added', 'value': dict2[key]})
        elif key not in dict2:
            result.append({'key': key, 'type': 'removed', 'value': dict1[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(dict1[key], dict2[key])
            })
        elif dict1[key] == dict2[key]:
            result.append({'key': key, 'type': 'unchanged', 'value': dict1[key]})
        else:
            result.append({
                'key': key, 
                'type': 'changed',
                'old_value': dict1[key], 
                'new_value': dict2[key]
            })
    
    return result