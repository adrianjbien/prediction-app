from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def cast_input(x, y, cat):
    x = float(x)
    y = float(y)
    cat = int(cat)
    return x, y, cat


def make_prediction(all_data, x, y):
    points = [[point['x'], point['y']] for point in all_data]
    categories = [point['cat'] for point in all_data]
    scaler = StandardScaler()
    scaler.fit(points)
    points = scaler.transform(points)
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(points, categories)

    point_to_predict = [[x, y]]
    point_to_predict = scaler.transform(point_to_predict)
    return int(neigh.predict(point_to_predict))