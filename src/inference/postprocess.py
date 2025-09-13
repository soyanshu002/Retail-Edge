"""
Post-processing utilities for SNPE model outputs.
"""

import numpy as np

def non_max_suppression(detections, iou_threshold=0.5):
    """
    Dummy NMS implementation (not real).
    """
    print(f"[INFO] Applying NMS with IoU threshold {iou_threshold}")
    # Return same detections for now
    return detections

def format_results(detections):
    """
    Convert raw detections into JSON-friendly output.
    """
    return {"num_objects": len(detections), "objects": detections}

if __name__ == "__main__":
    fake_dets = [
        {"class": "car", "confidence": 0.9, "bbox": [100, 150, 200, 300]},
        {"class": "car", "confidence": 0.85, "bbox": [110, 160, 210, 310]},
    ]
    final = non_max_suppression(fake_dets)
    print(format_results(final))
