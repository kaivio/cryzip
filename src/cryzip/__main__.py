from pathlib import Path
import argparse
from datetime import datetime


def version():
    print('cryzip/0.1.0')


def ready(overwrite):
    text = ''
    try:
        f = Path(Path(__file__).parent, 'mkcryzip.py')
        text = f.read_text() or ''
        text = text % {
            'date': datetime.now().strftime("%Y-%m-%d"),
        }

        p = Path('mkcryzip.py')
        if overwrite or not p.exists():
            p.write_text(text)
            print('Create:  mkcryzip.py')
            print('Hint:    Edit then run it.')

        else:
            overwrite = input('`mkcryzip.py` is exists, overwrite?(y/n)')
            if overwrite.lower().startswith('y') :
                return ready(True)
            # print('`mkcryzip.py` is exists, overwrite?(y/n)' )

    except Exception as e:
        # traceback.print_exc()
        print(e)


def main():
    parser = argparse.ArgumentParser()
    parser.usage = '''
    cryzip    # init `mkcryzip.py` 
    python mkcryzip.py
    '''
    parser.add_argument('-y', '--yes', action='store_true', default=False)
    parser.add_argument('-v', '--version', action='store_true', default=False)

    flag = parser.parse_args()

    if flag.version:
        return version()

    ready(flag.yes)


if __name__ == '__main__':
    main()
