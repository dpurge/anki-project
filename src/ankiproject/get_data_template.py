import json
from pathlib import Path, PurePath
from jinja2 import Environment, FileSystemLoader

def get_data_template(config):

    cfg_path = Path(config)

    if not cfg_path.exists():
        raise Exception("Data template configuration does not exist: {cfg_path}".format(cfg_path=cfg_path))

    with cfg_path.open(mode="r", encoding="utf-8") as f:
        cfg = json.load(f)

    loader = FileSystemLoader(cfg_path.parent)
    env = Environment(loader=loader)

    templates = {}
    for key in cfg['templates'].keys():
        item = {
            'template': env.get_template(cfg['templates'][key]),
            'markdown': key in cfg['markdown']
        }
        templates[key] = item

    return templates