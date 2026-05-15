from concurrent.futures import ThreadPoolExecutor
from config import INPUT_DIR, OUTPUT_DIR, MAX_WORKERS
from logger import logger
from image_processor import resize_image, rotate_image, process_image
from utils import create_folder, get_image_path


def main():
    logger.info("Pipeline started!")
    create_folder(OUTPUT_DIR)
    image_paths = get_image_path(INPUT_DIR)

    if len(image_paths) == 0:
        print("No image Found!\n")
        logger.error(f"No image found in input folder!")
        return
    

    print(f"Total images are in Input folder is: {len(image_paths)}")

    for image_path in image_paths:
        process_image(image_path)

    logger.info(f"Pipeline completed")
    print("\nPipeline Completed Successfully")

if __name__ == "__main__":
    main()
