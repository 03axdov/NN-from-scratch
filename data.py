from tensor import Tensor
import numpy as np
from typing import Iterator, NamedTuple

BATCH = NamedTuple("BATCH", [("inputs", Tensor), ("targets", Tensor)])


class DataIterator:
    def __call__(self, inputs: Tensor, targets: Tensor) -> Iterator[BATCH]:
        raise NotImplementedError


class BatchIterator:
    def __init__(self, batch_size: int = 32, shuffle: bool = True) -> None:
        self.batch_size = batch_size
        self.shuffle = shuffle
    def __call__(self, inputs: Tensor, targets: Tensor) -> Iterator[BATCH]:
        starts = np.arange(0, len(inputs), self.batch_size)
        if self.shuffle:
            np.random.shuffle(starts)

        for start in starts:
            end = start + self.batch_size
            batch_inputs = inputs[start:end]
            batch_targets = targets[start:end]
            yield BATCH[batch_inputs, batch_targets]