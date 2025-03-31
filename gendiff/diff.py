def get_intact_key_info(key_value, nested_key=False) -> dict:
    if nested_key:
        return {
        'type_of_change': 'intact',
        'key_type': 'nested_key',
        'value': key_value
            }
    if isinstance(key_value, dict):
        return {
                'type_of_change': 'intact',
                'key_type': 'nested_key',
                'value': {
                    key: get_intact_key_info(value)
                    for key, value in key_value.items()
                }
            }
    return {
        'type_of_change': 'intact',
        'key_type': 'flat_key',
        'value': key_value
    }


def get_deleted_key_info(key_value) -> dict:
    if isinstance(key_value, dict):
        return {
            'type_of_change': 'deleted',
            'key_type': 'nested_key',
            'value': {
                key: get_intact_key_info(value) 
                for key, value in key_value.items()
                }
        }
    return {
        'type_of_change': 'deleted',
        'key_type': 'flat_key',
        'value': key_value
    }


def get_added_key_info(key_value) -> dict:
    if isinstance(key_value, dict):
        return {
            'type_of_change': 'added',
            'key_type': 'nested_key',
            'value': {
                key: get_intact_key_info(value) 
                for key, value in key_value.items()
                }
        }
    return {
        'type_of_change': 'added',
        'key_type': 'flat_key',
        'value': key_value
    }


def get_updated_key_info(key_value1, key_value2):
    if isinstance(key_value1, dict) and isinstance(key_value2, dict):
        return {
            'type_of_change': 'updated',
            'old_value': {
                key: get_intact_key_info(value) 
                for key, value in key_value1.items()
            },
            'new_value': {
                key: get_intact_key_info(value) 
                for key, value in key_value2.items()
            },
            'old_key_type': 'nested_key',
            'new_key_type': 'nested_key'
        }
    if isinstance(key_value1, dict):
        return {
            'type_of_change': 'updated',
            'old_value': {
                key: get_intact_key_info(value) 
                for key, value in key_value1.items()
            },
            'new_value': key_value2,
            'old_key_type': 'nested_key',
            'new_key_type': 'flat_key'
        }
    if isinstance(key_value2, dict):
        return {
            'type_of_change': 'updated',
            'old_value': key_value1,
            'new_value': {
                key: get_intact_key_info(value) 
                for key, value in key_value2.items()
            },
            'old_key_type': 'flat_key',
            'new_key_type': 'nested_key'
        }
    return {
            'type_of_change': 'updated',
            'old_value': key_value1,
            'new_value': key_value2,
            'old_key_type': 'flat_key',
            'new_key_type': 'flat_key'
    }


def get_diff(first_dict: dict, second_dict: dict):
    def walk(dict1, dict2):
        diff_dict = {}

        deleted_keys = {
            key: value 
            for key, value in dict1.items() 
            if key not in dict2
        }
        if deleted_keys:
            for key, value in deleted_keys.items():
                diff_dict[key] = get_deleted_key_info(value)

        added_keys = {
            key: value 
            for key, value in dict2.items() 
            if key not in dict1
        }
        if added_keys:
            for key, value in added_keys.items():
                diff_dict[key] = get_added_key_info(value)

        commons_keys = [key for key in dict1.keys() if key in dict2]
        if commons_keys:
            for key in commons_keys:
                value1 = dict1[key]
                value2 = dict2[key]
                if value1 == value2:
                    diff_dict[key] = get_intact_key_info(value1)
                elif isinstance(value1, dict) and isinstance(value2, dict):
                    nested_diff = walk(value1, value2)
                    diff_dict[key] = get_intact_key_info(nested_diff, True)
                else:
                    diff_dict[key] = get_updated_key_info(value1, value2)

        sorted_diff_dict = dict(sorted(diff_dict.items()))
        return sorted_diff_dict
    return walk(first_dict, second_dict)