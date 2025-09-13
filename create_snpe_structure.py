import os

# Base = your current project folder
base = os.getcwd()   # get current working directory
print(f"Creating inside: {base}")

folders = [
    "configs",
    "data/images",
    "data/annotations",
    "models/yolov5",
    "models/onnx",
    "models/dlc",
    "models/results",
    "scripts",
    "src/inference",
    "src/utils",
    "docs"
]

files = [
    "README.md", "requirements.txt", "environment.yml",
    "configs/export_config.yaml", "configs/quantization_config.yaml", "configs/device_config.yaml",
    "data/calib_list.txt",
    "models/yolov5/yolov5s.pt", "models/onnx/yolov5s.onnx", "models/dlc/yolov5.dlc",
    "scripts/export_to_onnx.py", "scripts/convert_to_dlc.sh", "scripts/quantize_model.sh",
    "scripts/benchmark.sh", "scripts/deploy.py",
    "src/inference/snpe_inference.py", "src/inference/postprocess.py",
    "src/utils/visualize.py", "src/utils/metrics.py",
    "src/pipeline.py",
    "docs/workflow_diagram.png", "docs/performance_report.md"
]

for folder in folders:
    os.makedirs(os.path.join(base, folder), exist_ok=True)

for file in files:
    path = os.path.join(base, file)
    if not os.path.exists(path):  # don’t overwrite existing files
        with open(path, "w") as f:
            pass
