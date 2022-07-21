# OBJ ONE: read_template will return the first line in the string

def read_template(filepath):
    with open(filepath, "r") as temp:
        stripped_string = temp.read().strip()
    return stripped_string


# OBJ TWO: parse_template will return a stripped string and the parts that fit into the string.
# EX: taking the adjectives and noun out of the string

def parse_template(template):
    stripped = ""
    current_cap = ""
    capture = False
    parts = []
    for character in template:
        if character == "{":
            stripped += character
            capture = True
            current_cap = ""
        elif character == "}":
            stripped += character
            capture = False
            parts.append(current_cap)
        elif capture:
            current_cap += character
        else:
            stripped += character
    return stripped, tuple(parts)

# OBJ THREE: merge will take stripped string and seperated parts and
# combine them in the appropriate place
def merge(template, tple):
    return template.format(*tple)


