import string
import keyword


def is_valid_variable_name(name):

    if name in keyword.kwlist:
        return False


    if name.count('_') > 1:
        return False


    if name[0].isdigit():
        return False


    if any(char.isupper() for char in name):
        return False


    invalid_chars = set(string.punctuation.replace('_', '') + ' ')
    if any(char in invalid_chars for char in name):
        return False

    return True



user_input = input("Введіть рядок для перевірки: ")


result = is_valid_variable_name(user_input)


print(result)