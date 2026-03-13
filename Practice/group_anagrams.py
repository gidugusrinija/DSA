from collections import defaultdict

def group_anagrams(inputs):

    groups = defaultdict(list)

    for input in inputs:
       res = "".join(sorted(input))
       groups[res].append(input)

    return list(groups.values())

inputs = ["ate", "xob", "eat", "tea", "box", "pen"]

print(group_anagrams(inputs))


def char_freq_map_grouping(inputs):

    grps = defaultdict(list)
    for word in inputs:

        cnt = [0] * 26

        for chr in word:
            cnt[ord(chr) - ord('a')] += 1

        grps[tuple(cnt)].append(word)

    return list(grps.values())


print(char_freq_map_grouping(inputs))
