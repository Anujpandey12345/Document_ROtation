import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import cv2



class OrientationModel:

    def __init__(self):
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        print(f"Using device: {self.device}")
        self.model = models.resnet18(weights=None)
        num_features = self.model.fc.in_features
        self.model.fc = torch.nn.Linear(num_features, 4)

        torch.save(
            self.model.state_dict(),
            "models/orientation_model.pth"
        )

        print("Model Saved Successfully")

        self.model.to(self.device)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

        self.class_to_angle = {
            0: 0,
            1: 90,
            2: 180,
            3: 270,
        }
        print("Orientation Model Loaded Successfully")

    def predict(self, image):
        print("STEP 1")

        image_rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        print("STEP 2")

        pil_image = Image.fromarray(image_rgb)

        print("STEP 3")

        tensor = self.transform(pil_image)

        print("STEP 4")

        tensor = tensor.unsqueeze(0)

        print("Tensor Shape:", tensor.shape)

        print("STEP 5")

        tensor = tensor.to(self.device)

        print("STEP 6")

        with torch.no_grad():

            outputs = self.model(tensor)

            print("STEP 7")

            prediction = torch.argmax(
                outputs,
                dim=1
            )

            prediction = prediction.item()

        print("STEP 8")
