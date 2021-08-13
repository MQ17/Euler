import numpy as np
import scipy.linalg as la

# -----ROLL MATRIX-----
faces = 20
roll_probabilities = [(faces-abs(faces-i))/(faces**2) for i in range(1, faces*2)]
print(roll_probabilities)

roll_matrix = np.zeros((40, 40))
# For all 40 initial positions
for c in range(40):
    # For all possible movements
    for m in range(2, faces*2+1):
        r = (c+m)%40
        roll_matrix[r, c] += roll_probabilities[m-2]


# # -----DOUBLES MATRIX-----
# doubles_matrix = roll_matrix/faces + np.identity(40)*(faces-1)/faces
# print(roll_matrix[:, 0])
# print(doubles_matrix[:, 0])
# -----SPEEDING MATRIX-----
cube = faces**3
speeding_matrix = (cube-1)/cube*np.identity(40)
speeding_matrix[10, :] = 1/cube
speeding_matrix[10, 10] = 1

# -----JAIL MATRIX-----
# [30]
jail_matrix = np.identity(40)
jail_matrix[30, 30] = 0
jail_matrix[10, 30] = 1


# -----CHANCE MATRIX-----
# [7, 22, 36]
chance_matrix = np.identity(40)

chance_matrix[7, 7] = 3/8  # staying put
chance_matrix[[0, 5, 10, 11, 24, 39], 7] = 1/16  # going to various squares
chance_matrix[15, 7] = 1/8  # going to next railroad
chance_matrix[12, 7] = 1/16  # going to next utility
chance_matrix[4, 7] = 1/16  # going back three spaces

chance_matrix[22, 22] = 3/8
chance_matrix[[0, 5, 10, 11, 24, 39], 22] = 1/16
chance_matrix[25, 22] = 1/8
chance_matrix[28, 22] = 1/16
chance_matrix[19, 22] = 1/16

chance_matrix[36, 36] = 3/8
chance_matrix[[0, 10, 11, 24, 39], 36] = 1/16
chance_matrix[5, 36] = 3/16  # combined r1 and next r
chance_matrix[12, 36] = 1/16
chance_matrix[33, 36] = 1/16


# -----CHEST MATRIX-----
# [2, 17, 33]
chest_matrix = np.identity(40)

chest_matrix[2, 2] = 7/8  # staying put
chest_matrix[[0, 10], 2] = 1/16  # going to go or jail

chest_matrix[17, 17] = 7/8
chest_matrix[[0, 10], 17] = 1/16

chest_matrix[33, 33] = 7/8
chest_matrix[[0, 10], 33] = 1/16


# -----FINAL MATRIX-----
matrices = [speeding_matrix, jail_matrix, chance_matrix, chest_matrix]
final_matrix = roll_matrix
for matrix in matrices:
    final_matrix = np.matmul(matrix, final_matrix)

eigen_vector = la.eig(final_matrix)[1]
steady_state = eigen_vector[:, 0]
steady_state = steady_state/sum(steady_state)

probabilities = list(steady_state)
sorted_probabilities = probabilities.copy()
sorted_probabilities.sort(reverse=True)
highest_three = sorted_probabilities[:3]

for high in highest_three:
    print(probabilities.index(high))

print(probabilities[10])
print(probabilities[24])
print(probabilities[0])
