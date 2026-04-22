
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


a = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}

b = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": 'null',
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}

c = build_diff(a, b)

# def recurs(data, path=''):
#   result = []
#   for i in data:
#     if isinstance(i, dict):
#       recurs(i)
#   return result



def recurs(j, path=''):
    res = []
    for i in j:
        if isinstance(i, list):
            res.extend(recurs(i, path))
        else:  # i — словарь
            current_key = i['key']
            full_path = f"{path}.{current_key}" if path else current_key

            if i['type'] == 'added':
              upd_value = i['value'] if not isinstance(i['value'], dict | list) else '[complex value]'
              res.append(f'Property {full_path} was added with value: {upd_value}')
            
            if i['type'] == 'removed':
              res.append(f'Property {full_path} was removed')

            if i['type'] == 'changed':
              upd_old_value = i['old_value'] if not isinstance(i['old_value'], dict | list) else '[complex value]'
              upd_new_value = i['new_value'] if not isinstance(i['new_value'], dict | list) else '[complex value]'
              res.append(f'Property {full_path} was updated. From {upd_old_value} to {upd_new_value}')

            if 'children' in i and isinstance(i['children'], list):
                res.extend(recurs(i['children'], full_path))

    return res


print('\n'.join(recurs(c)))

print(c)

