# YOLOv5 Edge AI Deployment with Qualcomm SNPE

## Overview

This project demonstrates the **optimization and deployment of a YOLOv5 object detection model** on **Qualcomm Snapdragon NPUs** using the **Snapdragon Neural Processing Engine (SNPE)**. The workflow enables real-time object detection on **edge devices**, leveraging model conversion, quantization, and acceleration.

---

## Features

- Export YOLOv5 (PyTorch `.pt`) model to **ONNX**
- Convert ONNX model to **DLC format** for Qualcomm SNPE
- Apply **post-training INT8 quantization** for faster inference
- Benchmark and evaluate model on Snapdragon NPU
- Modular, script-based workflow for **easy extension**
- Track results, visualize bounding boxes, and optimize performance