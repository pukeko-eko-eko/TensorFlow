import tensorflow as tf

print("Tensorflow version:", tf.__version__)

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0           # scale data

model = tf.keras.models.Sequential([                        # define model
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    ])

predictions = model(x_train[:1]).numpy()                    # look at the first predictions
#predictions

tf.nn.softmax(predictions).numpy()                          # run predictions through a SoftMax layer

# define a loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()

# compile the model
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# fit the model to the training data
model.fit(x_train, y_train, epochs=5)

# evaluate the performance of the model
model.evaluate(x_test, y_test, verbose=2)

probability_model = tf.keras.Sequential([
                        model,
                        tf.keras.layers.Softmax()

probability_model(x_test[:5])


