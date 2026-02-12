import random
from typing import List

def d(num_dice: int, num_sides: int) -> List[int]:
    """
    Rolls `num_dice` dice with `num_sides` sides.
    Returns die results, sorted
    """
    return sorted([random.randint(1, num_sides) for _ in range(num_dice)])

def drop_lowest_dice(die_results: List[int], num_dropped: int) -> List[int]:
    """
    Drops the lowest `num_dropped` dice from sorted `die_results`
    Returns die results, sorted
    """
    return die_results[num_dropped:]

def drop_highest_dice(die_results: List[int], num_dropped: int) -> List[int]:
    """
    Drops the highest `num_dropped` dice from sorted `die_results`
    Returns die results, sorted
    """
    return die_results[:len(die_results) - num_dropped]

def roll_result(die_results: List[int], modifier: int) -> int:
    return sum(die_results) + modifier
