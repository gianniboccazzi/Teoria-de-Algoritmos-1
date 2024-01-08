from pulp import LpVariable, LpBinary, LpProblem, lpSum, LpMinimize, PULP_CBC_CMD
import time

def hitting_set_problem_pl(A, subconjuntos):
    time_start = time.time()
    prob = LpProblem("Hitting_Set", LpMinimize)
    variables_binarias = LpVariable.dicts("Variable", A, 0, 1, LpBinary)
    prob += lpSum(variables_binarias[i] for i in A)
    for subconjunto in subconjuntos:
        prob += lpSum(variables_binarias[j] for j in subconjunto) >= 1
    prob.solve(PULP_CBC_CMD(msg=False))
    time_end = time.time()
    return [jugador for jugador in A if variables_binarias[jugador].value() > 0], time_end - time_start

