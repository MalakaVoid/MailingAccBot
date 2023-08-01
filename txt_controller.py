from globals import groups_to_add


def get_groups():
    f = open('groups.txt')
    for line in f:
        added_line = line.replace("\n", "")
        if "https://t.me/+" not in added_line:
            added_line = added_line.replace("https://t.me/", "")
        groups_to_add.append(added_line)
    f.close()
    f = open('groups.txt', "w")
    f.write("")
    f.close()

def remake_group_file(arr):
    f = open('groups.txt', 'a')
    for i in arr:
        f.write(f"{i}\n")
    f.close()


def add_group(group: str):
    f = open('groups.txt', 'a')
    f.write(f"{group}\n")
    f.close()
