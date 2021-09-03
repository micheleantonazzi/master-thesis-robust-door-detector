from src.bounding_box import BoundingBox
from src.evaluators.coco_evaluator import get_coco_summary
from src.utils.enumerators import BBType, BBFormat
import torch.nn.functional as F


class CocoEvaluator:
    def __init__(self):
        self._gt_bboxes = []
        self._predicted_bboxes = []

        self._img_count = 0

    def add_predictions(self, targets, predictions):
        img_count_temp = self._img_count

        for target in targets:
            for label, [x, y, w, h] in zip(target['labels'].tolist(), target['boxes'].tolist()):
                self._gt_bboxes.append(BoundingBox(
                    image_name=str(self._img_count),
                    class_id=str(label),
                    coordinates=(x - w / 2, y - h / 2, w, h),
                    bb_type=BBType.GROUND_TRUTH,
                    format=BBFormat.XYWH,
                ))
            self._img_count += 1

        pred_logits, pred_boxes_images = predictions['pred_logits'], predictions['pred_boxes']
        prob = F.softmax(pred_logits, -1)
        scores_images, labels_images = prob[..., :-1].max(-1)

        for scores, labels, pred_boxes in zip(scores_images, labels_images, pred_boxes_images):
            for score, label, [x, y, w, h] in zip(scores, labels, pred_boxes):
                label = label.item()
                score = score.item()
                if label >= 0:
                    self._predicted_bboxes.append(
                        BoundingBox(
                            image_name=str(img_count_temp),
                            class_id=str(label),
                            coordinates=(x - w / 2, y - h / 2, w, h),
                            bb_type=BBType.DETECTED,
                            format=BBFormat.XYWH,
                            confidence=score
                        )
                    )
            img_count_temp += 1

    def get_coco_metrics(self):
        return get_coco_summary(self._gt_bboxes, self._predicted_bboxes)

