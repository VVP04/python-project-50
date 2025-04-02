from gendiff.formatters.utils import get_key_data, wrap_with_braces


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
    formatted_diff = wrap_with_braces(lines, 'stylish')
    return formatted_diff