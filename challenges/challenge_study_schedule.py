from collections import Counter


def study_schedule(permanence_period, target_time):
    # validações
    if any(end < start for start, end in permanence_period):
        raise ValueError("Dados de permanência do usuário inválidos.")

    if target_time is None:
        raise ValueError("Insira um target time válido!")

    # algoritmo de busca
    permanence_result = []

    for i1, i2 in permanence_period:
        sequency = range(i1, i2 + 1)
        permanence_result.extend(sequency)

    counter = Counter(permanence_result)

    return counter[target_time]
