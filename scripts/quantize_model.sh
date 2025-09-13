#!/bin/bash
# Quantize DLC model using SNPE with calibration dataset

INPUT_DLC="models/dlc/yolov5.dlc"
OUTPUT_DLC="models/dlc/yolov5_quantized.dlc"
CALIB_LIST="data/calib_list.txt"

echo "[INFO] Running quantization..."
snpe-dlc-quantize --input_dlc $INPUT_DLC --output_dlc $OUTPUT_DLC --input_list $CALIB_LIST

if [ $? -eq 0 ]; then
    echo "[SUCCESS] Quantized DLC saved at: $OUTPUT_DLC"
else
    echo "[ERROR] Quantization failed!"
fi
