# input "camelCaseString" 
# output "camel Case String"


def convertString(target_string):
    array_of_characters = []
    for char in target_string:
        if char.isupper():
            array_of_characters.append(' ')
        array_of_characters.append(char)
    print(''.join(array_of_characters).strip())


if __name__ == '__main__':
    try:
        convertString("camelCaseString")
    except Exception as e:
        print("Exeption", e)