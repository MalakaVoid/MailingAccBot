from globals import groups_to_add


def get_groups():
    f = open('groups.txt')
    for line in f:
        added_line = line.replace("\n", "")
        added_line = added_line.replace("https://t.me/", "")
        groups_to_add.append(added_line)