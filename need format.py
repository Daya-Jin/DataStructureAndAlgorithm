def predictPartyVictory(senate: str) -> str:
    q_D, q_R = list(), list()
    n = len(senate)

    for idx, ch in enumerate(senate):
        if ch == 'R':
            q_R.append(idx)
        else:
            q_D.append(idx)

    while q_D and q_R:
        idx_D, idx_R = q_D.pop(0), q_R.pop()
        if idx_D < idx_R:
            q_D.append(idx_D + n)
        else:
            q_R.append(idx_R + n)

    return "Radiant" if q_R else 'Dire'


predictPartyVictory("DRDRR")