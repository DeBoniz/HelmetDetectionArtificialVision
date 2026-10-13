#  HelmetDetection

A deep learning project for automatic safety helmet detection using custom **YOLO / Ultralytics** models.

---

##  Directory Structure

```text
HelmetDetection/
├── AnnotationHelmet/
│   └── casco_env/              # Python virtual environment
├── datasetmodelloscelto/       # Primary dataset selected for training
├── datasets/                   # Additional support and testing datasets
├── ultralytics/                # YOLO framework, custom modifications, and configs
├── videotest/                  # Test videos for model inference
└── helmet_detection_report.md  # Comprehensive project report and summary
```

- **`AnnotationHelmet/`**: Contains annotation tools and management scripts. It also houses the **`casco_env/`** virtual environment required to run training, inference, and utility scripts.
- **`datasetmodelloscelto/`**: Contains the primary training dataset.
- **`datasets/`**: Contains auxiliary datasets for validation and experimentation.
- **`ultralytics/`**: Dedicated directory containing the customized **Ultralytics YOLO** framework, complete with modified modules and training configurations.
- **`videotest/`**: Contains test footage used to evaluate detection quality in realistic scenarios.
- **`helmet_detection_report.md`**: Detailed technical documentation covering model choices, loss curves, and comparative analysis.
- **Inference Samples**: 2 sample output videos processed with **`best.pt`** (the optimal checkpoint from training run 21) are available for evaluation.

---

##  Virtual Environment

Before running any script, training session, or inference task, activate the virtual environment:

```bash
source AnnotationHelmet/casco_env/bin/activate
```

To deactivate it:

```bash
deactivate
```

---

##  Usage

> **Important:** All commands below should be executed from within the `ultralytics/` directory with the virtual environment (`casco_env`) active.

```bash
cd ultralytics
```

### 1. Inference (Prediction on Images or Videos)

To perform object detection on an image or video file:

```bash
yolo task=detect mode=predict \
  model=runs/detect/train21-modelloscelto-/weights/best.pt \
  source=../videotest/testv.mp4 \
  project=runs/detect \
  name=predict
```

- **Model selection:** You can replace `train21-modelloscelto-` with any other run folder located in `runs/detect/`.
- **Source:** Set `source=` to any target image or video path.
- **Outputs:** Annotated predictions with bounding boxes are saved automatically inside `ultralytics/runs/detect/predict*/` (as `.avi` for videos or `.jpg` for images).

---

### 2. Model Training

To launch a new YOLO training pipeline:

```bash
yolo task=detect mode=train \
  model=yolo11s.pt \
  data=datasetmodelloscelto/data.yaml \
  epochs=100 \
  imgsz=640
```

- **`model`**: Select the starting architecture checkpoint (e.g., `yolo11s.pt`, located in the `ultralytics/` directory).
- **`data`**: Path to the dataset configuration file (`data.yaml`). Ensure paths are correctly mapped.
- **`epochs` & `imgsz`**: Customize training iterations and input resolution according to your hardware setup and requirements.

---

### 3. Evaluation & Metrics

All metrics and artifact files for the primary model are stored inside `runs/detect/train21(modelloscelto)/`:
- **Visual performance graphs:** Confusion matrices, box plots, F1-confidence curves, and precision-recall (PR) curves.
- **Epoch logs:** `results.csv` tracking loss metrics, precision, recall, and mAP across epochs.
- **Hyperparameter records:** `args.yaml` containing the complete training configuration.