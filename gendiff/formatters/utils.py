def get_formatted_value(value, add_quotes):
    if isinstance(value, bool):  
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str) and add_quotes:
        return f"'{value}'"
    return value


def get_key_data(type_of_change, key_values, add_quotes=False):
    if type_of_change == 'updated':
        return (
            key_values['old_key_type'],
            key_values['new_key_type'],
            get_formatted_value(key_values['old_value'], add_quotes),
            get_formatted_value(key_values['new_value'], add_quotes)
        )
    return (
        key_values['key_type'],
        get_formatted_value(key_values['value'], add_quotes)
    ) 


def wrap_with_braces(lines: list, format) -> str:
    if format == 'stylish' or format == 'json':
        return '{\n' + '\n'.join(lines) + '\n}'
    if format == 'plain':
        return '\n'.join(lines)