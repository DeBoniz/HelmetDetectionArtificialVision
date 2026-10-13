from inference_sdk import InferenceHTTPClient
from pathlib import Path
import os

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="BZ8QO9B9dGk0SzN7qB2o"
)

images_folder = Path("Full-Face Helmet 3445")  # Cambia con la tua cartella immagini
labels_folder = Path("label-full-face")
labels_folder.mkdir(exist_ok=True)

# Mappa le classi ai rispettivi ID YOLO (modifica se necessario)
class_map = {
    "Helmet": 0,
    "No_Helmet": 1,
    "Person": 2
}

for img_path in images_folder.glob("*.jpg"):
    result = CLIENT.infer(str(img_path), model_id="mytesttoukui/4")
    yolo_lines = []
    width = result["image"]["width"]
    height = result["image"]["height"]

    for prediction in result["predictions"]:
        class_name = prediction["class"]
        if class_name not in class_map:
            continue  # Salta classi sconosciute
        class_id = class_map[class_name]
        # Bounding box in pixel
        x, y, w, h = prediction["x"], prediction["y"], prediction["width"], prediction["height"]
        # Converti in formato YOLO (normalizzato)
        x_center = x / width
        y_center = y / height
        w_norm = w / width
        h_norm = h / height
        yolo_lines.append(f"{class_id} {x_center} {y_center} {w_norm} {h_norm}")

    # Salva il file .txt con lo stesso nome dell'immagine
    label_path = labels_folder / (img_path.stem + ".txt")
    with open(label_path, "w") as f:
        f.write("\n".join(yolo_lines))

    print(f"Annotazione YOLO salvata per {img_path.name}")

print("Annotazioni completate.")
