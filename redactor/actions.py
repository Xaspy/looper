import subprocess


class Action:
    @staticmethod
    def speed(multiplier: float, path: str, iter: int) -> str:
        old_path = path + str(iter) + '.wav'
        new_path = path + str(iter + 1) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{old_path}', '-filter:a',
                         f'atempo={multiplier}', '-vn', f'{new_path}'])
        return new_path

    @staticmethod
    def volume(multiplier: float, path: str, iter: int) -> str:
        old_path = path + str(iter) + '.wav'
        new_path = path + str(iter + 1) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{old_path}',
                         '-af', f'volume={multiplier}', f'{new_path}'])
        return new_path

    @staticmethod
    def cut(start_s: float, end_s: float, path: str, iter: int) -> str:
        old_path = path + str(iter) + '.wav'
        new_path = path + str(iter + 1) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{old_path}', '-ss',
                         f'{start_s}', '-to', f'{end_s}', f'{new_path}'])
        return new_path

    @staticmethod
    def merge(merged_path: str, path: str, iter: int) -> str:
        old_path = path + str(iter) + '.wav'
        new_path = path + str(iter + 1) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{old_path}', '-i', f'{merged_path}',
                         '-filter_complex', '[0:a] [1:a] concat=n=2:v=0:a=1', f'{new_path}'])
        return new_path

    @staticmethod
    def overlay(other_path: str, path: str, iter: int) -> str:
        old_path = path + str(iter) + '.wav'
        new_path = path + str(iter + 1) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{old_path}', '-i', f'{other_path}',
                         '-filter_complex', 'amix=inputs=2:duration=longest', f'{new_path}'])
        return new_path

    @staticmethod
    def fade_in(start_s: float, duration_s: float, path: str, iter: int) -> str:
        old_path = path + str(iter) + '.wav'
        new_path = path + str(iter + 1) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{old_path}', '-af',
                         f'afade=t=in:st={start_s}:d={duration_s}', f'{new_path}'])
        return new_path

    @staticmethod
    def fade_out(start_s: float, duration_s: float, path: str, iter: int) -> str:
        old_path = path + str(iter) + '.wav'
        new_path = path + str(iter + 1) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{old_path}', '-af',
                         f'afade=t=out:st={start_s}:d={duration_s}', f'{new_path}'])
        return new_path

    @staticmethod
    def equalize(freq: float, width_type: str, width: float, gain: float, path: str, iter: int) -> str:
        old_path = path + str(iter) + '.wav'
        new_path = path + str(iter + 1) + '.wav'
        subprocess.call(['ffmpeg', '-y', '-i', f'{old_path}', '-af',
                         f'equalizer=f={freq}:width_type={width_type}:width={width}:g={gain}',
                         f'{new_path}'])
        return new_path
