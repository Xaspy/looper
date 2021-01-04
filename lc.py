import argparse
from redactor.audio import Audio


DESCRIPTION = 'Simple console script for redact audio files. Written in ' \
              'Python. For correct work needs ffmpeg(in PATH on Windows)' \
              '. This program can change speed, cut and merge files.' \
              'Version - 0.8 by Xaspy'
DESCRIPTION_RM = 'usage in redact mode: [-h] [-s SPEED] [-c CUT CUT]' \
              ' [-m MERGE] [-o OVERLAY] [-v VOLUME] [-fi FADE_IN FADE_IN]' \
              ' [-fo FADE_OUT FADE_OUT] [-e EQUAL EQUAL EQUAL EQUAL]' \
              ' [-f FINISH] [-t]\n\nredact mode arguments:\n' \
              '  -h\n\t\tshow help to redact mode\n' \
              '  -s SPEED\n\t\tchange speed in audio by multiplier\n' \
              '  -c CUT CUT\n\t\tcut audio file by time segment in mc\n' \
              '  -m MERGE\n\t\tmerge file with file by path in argument\n' \
              '  -f FINISH\n\t\tsave file by argument path and exit from this mode\n' \
              '  -v VOLUME\n\t\tchange volume by multiplier\n' \
              '  -o OVERLAY\n\t\toverlay file with file by path in argument\n' \
              '  -fi FADE_IN FADE_IN\n\t\tfade in effect with start at first and duration at second argument\n' \
              '  -fo FADE_OUT FADE_OUT\n\t\tfade out effect with start at first and duration at second argument\n' \
              '  -e EQUAL EQUAL EQUAL EQUAL\n\t\tequalize audio by 4 params\n' \
              '  -u\n\t\tundo last change\n' \
              '  -r\n\t\tredo last change\n' \
              '  -t\n\t\tterminate this redact session without save'


def create_main_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-s', '--select', nargs='+',
                        help='select audio file to redact by path')
    parser.add_argument('-hrm', '--help_redact_mode', action='store_true',
                        help='prints help message for redact mode')
    return parser


def main():
    parser = create_main_parser()
    namespace = parser.parse_args()

    hrm = namespace.help_redact_mode
    if hrm:
        print(DESCRIPTION_RM)

    selected_audio = namespace.select
    if selected_audio:
        path = ' '.join(selected_audio)
        try:
            audio = Audio(path)
        except ValueError as e:
            print(e.args[0])
            return
        print(f'\nyou selected a file by path: {path}')
        while True:
            request = input('>')
            if request.startswith('-t'):
                print('redact mode was terminated')
                break
            elif request.startswith('-h'):
                print(DESCRIPTION_RM)
            elif request.startswith('-s'):
                if not _is_correct(2, request):
                    print('err syntax')
                    continue
                speed_mult = request.split(maxsplit=1)[1]
                try:
                    audio.change_speed(float(speed_mult))
                    print('file was speeded')
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-v'):
                if not _is_correct(2, request):
                    print('err syntax')
                    continue
                volume_mult = request.split(maxsplit=1)[1]
                try:
                    audio.change_volume(float(volume_mult))
                    print('file was volumed')
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-c'):
                if not _is_correct(3, request):
                    print('err syntax')
                    continue
                split_req = request.split()
                try:
                    audio.cut(int(split_req[1]), int(split_req[2]))
                    print('file was cut')
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-fi'):
                if not _is_correct(3, request):
                    print('err syntax')
                    continue
                split_req = request.split()
                try:
                    audio.fade_in(float(split_req[1]), float(split_req[2]))
                    print('file was fade inned')
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-fo'):
                if not _is_correct(3, request):
                    print('err syntax')
                    continue
                split_req = request.split()
                try:
                    audio.fade_out(float(split_req[1]), float(split_req[2]))
                    print('file was fade outed')
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-f'):
                if not _is_correct(2, request):
                    print('err syntax')
                    continue
                path_to_save = request.split(maxsplit=1)[1]
                try:
                    audio.save(path_to_save)
                    print(f'file was saved to {path_to_save}')
                    continue
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-e'):
                if not _is_correct(5, request):
                    print('err syntax')
                    continue
                split_req = request.split()
                try:
                    audio.equalize(float(split_req[1]), split_req[2],
                                   float(split_req[3]), float(split_req[4]))
                    print('equalized successfully')
                except Exception as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-m'):
                split_req = request.split(maxsplit=1)[1]
                path_to_file = split_req
                try:
                    audio.merge(path_to_file)
                    print('merged successfully')
                except Exception as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-o'):
                split_req = request.split(maxsplit=1)[1]
                path_to_file = split_req
                try:
                    audio.overlay(path_to_file)
                    print('overlayed successfully')
                except Exception as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-u'):
                audio.undo()
            elif request.startswith('-r'):
                audio.redo()
            else:
                print('err syntax')


def _is_correct(number: int, req: str) -> bool:
    return len(req.split()) == number


if __name__ == '__main__':
    main()
