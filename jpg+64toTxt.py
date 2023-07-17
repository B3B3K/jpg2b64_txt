import cv2
import numpy as np
import base64

# Load the image
image_path = "test_r.jpg"
image = cv2.imread(image_path)
h, w, _ = image.shape



# Print the height and width
print(f"Height (h): {h} pixels")
print(f"Width (w): {w} pixels")
# Define the size of each split area
split_size = 10

# Get the dimensions of the image
height, width, _ = image.shape

# Create an empty list to store the average color and coordinates of each split area
split_areas = []

# Iterate over the image in split_size intervals
for y in range(0, height, split_size):
    for x in range(0, width, split_size):
        # Calculate the coordinates of the split area
        x1 = x
        y1 = y
        x2 = x + split_size
        y2 = y + split_size

        # Extract the split area from the image
        split_area = image[y1:y2, x1:x2]

        # Calculate the average color of the split area
        average_color = np.mean(split_area, axis=(0, 1))

        # Store the average color and coordinates in the list
        split_areas.append((x1, y1, x2, y2, average_color))

# Write the coordinates and average color of each split area to a text file
output_file = "split_areas.txt"
with open(output_file, "w") as file:
    with open(image_path, "rb") as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)
        file.write("DATE: ")
        file.write("\nJPG:")
        file.write(str(base64_data).replace("\n",""))
        file.write("\n")

    for i, (x1, y1, x2, y2, color) in enumerate(split_areas):
        file.write(f"Split Area {i+1}:\n")
        file.write(f"Coordinates: ({x1}, {y1}) - ({x2}, {y2})\n")
        
        # Convert the average color values from float to integer
        color_int = color.astype(int)
        file.write(f"Average Color (RGB): {color_int}\n")
        file.write("\n")
    file.close()
    