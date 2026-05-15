import os 

def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)

def get_image_path(folder_path):
    valid_extensions = [".jpg", ".jpeg", ".png"]

    image_paths = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)


        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()


            if ext in valid_extensions:
                image_paths.append(file_path)

    return image_paths

