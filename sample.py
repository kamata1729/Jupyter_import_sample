# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np
from numpy.random import randint


class SampleClass():
    def __init__(self, num):
        self.num = num
    def __call__(self):
        return np.arange(self.num)


def make_randint(num):
    return randint(num)


sample_class = SampleClass(10)

print(sample_class())

print(make_randint(100))
