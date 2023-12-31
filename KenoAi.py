import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from art import text2art

# Generate ASCII art with the text "KenoAi"
ascii_art = text2art("KenoAi")

print("============================================================")
print("KenoAi")
print("Created by: Corvus Codex")
print("Github: https://github.com/CorvusCodex/")
print("Licence : MIT License")
print("Support my work:")
print("BTC: bc1q7wth254atug2p4v9j3krk9kauc0ehys2u8tgg3")
print("ETH & BNB: 0x68B6D33Ad1A3e0aFaDA60d6ADf8594601BE492F0")
print("Buy me a coffee: https://www.buymeacoffee.com/CorvusCodex")
print("============================================================")

# Print the generated ASCII art
print(ascii_art)
print("Keno prediction artificial intelligence")

# Load data from file, ignoring white spaces and accepting unlimited length numbers
data = np.genfromtxt('data.txt', delimiter=',', dtype=int)

# Replace all -1 values with 0
data[data == -1] = 0

train_data = data[:int(0.8*len(data))]
val_data = data[int(0.8*len(data)):]

max_value = 80

# Get the number of features from the data
num_features = train_data.shape[1]

model = keras.Sequential()
model.add(layers.Embedding(input_dim=max_value+1, output_dim=64))
model.add(layers.LSTM(256))
model.add(layers.Dense(num_features, activation='softmax'))  # Set the number of units to match the number of features

# Define the learning rate schedule
lr_schedule = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=1e-2,
    decay_steps=10000,
    decay_rate=0.9)

# Use Adam optimizer with learning rate schedule
optimizer = keras.optimizers.Adam(learning_rate=lr_schedule)

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

history = model.fit(train_data, train_data, validation_data=(val_data, val_data), epochs=100)

predictions = model.predict(val_data)

indices = np.argsort(predictions, axis=1)[:, -num_features:]
predicted_numbers = np.take_along_axis(val_data, indices, axis=1)

print("============================================================")
print("Predicted Numbers:")
for numbers in predicted_numbers[:10]:
    print(', '.join(map(str, numbers)))

print("============================================================")
print("If you won buy me a coffee: https://www.buymeacoffee.com/CorvusCodex")
print("Support my work:")
print("BTC: bc1q7wth254atug2p4v9j3krk9kauc0ehys2u8tgg3")
print("ETH & BNB: 0x68B6D33Ad1A3e0aFaDA60d6ADf8594601BE492F0")
print("Buy me a coffee: https://www.buymeacoffee.com/CorvusCodex")
print("============================================================")

# Prevent the window from closing immediately
input('Press ENTER to exit')
