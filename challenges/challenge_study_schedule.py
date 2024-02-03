from collections import Counter


def study_schedule(permanence_period, target_time):
    # validações
    if any(
        start is None
        or end is None
        or not isinstance(start, int)
        or not isinstance(end, int)
        for start, end in permanence_period
    ):
        return None

    if target_time is None:
        return None

    # algoritmo de busca
    permanence_result = []

    for i1, i2 in permanence_period:
        sequency = range(i1, i2 + 1)
        permanence_result.extend(sequency)

    counter = Counter(permanence_result)

    return counter[target_time]
