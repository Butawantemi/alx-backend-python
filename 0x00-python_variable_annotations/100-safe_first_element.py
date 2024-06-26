#!/usr/bin/env python3
""" duck-typed annotations """

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return first element of a sequence
    """
    return (lst[0] if lst else None)