import tensorflow as tf

# Generate some example data
x_train = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32)
y_train = tf.constant([2, 4, 6, 8, 10], dtype=tf.float32)

# Define the model
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, epochs=300)

# Make a prediction
x_new = tf.constant([[7], [8], [9]], dtype=tf.float32)  # Note the double brackets
prediction = model.predict(x_new)

# Print predictions for each input
for i, value in enumerate([7, 8, 9]):
    print(f'Prediction for {value}: {prediction[i][0]}')
