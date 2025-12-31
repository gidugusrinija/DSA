"""
You get a string morsecode made of "." and "-".
You can perform one move only:

👉 Replace any two consecutive characters with the opposite pattern:

".." → "--"

"--" → ".."

You must return all possible strings you can get by doing exactly ONE such replacement.

If no ".." or "--" exists → return empty list.
"""

morsecode = "...."


def possible_morsecodes(morsecode):
    res = []
    for i in range(len(morsecode) - 1):
        new_code = None
        pair = morsecode[i:i + 2]
        if pair == "..":
            new_code = morsecode[:i] + "--" + morsecode[i + 2:]
        # elif pair == "--":
        #     new_code = morsecode[:i] + ".." + morsecode[i + 2:]
        res.append(new_code)

    return res


x = possible_morsecodes(morsecode)
srinija = "srinija"
print(srinija[:2])
print(x)
