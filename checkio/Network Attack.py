def capture(matrix):
    comps = {}
    for i in range(len(matrix)):
        comps[i] = [];
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == matrix[j][i] == 1:
                comps[i] += [j];
    infect_status = {i: 'false' for i in comps}
    infect_status[0] = 'true'
    notinfected = len(matrix)
    count = 0
    while (notinfected > 1):
        infected = set()
        count += 1
        for comp in infect_status:
            if infect_status[comp] == 'true':
                for i in comps[comp]:
                    infected.add(i)
        for c in infected:
            matrix[c][c] -= 1
            if matrix[c][c] == 0:
                notinfected -= 1
                infect_status[c] = 'true'
    return count




if __name__ == '__main__':
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
