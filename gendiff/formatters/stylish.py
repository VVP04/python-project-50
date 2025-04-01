def get_formatted_value(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def get_key_data(type_of_change, key_values):
    if type_of_change == 'updated':
        return (
            key_values['old_key_type'],
            key_values['new_key_type'],
            get_formatted_value(key_values['old_value']),
            get_formatted_value(key_values['new_value'])
        )
    return (
        key_values['key_type'],
        get_formatted_value(key_values['value'])
    ) 


def wrap_with_braces(lines: list) -> str:
    return '{\n' + '\n'.join(lines) + '\n}'


def format_stylish(diff_dict: dict) -> str:
    def get_lines(diff, indent_size):
        lines = []
        indent = ' ' * indent_size
        sign_indent = ' ' * (indent_size - 2)

        intact = '  '
        added = '+ '
        deleted = '- '

        keys = sorted(diff.keys())

        for key in keys:
            change = diff[key]['type_of_change']
            value = diff[key]

            if change == 'updated':
                old_key, new_key, old_val, new_val = get_key_data(change, value)

                if old_key == 'nested_key':
                    lines.append(f'{sign_indent}{deleted}{key}: {{')
                    lines.extend(get_lines(old_val, indent_size + 4))
                    lines.append(f'{indent}}}')
                else:
                    lines.append(f'{sign_indent}{deleted}{key}: {old_val}')

                if new_key == 'nested_key':
                    lines.append(f'{sign_indent}{added}{key}: {{')
                    lines.extend(get_lines(new_val, indent_size + 4))
                    lines.append(f'{indent}}}')
                else:
                    lines.append(f'{sign_indent}{added}{key}: {new_val}')

            else:
                key_type, val = get_key_data(change, value)

                prefix = added if change == "added" else \
                         deleted if change == "deleted" else \
                         intact

                if key_type == 'nested_key':
                    lines.append(f'{sign_indent}{prefix}{key}: {{')
                    lines.extend(get_lines(val, indent_size + 4))
                    lines.append(f'{indent}}}')
                else:
                    lines.append(f'{sign_indent}{prefix}{key}: {val}')

        return lines

    lines = get_lines(diff_dict, 4)
    formatted_diff = wrap_with_braces(lines)
    return formatted_diff