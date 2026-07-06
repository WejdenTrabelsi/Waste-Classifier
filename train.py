"""
Train a waste image classifier with fastai (transfer learning on ResNet34).

Dataset: Kaggle "Garbage Classification" (TrashNet-based)
https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification


Run:
    python train.py
"""

from pathlib import Path
from fastai.vision.all import (
    ImageDataLoaders,
    Resize,
    vision_learner,
    resnet34,
    accuracy,
)

DATA_PATH = Path("data")
MODEL_OUT = Path("model/waste_classifier.pkl")


def main():
    dls = ImageDataLoaders.from_folder(
        DATA_PATH,
        valid_pct=0.2,
        seed=42,
        item_tfms=Resize(224),
    )

    learn = vision_learner(dls, resnet34, metrics=accuracy)
    learn.fine_tune(4)

    MODEL_OUT.parent.mkdir(exist_ok=True)
    learn.export(MODEL_OUT)
    print(f"Model saved to {MODEL_OUT}")


if __name__ == "__main__":
    main()
