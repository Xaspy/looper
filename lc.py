import argparse
from redactor.audio import Audio


DESCRIPTION = 'Simple console script for redact audio files. Written in ' \
              'Python. For correct work needs ffmpeg(in PATH on Windows)' \
              '. This program can change speed, cut and merge files.' \
              'Version - 0.8 by Xaspy'
DESCRIPTION_RM = 'usage in redact mode: [-h] [-s SPEED] [-c CUT CUT]' \
              ' [-m MERGE *] [-f FINISH] [-t]\n\nredact mode arguments:\n' \
              '  -h\n\t\tshow help to redact mode\n' \
              '  -s SPEED\n\t\tchange speed in audio by multiplier\n' \
              '  -c CUT CUT\n\t\tcut audio file by time segment in mc\n' \
              '  -m MERGE MERGE\n\t\tmerge file with file by path in' \
              ' first argument and merge to end if second argument' \
              ' is "0" and to begin otherwise\n' \
              '  -f FINISH\n\t\tsave file by argument path and exit' \
              ' from this mode\n' \
              '  -t\n\t\tterminate this redact session without save'


def create_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-s', '--select', nargs='+',
                        help='select audio file to redact by path')
    parser.add_argument('-hrm', '--help_redact_mode', action='store_true',
                        help='prints help message for redact mode')

    return parser


def main():
    parser = create_parser()
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
                speed_mult = request.split(maxsplit=1)[1]
                try:
                    audio.change_speed(float(speed_mult))
                    print('file was speeded')
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-c'):
                split_req = request.split()
                if len(split_req) != 3:
                    print('err syntax')
                    continue
                try:
                    audio.cut(int(split_req[1]), int(split_req[2]))
                    print('file was cut')
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-f'):
                path_to_save = request.split(maxsplit=1)[1]
                try:
                    audio.save(path_to_save)
                    print(f'file was saved to {path_to_save}')
                    continue
                except ValueError as e:
                    print(e.args[0])
                    continue
            elif request.startswith('-m'):
                split_req = request.split(maxsplit=1)[1]
                path_to_file = split_req.rsplit(maxsplit=1)[0]
                mode = split_req.rsplit(maxsplit=1)[1]
                try:
                    other_audio = Audio(path_to_file)
                    bool_mode = mode != '0'
                    audio.merge(other_audio, bool_mode)
                    print('merged successfully')
                except Exception as e:
                    print(e.args[0])
                    continue
            else:
                print('err syntax')


if __name__ == '__main__':
    main()
