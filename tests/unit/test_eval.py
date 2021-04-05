from pathlib import Path
from ocr_eval.eval import eval_txt_file

test_path = Path(__file__).resolve().parents[1]


def test_eval_txt_file():
    truth_path = test_path / "data" / "truth" / "example1.txt"
    hypothesis_path = test_path / "data" / "hypothesis" / "example1.txt"

    eval_dict = eval_txt_file(truth_path, hypothesis_path)

    assert "wer" in eval_dict