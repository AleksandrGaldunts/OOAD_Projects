def c3_linearization(class_hierarchy):
    result = []

    while class_hierarchy:
        head = class_hierarchy[0][0]
        if not any(head in tail[1:] for tail in class_hierarchy[1:]):
            result.append(head)
            class_hierarchy = [tail for tail in class_hierarchy if head != tail[0]]
        else:
            raise ValueError("Inconsistent hierarchy, cannot determine linearization.")

    return result

if __name__ == "__main__":
    hierarchy_1 = [
        ['D', 'B', 'A', 'C'],
        ['B', 'A'],
        ['C', 'A'],
        ['A']
    ]
    result_1 = c3_linearization(hierarchy_1)
    print("Linearization 1:", result_1)

    hierarchy_2 = [
        ['D', 'B', 'A', 'C'],
        ['B', 'A','E'],
        ['C', 'A'],
        ['A']
    ]
    result_2 = c3_linearization(hierarchy_2)
    print("Linearization 2:", result_2)

    #Linearization error
    hierarchy_3 = [
        ['D', 'B', 'A', 'C'],
        ['B', 'A', 'D'],
        ['C', 'A'],
        ['A']
        ]
    try:
        result_3 = c3_linearization(hierarchy_3)
        print("Linearization 3:", result_3)
    except ValueError as exp:
        print("Error:", exp)

a
