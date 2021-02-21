from pathlib import Path
import pandas as pd
import numpy as np
import h5py
import click

DATA_PATH = Path("../../data")

BRATS_IMAGES = Path(DATA_PATH / "BraTS2020_training_data")
SURVIVAL_INFO = Path(DATA_PATH / "survival_info.csv")
META_DATA = Path(DATA_PATH / "meta_data.csv")


@click.command()
@click.option("--survival_info_path", default=SURVIVAL_INFO)
@click.option("--meta_data_path", default=META_DATA)
def preprocess_kaggle_data(survival_info_path, meta_data_path):

    # Process survival info
    survival_info = pd.read_csv(Path(survival_info_path))
    survival_info.loc[
        survival_info.Survival_days == "ALIVE (361 days later)", "Survival_days"
    ] = 361
    survival_info.Survival_days = survival_info.Survival_days.astype(int)
    print(f"Saving processed survival info to {survival_info_path}")
    survival_info.to_csv(survival_info_path)

    # Process meta data
    meta_data = pd.read_csv(Path(meta_data_path))
    meta_data.slice_path = [Path(i).name for i in meta_data.slice_path]
    print(f"Saving processed meta data to {meta_data_path}")
    meta_data.to_csv(meta_data_path)


class BratsData:
    def __init__(self, train_path, val_path, test_path):
        self.train_path = train_path
        self.val_path = val_path
        self.test_path = test_path

    def get_volume(self, idx, meta_data, data_path=BRATS_IMAGES):

        df = meta_data[meta_data.volume == idx]

        for i, row in df.iterrows():
            path = Path(data_path).joinpath(row.slice_path)
            hf = h5py.File(path, "r")
            img = np.array(hf.get("image"))
            mask = np.array(hf.get("mask"))
            yield {"image": img, "mask": mask, "slice": row.slice}


if __name__ == "__main__":
    preprocess_kaggle_data()
