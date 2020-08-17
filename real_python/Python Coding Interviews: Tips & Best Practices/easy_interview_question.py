def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 1, 2, 3, 4])
    []
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([1])
    [0]
    '''
    # find majority element
    # if there is no majority element, return []
    # find the indexes of the majority element,
    # put them in a lst
    from math import floor
    from collections import Counter

    # if lst == []:
    #     return []
    # count = Counter(lst)
    # top_elems = sorted(
    #     count.keys(),
    #     key=lambda x: -count[x]
    # )
    # maj_elem = top_elems[0]
    # # Top elem doesn't have majority count
    # if count[maj_elem[0]] <= len(lst) // 2:
    #     return []
    # return [
    #     i for i, elem in enumerate(lst)
    #     if elem == maj_elem
    # ]

    # ----------------------------------------------

    # if lst == []:
    #     return []
    # count = Counter(lst)
    # max_count = max(count.values())
    # maj_elems = [
    #     elem for elem, count
    #     in count.items() if count == max_count
    # ]
    # # Top two elems have same count
    # # or top elem doesn't have majority count
    # if (
    #     len(maj_elems) > 1
    #     or count[maj_elems[0]] <= len(lst) // 2
    # ):
    #     return []
    # return [
    #     i for i, elem in enumerate(lst)
    #     if elem == maj_elems[0]
    # ]

    # ----------------------------------------------

    # Versão mais perfeita
    # if lst:
    #     most_frequent_elem, n = Counter(lst).most_common(1)[0]
    #     if n > len(lst) // 2:
    #         return [k for k, x in enumerate(lst) if x == most_frequent_elem]
    # return []

    # ----------------------------------------------

    # Outra versão minha. Feia mas mais eficiente em casos de múltiplos números majoritários
    # common = Counter(lst).most_common(1)
    # lista = []
    # if common[0][1] > appearence_limit:
    #     for index, number in enumerate(lst):
    #         if number == common[0][0]:
    #             lista.append(index)
    # return lista
    
    # ----------------------------------------------

    # Minha versão final.
    mininum_appearences = floor(len(lst) / 2)

    if lst:
        return [
            index for index, number in enumerate(lst) 
            if lst.count(number) > mininum_appearences
        ]
    return []

    

print(majority_element_indexes([1, 3, 5, 4, 5, 5, 5]))
print(majority_element_indexes([1, 1, 2]))
print(majority_element_indexes([1, 1, 2, 3, 4]))
print(majority_element_indexes([1, 2]))
print(majority_element_indexes([1]))
