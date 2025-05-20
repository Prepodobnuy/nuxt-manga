import os


def contains_ignore(path: str, ignore: list[str]):
    for i in ignore:
        if i in path:
            return True
    return False


def collect_files(dir: str, ignore: list[str]):
    res = []

    for file in os.listdir(dir):
        path = f"{dir}/{file}"
        if os.path.isdir(path):
            res += collect_files(path, ignore)
            continue
        if not contains_ignore(path, ignore):
            res.append(path)

    return res


def replace(fr: str, to: str, path: str):
    with open(path, "r") as file:
        data = file.read()

    if fr in data:
        data = data.replace(fr, to)
        with open(path, "w") as file:
            file.write(data)


path = os.path.abspath("./server/models")

f = collect_files(path, ["__pycache__"])

for i in f:
    replace(
        "(Base)",
        "(Base):",
        i,
    )
