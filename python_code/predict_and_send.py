import serial
import time
import numpy as np
from tensorflow.keras.models import load_model
import cv2

# Load the trained model
model = load_model('your_model.h5')  # Replace with your actual model path
model.summary()  # Check the model summary
number= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Function to send predicted number via serial port
def send_predicted_number(image_path, serial_port):
    # Load and preprocess the image

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img.reshape((1, 28, 28, 1))

    # Make predictions
    predictions = model.predict(img)[0][:]
    print("Prediction Dimensions:", predictions)
    Max_Prediction = np.where(predictions == max(predictions))[0][0]
    print(number[Max_Prediction])

    #predicted_number = np.argmax(predictions)

    # Send predicted number via serial port
    serial_port.write(str(Max_Prediction).encode())
    #print(f"Predicted Number sent: {predicted_number}")

arduino_serial = serial.Serial('COM4', 9600)
time.sleep(3)

# Replace 'your_image_path.jpg' with the actual path to your image file
image_path = 'img_989.jpg'

# Send the predicted number via serial port
send_predicted_number(image_path, arduino_serial)

# Close the serial port
arduino_serial.close()