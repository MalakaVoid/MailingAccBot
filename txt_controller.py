from globals import groups_to_add


def get_groups():
    f = open('groups.txt')
    for line in f:
        added_line = line.replace("\n", "")
        added_line = added_line.replace("https://t.me/", "")
        groups_to_add.append(added_line)
    f.close()


def add_group(group: str):
    f = open('groups.txt', 'a')
    f.write(f"{group}\n")
    f.close()
