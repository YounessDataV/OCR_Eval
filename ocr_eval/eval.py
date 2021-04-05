import jiwer
from pathlib import Path
from typing import Mapping


def eval_txt_file(ground_truth_path: Path, prediction_path: Path) -> Mapping[str, float]:
    """

    :param ground_truth_path:
    :param prediction_path:
    :return:
    """
    with open(ground_truth_path, "r") as f:
        truth = f.read()

    with open(prediction_path, "r") as f:
        hypothesis = f.read()

    return jiwer.compute_measures(truth=truth, hypothesis=hypothesis)

