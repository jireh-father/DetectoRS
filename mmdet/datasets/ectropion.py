from .builder import DATASETS
from .coco import CocoDataset


@DATASETS.register_module()
class MyDataset(CocoDataset):
    CLASSES = ('ectropion')
