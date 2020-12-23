import os
import wave
import shutil
import subprocess

MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_TEMP = os.path.join(MAIN_PATH, '_temp')


class Audio:
    def __init__(self, path: str) -> None:
        if not os.path.exists(path) or os.path.isdir(path):
            raise ValueError('path to file is incorrect')
        self.file_path = ''
        self.iter = 0
        self._name = path
        self._send_audio_to_temp(path)

    def get_name(self) -> str:
        return self._name

    def save(self, path: str) -> None:
        if os.path.isdir(path):
            raise ValueError('path to new file specified incorrectly')
        if os.path.exists(path):
            raise ValueError('this file already exists')

        shutil.copy(self.file_path, path)

    def cut(self, start_ms: int, end_ms: int) -> None:
        self.iter += 1
        new_path = self.file_path[:-5] + str(self.iter) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{self.file_path}',
                         '-ss', f'{start_ms}', '-to', f'{end_ms}',
                         f'{new_path}'])
        self.file_path = new_path

    def change_speed(self, multiplier: float) -> None:
        self.iter += 1
        new_path = self.file_path[:-5] + str(self.iter) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{self.file_path}',
                         '-filter:a', f'atempo={multiplier}', '-vn',
                         f'{new_path}'])
        self.file_path = new_path

    def change_volume(self, multiplier: float) -> None:
        self.iter += 1
        new_path = self.file_path[:-5] + str(self.iter) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{self.file_path}',
                         '-af', f'volume={multiplier}', f'{new_path}'])
        self.file_path = new_path

    def merge(self, other) -> None:
        pass

    def _send_audio_to_temp(self, orig_path: str) -> None:
        filename, _ = os.path.splitext(os.path.basename(orig_path))
        temp_file_path = os.path.join(PATH_TO_TEMP, f'{filename}_temp_{self.iter}.wav')
        subprocess.call(['ffmpeg', '-y', '-i', f'{orig_path}', f'{temp_file_path}'])
        self.file_path = temp_file_path

    def __del__(self):
        try:
            os.remove(self.file_path)
        except AttributeError:
            pass


if __name__ == '__main__':
    pass
