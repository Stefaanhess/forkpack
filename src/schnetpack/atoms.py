"""
This module contains all functionalities required to load atomistic data,
generate batches and compute statistics. It makes use of the ASE database
for atoms [#ase2]_.

References
----------
.. [#ase2] Larsen, Mortensen, Blomqvist, Castelli, Christensen, Dułak, Friis,
   Groves, Hammer, Hargus:
   The atomic simulation environment -- a Python library for working with atoms.
   Journal of Physics: Condensed Matter, 9, 27. 2017.
"""
import logging
import os
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, List, Dict, Any, Iterable, Union, Tuple

import torch
import copy
from ase import Atoms
from ase.db import connect


logger = logging.getLogger(__name__)

__all__ = [
    "load_dataset",
]

def load_dataset(datapath: str, format, **kwargs):
    """
    Load dataset.

    Args:
        datapath: file path
        format: atoms data format
        **kwargs: arguments for passed to AtomsData init

    """
    return 0

