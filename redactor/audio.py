import os
import shutil
import subprocess
from redactor.hist import AudioHistory
from redactor.actions import Action

MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_TEMP = os.path.join(MAIN_PATH, '_temp')


class Audio:
    def __init__(self, path: str) -> None:
        if not os.path.exists(path) or os.path.isdir(path):
            raise ValueError('path to file is incorrect')
        self.hist = None
        self.iter = 1
        self._send_audio_to_temp(path)

    def get_name(self) -> str:
        return self.hist.get_current()

    def save(self, path: str) -> None:
        if os.path.isdir(path):
            raise ValueError('path to new file specified incorrectly')
        if os.path.exists(path):
            raise ValueError('this file already exists')
        shutil.copy(self.hist.get_current(), path)

    def cut(self, start_s: float, end_s: float) -> None:
        new_path = self.file_path + str(self.hist.get_iter() + 1) + '.wav'
        self.hist.add(new_path)
        self._delete_old_versions()
        Action.cut(start_s, end_s, self.file_path, self.hist.get_iter() - 1)
        self._delete_old_versions()

    def change_speed(self, multiplier: float) -> None:
        new_path = self.file_path + str(self.hist.get_iter() + 1) + '.wav'
        self.hist.add(new_path)
        self._delete_old_versions()
        Action.speed(multiplier, self.file_path, self.hist.get_iter() - 1)
        self._delete_old_versions()

    def change_volume(self, multiplier: float) -> None:
        new_path = self.file_path + str(self.hist.get_iter() + 1) + '.wav'
        self.hist.add(new_path)
        self._delete_old_versions()
        Action.volume(multiplier, self.file_path, self.hist.get_iter() - 1)
        self._delete_old_versions()

    def merge(self, other: str) -> None:
        new_path = self.file_path + str(self.hist.get_iter() + 1) + '.wav'
        self.hist.add(new_path)
        self._delete_old_versions()
        Action.merge(other, self.file_path, self.hist.get_iter() - 1)
        self._delete_old_versions()

    def overlay(self, other: str) -> None:
        new_path = self.file_path + str(self.hist.get_iter() + 1) + '.wav'
        self.hist.add(new_path)
        self._delete_old_versions()
        Action.overlay(other, self.file_path, self.hist.get_iter() - 1)
        self._delete_old_versions()

    def fade_in(self, start_s: float, duration_s: float):
        new_path = self.file_path + str(self.hist.get_iter() + 1) + '.wav'
        self.hist.add(new_path)
        self._delete_old_versions()
        Action.fade_in(start_s, duration_s, self.file_path, self.hist.get_iter() - 1)
        self._delete_old_versions()

    def fade_out(self, start_s: float, duration_s: float):
        new_path = self.file_path + str(self.hist.get_iter() + 1) + '.wav'
        self.hist.add(new_path)
        self._delete_old_versions()
        Action.fade_out(start_s, duration_s, self.file_path, self.hist.get_iter() - 1)
        self._delete_old_versions()

    def equalize(self, freq: float, width_type: str, width: float, gain: float):
        new_path = self.file_path + str(self.hist.get_iter() + 1) + '.wav'
        self.hist.add(new_path)
        self._delete_old_versions()
        Action.equalize(freq, width_type, width, gain, self.file_path, self.hist.get_iter() - 1)
        self._delete_old_versions()

    def undo(self) -> None:
        self.hist.undo()

    def redo(self) -> None:
        self.hist.redo()

    def _send_audio_to_temp(self, orig_path: str) -> None:
        filename, _ = os.path.splitext(os.path.basename(orig_path))
        temp_file_path = os.path.join(PATH_TO_TEMP, f'{filename}_temp_{self.iter}.wav')
        self.file_path = temp_file_path[:-5]
        subprocess.call(['ffmpeg', '-y', '-i', f'{orig_path}', f'{temp_file_path}'])
        self.hist = AudioHistory(temp_file_path, 5)

    def _delete_old_versions(self):
        paths_to_del = self.hist.get_paths_to_del()
        for path in paths_to_del:
            os.remove(path)

    def __del__(self):
        try:
            for path in self.hist.get_all_paths():
                os.remove(path)
        except AttributeError:
            pass


if __name__ == '__main__':
    pass
