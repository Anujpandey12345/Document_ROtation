import cv2
import os
from logger import logger
from config import OUTPUT_DIR, RESIZE_HEIGHT, RESIZE_WIDTH
from model import OrientationModel
model = OrientationModel()

# def detect_orientation(filename):
#     """
#     Dummy orientation logic.
#     Replace this later with AI model / OCR logic.
#     """
#     filename = filename.lower()

#     if "90" in filename:
#         return 90
#     elif "180" in filename:
#         return 180
#     elif "270" in filename:
#         return 270
#     return 0

def resize_image(image):
    return cv2.resize(
        image,
        (RESIZE_WIDTH, RESIZE_HEIGHT)
    )

def rotate_image(image, angle):
    

    if angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return image



def process_image(image_path):
    try:
        print("\n=================================")
        print("Processing:", image_path)
        filename = os.path.basename(image_path)
        logger.info(f"Processing started: {filename}")

        image = cv2.imread(image_path)

        print("Image Loaded: ", image is not None)
        if image is None:
            logger.error(f"failed to read image: {filename}")
            return
        
        image = resize_image(image)
        print("Image Resized")
        angle = model.predict(image)
        print("Predicted Angle:", angle)
        logger.info(f"Predicted Angle: {angle}")
        rotated_image = rotate_image(image, angle)
        print("Rotation Done")
    

        output_path = os.path.join(OUTPUT_DIR, filename)
        print("Saving To:", output_path)
        cv2.imwrite(output_path, rotated_image)
        print("IMAGE SAVED SUCCESSFULLY")

        logger.info(
            f"Successfully processed: {filename} | Rotation: {angle}"
        )
        print(f"Processed: {filename}")

    except Exception as e:

        logger.error(
            f"Error processing {image_path}: {e}"
        )

        print("\nERROR OCCURRED")
        print(e)




