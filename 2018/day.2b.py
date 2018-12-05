#!/usr/bin/env python3

def execute():
    with open('input.2.txt') as inp:
        lines = inp.readlines()
    return match_bar_one([l.strip() for l in lines if len(l.strip()) > 0])

def partial_match(s1, s2, length):
    return s1 != s2 and sum([a == b for (a,b) in zip(s1[:length], s2[:length])]) >= length - 1 
    # s1[0] == s2[0] or s1[1] == s2[1]

def match_bar_one_cl(candidate_lists, length):
    if length > len(candidate_lists[0][0]):
        return "ERROR"

    if length == len(candidate_lists[0][0]):
        return candidate_lists
    
    unmatched = []
    
    for cl in candidate_lists:
        for box_id in cl[1:]:
            if not partial_match(box_id, cl[0], length):
                unmatched.append(box_id)
        for um in unmatched:
            if um in cl:
                cl.remove(um)
    
    # print(unmatched)
    
    for um in unmatched:
        matched = False
        for cl in candidate_lists:
            if partial_match(um, cl[0], length):
                matched = True
                cl.append(um)
        if not matched:
            candidate_lists.append([um])
    candidate_lists = [cl for cl in candidate_lists if len(cl) > 1]
    # print(length, candidate_lists)
    return match_bar_one_cl(candidate_lists, length+1)
        
def remove_unique(s1, s2):
    return ''.join([a for (a, b) in zip(s1, s2) if a == b])

def match_bar_one(box_ids):
    candidate_lists = [[box_ids[0]]]
    for box_id in box_ids[1:]:
        matched = False
        for cl in candidate_lists:
            if partial_match(box_id, cl[0], 2):
                matched = True
                cl.append(box_id)
        if not matched:
            candidate_lists.append([box_id])
    candidate_lists = [cl for cl in candidate_lists if len(cl) > 1]
    # print(candidate_lists)
    final_list = match_bar_one_cl(candidate_lists, 3)
    if len(final_list) > 1:
        return "Too many matches", final_list
    if len(final_list) < 1:
        return "No unique matches"
        
    return remove_unique(*final_list[0])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    boxes = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""
    verify(match_bar_one(boxes.split("\n")), "fgij")

if __name__ == "__main__":
    test_cases()
    print(execute())