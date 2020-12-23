import unittest
from redactor.redacts import Track, Entity
from unittest.mock import Mock
from redactor.audio import Audio
from redactor.exceptions.track_exc import OccupiedException


class TestTrackActions(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.track = Track(10000)
        audio = Mock()
        audio.get_name.return_value = '0'
        entity = Entity(audio, 0, 3000)
        cls.track.add(entity)

    def test_cannot_add(self):
        audio = Mock()
        entity = Entity(audio, 1000, 5000)
        self.assertRaises(OccupiedException, self.track.add, entity)

    def test_add(self):
        audio = Mock()
        audio.get_name.return_value = '1'
        entity_1 = Entity(audio, 3000, 5000)
        audio.get_name.return_value = '2'
        entity_2 = Entity(audio, 6000, 7000)
        self.track.add(entity_1)
        self.track.add(entity_2)
        self.assertEqual(list(self.track.entities.keys()), ['0', '1', '2'])

    def test_delete(self):
        audio = Mock()
        audio.get_name.return_value = '3'
        entity_3 = Entity(audio, 7000, 8000)
        self.track.add(entity_3)
        self.assertEqual(list(self.track.entities.keys()), ['0', '1', '2', '3'])
        self.track.delete('3')
        self.assertFalse('3' in self.track.entities.keys())


if __name__ == '__main__':
    unittest.main()
