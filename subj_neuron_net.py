def neuron_net_test(test_data):
    import numpy as np
    import tensorflow as tf
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    import csv

    train_subj_data = []
    labels = []
    with open("train_subj_data.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            train_subj_data.append(list(map(float, row[:-1])))
            labels.append(float(row[-1]))

    train_subj_data = np.array(train_subj_data)
    labels = np.array(labels)
    scaler = MinMaxScaler()
    train_subj_data = scaler.fit_transform(train_subj_data)
    X_train, X_test, y_train, y_test = train_test_split(train_subj_data, labels, test_size=0.2, random_state=42)
    neuron_net = tf.keras.models.Sequential([
        tf.keras.layers.Dense(256, activation="relu", input_shape=(7,)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(1, activation="linear")
    ])

    neuron_net.compile(optimizer="adam", loss="mean_squared_error")
    neuron_net.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)
    loss = neuron_net.evaluate(X_test, y_test)

    test_data1 = np.array([test_data])
    test_data1 = scaler.transform(test_data1)
    prediction1 = neuron_net.predict(test_data1)
    return prediction1