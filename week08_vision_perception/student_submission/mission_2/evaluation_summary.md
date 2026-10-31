# Visual evaluation

Shared images: 31. Cup detection threshold: 0.2.
NMS overlap: 0.35. Classification cup-score threshold: 0.885.
Foreground threshold: 0.5.

Cup AP50: 0.800122549019608.
Classification accuracy: 0.3548387096774194, precision: None, recall: 0.0.

Classification maps the ImageNet cup and coffee mug scores to a binary rule. The segmenter predicts class-agnostic salient foreground, evaluated against the desired cup region. These are different output tasks.

Pixel annotations are approximate manually traced visible-cup silhouettes. Independent photos have no pixel labels and are excluded from mask scores. Both-empty masks score 1. Inspect target-present and absent rows separately.

AP50 uses one cup class at IoU 0.50, with a 0.001 proposal score floor. It is not multiclass or multi-IoU COCO mAP. Timings exclude loading, transport and action. See the mission explanation for the student's conclusions.
