import json
from pathlib import Path

import numpy as np
import numba


@numba.njit
def _calculate_score(candidate_words, real_words):
    """
    Calculate the number of letters

    Parameters
    ----------
    candidate_words: np.array
        2d array of integers, axis=0 is words, axis=1 is letters
    real_words: np.array
        2d array of integers, axis=0 is words, axis=1 is letters

    Returns
    -------
    in_spots: np.array
        1d array of integers, len(in_spots) == len(candidate_words)
        the total number of letters appearing in correct positions in the target wordlist
    in_words: np.array
        1d array of integers, len(in_words) == len(candidate_words)
        the total number of letters appearing in words (but not in correct positions) in the target wordlist
    """
    in_spots = np.zeros(shape=candidate_words.shape[0])
    in_words = np.zeros(shape=candidate_words.shape[0])

    for w_idx, word in enumerate(candidate_words):
        for l_idx, letter in enumerate(word):
            for test_word in real_words:
                if letter == test_word[l_idx]:
                    in_spots[w_idx] += 1
                elif letter in test_word:
                    in_words[w_idx] += 1
    return in_spots, in_words


def calculate_score(candidates, reals):
    in_spots, in_words = _calculate_score()
    mean_in_spots = in_spots / len(reals)
    mean_in_words = in_words / len(reals)
    return mean_in_spots, mean_in_words


def calculate_one_score(candidate, real):
    candidates = np.array([list(candidate)]).view(np.int32)
    reals = np.array([list(real)]).view(np.int32)
    in_spot, in_word = _calculate_score(candidates, reals)
    return in_spot[0], in_word[0]
