import os
import sys
import datetime
import time
import shutil


def get_last_change_time(path, days):
    return datetime.datetime.fromtimestamp(os.path.getmtime(path))


def main(path=sys.path[0], days=2, size=4096):
    if os.path.isdir(path) and not os.path.exists(path):
        print('ERROR!!! Path is not found!')

    path_archive = path + '\\' + 'Archive'
    path_small = path + '\\' + 'Small'
    path_clear = path + '\\'
    to_archive, to_small = False

    if os.path.isdir(path_archive):
        to_archive = True
        
    if os.path.isdir(path_small):
        to_small = True

    cur_date = datetime.datetime.today()

    files_list = os.listdir(path)

    for file in files_list:
        if os.path.isfile(path_archive + file) and cur_date - get_last_change_time(path_clear + file) >= datetime.timedelta(days=days):
            if to_archive:
                os.mkdir(path_archive)
                to_archive = False
            shutil.copy(path_clear + file, path_archive + '\\' + file)

        if os.path.isfile(path_clear + file) and os.path.getsize(path_clear + file) <= size:
            if to_small:
                os.mkdir(path_small)
                to_small = False
            shutil.copy(path_clear + file, path_small + '\\' + file)


if __name__ == '__main__':
    if len(sys.argv) == 7 and sys.argv[1] == '--sourse' and sys.argv[3] == "--days" and sys.argv[5] == '--size':
        main(sys.argv[2], int(sys.argv[4]), int(sys.argv[7]))
    else:
        raise Exception('ERROR!!! Incorrect command or something else went wrong!')
