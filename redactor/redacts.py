from redactor.audio import Audio
from redactor.exceptions.track_exc import OccupiedException, TimeCannotBeZero
from redactor.track_parts import Segment


class Track:
    def __init__(self, size: int) -> None:
        self.size = size
        self.entities = {}
        self.occupied = {-1: Segment(-1, 0)}

    def add(self, entity) -> None:
        if self._is_free_space(entity.pos):
            self.entities[entity.name] = entity
            self.occupied[entity.pos.start] = entity.pos
        else:
            raise OccupiedException('these place already occupied')

    def delete(self, name: str) -> None:
        start = self.entities[name].pos.start
        del self.entities[name]
        del self.occupied[start]

    def _is_free_space(self, pos: Segment) -> bool:
        starts = sorted(self.occupied.keys())
        prev = self.size
        for x in starts[::-1]:
            if x < pos.start and self.occupied[x].end <= pos.start and prev >= pos.end:
                return True
            prev = x
        return False


class Entity:
    def __init__(self, audio: Audio, start_ms: int, end_ms: int) -> None:
        if start_ms == end_ms:
            raise TimeCannotBeZero('start equals end')
        self.audio = audio
        self.pos = Segment(start_ms, end_ms)
        self.name = audio.get_name()

