from gendiff.formatters.utils import get_key_data, wrap_with_braces


def format_plain(diff_dict):
    def get_lines(diff, path):
        lines = []
        keys = sorted(diff.keys())

        for key in keys:
            change = diff[key]['type_of_change']
            value = diff[key]

            new_path = path + [key]
            formatted_path = '.'.join(new_path)

            if change == 'updated':
                old_type, new_type, old_val, new_val = get_key_data(change, 
                                                                    value, 
                                                                    True)
                old_value = old_val if old_type == 'flat_key' \
                    else '[complex value]'
                new_value = new_val if new_type == 'flat_key' \
                    else '[complex value]'

                lines.append(f"Property '{formatted_path}' was updated. "
                             f"From {old_value} to {new_value}")

            else:
                key_type, val = get_key_data(change, value, True)

                if change == 'intact' and key_type == 'nested_key':
                    lines.extend(get_lines(val, new_path))

                elif change == 'deleted':
                    lines.append(f"Property '{formatted_path}' was removed")

                elif change == 'added':
                    value_repr = val if key_type == 'flat_key' \
                        else '[complex value]'
                    lines.append(f"Property '{formatted_path}' \
                        was added with value: {value_repr}")

        return lines
            
    lines = get_lines(diff_dict, [])
    formatted_diff = wrap_with_braces(lines, 'plain')
    return formatted_diff