from pulp import LpVariable, LpBinary, LpProblem, lpSum, LpMinimize, LpContinuous, PULP_CBC_CMD
import time

def hitting_set_problem_pl_relajado(A, subconjuntos):
    time_start = time.time()
    prob = LpProblem("Hitting_Set", LpMinimize)
    variables_continuas = LpVariable.dicts("Variable", A, 0, 1, LpContinuous)
    prob += lpSum(variables_continuas[i] for i in A)
    for subconjunto in subconjuntos:
        prob += lpSum(variables_continuas[j] for j in subconjunto) >= 1
    prob.solve(PULP_CBC_CMD(msg=False))
    b = max([len(subconjunto) for subconjunto in subconjuntos])
    time_end = time.time()
    return [jugador for jugador in A if variables_continuas[jugador].value() >= 1/b], time_end - time_start
