import os
import wave
import shutil
import subprocess


MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_TEMP = os.path.join(MAIN_PATH, '_temp')


class Audio:
    def __init__(self, path: str) -> None:
        if os.path.isdir(path):
            raise ValueError('Path to file specified incorrectly')

        self._send_audio_to_temp(path)
        self.audio = wave.open(self.file_path, 'r')

        self.audio.rewind()
        self._frames_per_ms = int(self.audio.getframerate() / 1000)
        self._pointer = self.audio.tell()
        self._length = self.audio.getnframes()
        self._rate = self.audio.getframerate()
        self._frames = self.audio.readframes(self._length)

    def save(self, path: str) -> None:
        if os.path.isdir(path):
            raise ValueError('Path to new file specified incorrectly')
        if os.path.exists(path):
            raise ValueError('This file already exists')

        shutil.copy(self.file_path, path)

    def cut(self, start_ms: int, end_ms: int) -> None:
        if start_ms > end_ms:
            raise ValueError("start_ms must be less than end_ms")

        self._length = (end_ms - start_ms) * self._frames_per_ms
        start_index = start_ms * self._frames_per_ms
        self.audio.setpos(self._pointer + start_index)
        self._frames = self.audio.readframes(self._length)

        self._update_temp_file()

    def change_speed(self, multiplier: float) -> None:
        if multiplier <= 0:
            raise ValueError('multiplier must be greater than zero')

        self._rate = self._rate * multiplier

        self._update_temp_file()

    def merge(self, other) -> None:
        if not isinstance(other, Audio):
            raise ValueError('argument should be Audio object')

        self._length = self._length + other._length
        self._frames = self._frames + other._frames

        self._update_temp_file()

    def _update_temp_file(self) -> None:
        params = (
            self.audio.getnchannels(), self.audio.getsampwidth(),
            self._rate, self._length,
            self.audio.getcomptype(), self.audio.getcompname()
        )
        self.audio.close()

        with wave.open(self.file_path, 'w') as file:
            file.setparams(params)
            file.writeframes(self._frames)

        self.audio = wave.open(self.file_path, 'r')
        self._update_local_vars()

    def _send_audio_to_temp(self, orig_path: str) -> None:
        filename, _ = os.path.splitext(os.path.basename(orig_path))
        temp_file_path = os.path.join(PATH_TO_TEMP, f'{filename}_temp.wav')
        subprocess.call(['ffmpeg', '-y', '-i', f'{orig_path}', f'{temp_file_path}'])
        self.file_path = temp_file_path

    def _update_local_vars(self):
        self.audio.rewind()
        self._frames_per_ms = int(self.audio.getframerate() / 1000)
        self._pointer = self.audio.tell()
        self._length = self.audio.getnframes()
        self._rate = self.audio.getframerate()
        self._frames = self.audio.readframes(self._length)


if __name__ == '__main__':
    pass
