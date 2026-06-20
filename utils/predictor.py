import sqlite3
import joblib

from utils.Similarity import calculate_distance

model = joblib.load("model.pkl")

THRESHOLD = 20

def search_database(db_path, features):

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT area,
           bedrooms,
           bathrooms,
           age,
           location,
           price
    FROM houses
    """)

    rows = cursor.fetchall()

    best_price = None
    best_distance = 999999

    for row in rows:

        db_features = row[:-1]

        distance = calculate_distance(
            features,
            db_features
        )

        if distance < best_distance:

            best_distance = distance
            best_price = row[-1]

    conn.close()

    if best_distance < THRESHOLD:
        return best_price

    return None


def save_prediction(features, price):

    conn = sqlite3.connect("databases/test.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO houses
    (
    area,
    bedrooms,
    bathrooms,
    age,
    location,
    price
    )
    VALUES (?,?,?,?,?,?)
    """,
    (
    features[0],
    features[1],
    features[2],
    features[3],
    features[4],
    price
    ))

    conn.commit()
    conn.close()


def predict_house(features):

    train_result = search_database(
        "databases/train.db",
        features
    )

    if train_result is not None:

        return {
            "source": "train_database",
            "price": train_result
        }

    test_result = search_database(
        "databases/test.db",
        features
    )

    if test_result is not None:

        return {
            "source": "test_database",
            "price": test_result
        }

    price = model.predict([features])[0]

    save_prediction(
        features,
        float(price)
    )

    return {
        "source": "ml_model",
        "price": float(price)
    }