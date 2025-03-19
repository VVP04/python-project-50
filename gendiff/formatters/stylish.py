
def make_string(data1, data2):
    data1_keys = list(data1.keys())
    data2_keys = list(data2.keys())
    keys = []
    keys.extend(data1_keys)
    keys.extend(data2_keys)
    keys = sorted(set(keys))
    diff = ['{']
    for key in keys:
        if key in data1_keys and key in data2_keys:
            value1 = data1[key]
            value2 = data2[key]
            if value1 == value2:
                if isinstance(value1, bool):
                    value1 = str(value1).lower()
                    diff.append(f'    {key}: {value1}')
                else:
                    diff.append(f'    {key}: {value1}')
            else:
                if isinstance(value1, bool):
                    value1 = str(value1).lower()
                    value2 = str(value2).lower()
                    diff.append(f'  - {key}: {value1}')
                    diff.append(f'  + {key}: {value2}')
                else:
                    diff.append(f'  - {key}: {value1}')
                    diff.append(f'  + {key}: {value2}')
        else:
            if key in data1_keys:
                value1 = data1[key]
                if isinstance(value1, bool):
                    value1 = str(value1).lower()
                    diff.append(f'  - {key}: {value1}')
                else:
                    diff.append(f'  - {key}: {value1}')
            else:
                value2 = data2[key]
                if isinstance(value2, bool):
                    value2 = str(value2).lower()
                    diff.append(f'  + {key}: {value2}')
                else:
                    diff.append(f'  + {key}: {value2}')
    diff.append('}')
    result = '\n'.join(diff)
    return result
