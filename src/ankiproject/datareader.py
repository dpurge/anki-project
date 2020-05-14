import os
import json
import yaml
import csv

from .datarecord import Record

def get_format(data):
    format = 'data/unknown'
    if isinstance(data, str):
        format = 'data/text'
    if isinstance(data, dict):
        format = 'data/dictionary'
    if isinstance(data, list):
        format = 'data/list'
    return format

def get_text_records(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        meta = {'format': 'data/text'}
        data = line.strip()
        yield Record(meta = meta, data = data)


def get_csv_records(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        records = csv.DictReader(f)
        for data in records:
            meta = {'format': get_format(data)}
            yield Record(meta = meta, data = data)


def get_markdown_records(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        contents = f.read()
    for record in contents.split("\n---\n"):
        meta = {'format': 'data/markdown'}
        data = record.strip()
        yield Record(meta = meta, data = data)


def get_json_records(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        records = json.load(f)
    for data in records:
        meta = {'format': get_format(data)}
        yield Record(meta = meta, data = data)


def get_yaml_records(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        records = yaml.safe_load(f)
    for data in records:
        meta = {'format': get_format(data)}
        yield Record(meta = meta, data = data)


def get_audio_record(filename):
        meta = {'format': 'data/audio'}
        data = filename
        yield Record(meta = meta, data = data)


def get_video_record(filename):
        meta = {'format': 'data/video'}
        data = filename
        yield Record(meta = meta, data = data)


def get_image_record(filename):
        meta = {'format': 'data/image'}
        data = filename
        yield Record(meta = meta, data = data)


readers = {
    '.txt': get_text_records,
    '.csv': get_csv_records,
    '.md': get_markdown_records,
    '.json': get_json_records,
    '.yaml': get_yaml_records,
    '.mp3': get_audio_record,
    '.mp4': get_video_record,
    '.svg': get_image_record
}


def get_data(records):
    for record in records:
        if record.meta['format'] == 'filesystem/file':
            filename = record.data
            extension = os.path.splitext(filename)[-1]
            reader = readers.get(extension, get_text_records)
            for item in reader(filename):
                yield item
        else:
            yield record


def get_files(records):
    for record in records:
        if record.meta['format'] == 'filesystem/directory':
            for subdir, dirs, files in os.walk(record.data):
                for file in files:
                    meta = {
                        'format': 'filesystem/file'
                    }
                    data = os.path.join(subdir, file)
                    yield Record(meta = meta, data = data)
        else:
            yield record