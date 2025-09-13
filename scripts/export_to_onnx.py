"""
Export YOLOv5 PyTorch model to ONNX format
"""

import yaml
import torch

def export_to_onnx(config_path="configs/export_config.yaml"):
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    weights = cfg["model"]["weights"]
    onnx_path = cfg["output"]["onnx_path"]
    input_size = tuple(cfg["model"]["input_size"])

    print(f"[INFO] Loading model from {weights}")
    model = torch.hub.load("ultralytics/yolov5", "custom", path=weights)

    dummy_input = torch.zeros(1, 3, *input_size)
    print(f"[INFO] Exporting model to {onnx_path}")
    torch.onnx.export(
        model,
        dummy_input,
        onnx_path,
        opset_version=cfg["model"]["opset_version"],
        input_names=["input"],
        output_names=["output"],
        dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}},
    )

    print("[SUCCESS] Export completed!")

if __name__ == "__main__":
    export_to_onnx()
