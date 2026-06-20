import numpy as np

def calculate_distance(input_row, db_row):

    input_vector = np.array(input_row)

    db_vector = np.array(db_row)

    return np.linalg.norm(
        input_vector - db_vector
    )