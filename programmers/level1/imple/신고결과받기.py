from collections import defaultdict


def solution(id_list, report, k):
    do_dict = dict()
    ed_dict = defaultdict(set)

    for i in id_list:
        do_dict[i] = 0

    for r in report:
        a, b = r.split()
        ed_dict[b].add(a)

    for v in ed_dict.values():
        if len(v) >= k:
            for i in v:
                do_dict[i] += 1

    return list(do_dict.values())
