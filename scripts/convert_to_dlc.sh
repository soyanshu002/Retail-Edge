#!/bin/bash
# Convert ONNX model to DLC format using Qualcomm SNPE

ONNX_MODEL="models/onnx/yolov5s.onnx"
DLC_OUTPUT="models/dlc/yolov5.dlc"

echo "[INFO] Converting ONNX to DLC..."
snpe-onnx-to-dlc --input_network $ONNX_MODEL --output_path $DLC_OUTPUT

if [ $? -eq 0 ]; then
    echo "[SUCCESS] Model converted to DLC: $DLC_OUTPUT"
else
    echo "[ERROR] Conversion failed!"
fi
