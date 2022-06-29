from pathlib import Path
from json import loads
from pprint import pprint


def build_code():
    print('BUILD')
    plan = read_dev_plan()
    for lesson in plan['lessons']['table']:
        pprint(lesson)


def read_dev_plan():
    return read_json(f'Documents/course.json')


def read_json(filename):
    if Path(filename).exists():
        return loads(Path(filename).read_text())
    return {}
