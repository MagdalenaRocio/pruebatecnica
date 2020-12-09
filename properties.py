from typing import NamedTuple, List, Text


class Video(NamedTuple):
    """
    That's a video from the API
    """

    name: Text
    width: int
    height: int
    frames: int
    frame_rate: List[int]
    url: Text
    first_frame: Text
    last_frame: Text


class Size(NamedTuple):
    """
    tamaño
    """

    width: int
    height: int


DISPLAY_SIZE = Size(int(480 * 1.5), int(270 * 1.5))
