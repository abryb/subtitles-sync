#!/usr/bin/python3

import sys
import re
import datetime
from os import path


def sync_subtitles(lines: list, value: int) -> list:
    synced = []
    for line in lines:
        synced.append(sync_line(line, value))
    return synced


def sync_line(line: str, t: int) -> str:
    match = re.match(r'^(\d\d:\d\d:\d\d):(.*)$', line)
    if match is None:
        return line
    time_string = match.group(1)
    a = datetime.datetime.strptime(time_string, "%H:%M:%S")
    a = a + datetime.timedelta(0, int(t))
    return "%s:%s" % (a.time(), match.group(2))


def parse_argv_and_run(argv):
    script_name = argv[0]

    if len(argv) < 3:
        print("Usage:\n%s <file> <sync_value_in_seconds>" % script_name)
        exit(0)

    subtitles_file = argv[1]
    seconds_delta_arg = argv[2]

    if not path.exists(subtitles_file):
        print("%s file does not exists." % subtitles_file)
        exit(1)

    if re.match(r"^[+-]?\d+$", seconds_delta_arg) is None:
        print("%s is not numeric value." % seconds_delta_arg)
        exit(1)

    seconds_delta = int(seconds_delta_arg)
    file1 = open(subtitles_file, 'r')

    subtitles_original = file1.readlines()
    subtitles_synced = sync_subtitles(subtitles_original, seconds_delta)

    if len(argv) > 3 and argv[3] == '--save':
        with open(subtitles_file, 'w') as file:
            for line in subtitles_synced:
                file.write("%s\n" % line)
    else:
        for line in subtitles_synced:
            print(line)


if __name__ == '__main__':
    parse_argv_and_run(sys.argv)
