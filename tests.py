import numpy as np
from main import pageRankPower, pageRankLinear, main, get_prob_matrix

if __name__ == '__main__':

    # Test get_prob_matrix
    m1 = np.array([[2, 1, 1],
                   [1, 0, 0.5],
                   [2, 2, 2]])
    expected = np.array([[0.5, 0.25, 0.25], [2 / 3, 0, 1 / 3], [1 / 3, 1 / 3, 1 / 3]])
    actual = get_prob_matrix(m1)
    if not np.array_equal(expected, actual):
        print('expected:', expected)
        print('actual:', actual)

    v = np.array([0.2,0.9,0.6])
    print(pageRankPower(m1, v=v))
    print(pageRankLinear(m1, v=v))






