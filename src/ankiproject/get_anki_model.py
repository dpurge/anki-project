import json
from pathlib import Path, PurePath
from genanki import Model

def get_anki_model(config):

    cfg_path = Path(config)

    if not cfg_path.exists():
        raise Exception("Anki model configuration does not exist: {cfg_path}".format(cfg_path=cfg_path))

    with cfg_path.open(mode="r", encoding="utf-8") as f:
        cfg = json.load(f)

    model_id = cfg['id']
    name = cfg['name']
    fields = [{'name': f} for f in cfg['fields']]
    model_type = Model.CLOZE if cfg['type'] == 'cloze' else Model.FRONT_BACK

    stylesheet = Path(PurePath.joinpath(cfg_path.parent, cfg['styles']))
    if not stylesheet.exists():
        raise Exception("Anki model stylesheet does not exist: {stylesheet}".format(stylesheet=stylesheet))

    with stylesheet.open(mode="r", encoding="utf-8") as f:
        css = f.read()

    templates = []
    for t in cfg['templates']:
        n = t['name']

        q = Path(PurePath.joinpath(cfg_path.parent, t['qfmt']))
        if not q.exists():
            raise Exception("Missing qfmt template in Anki model '{name}', card '{card}': {qfmt}".format(name=name, card=n, qfmt=q))
        with q.open(mode="r", encoding="utf-8") as f:
            qfmt = f.read()

        a = Path(PurePath.joinpath(cfg_path.parent, t['afmt']))
        if not a.exists():
            raise Exception("Missing afmt template in Anki model '{name}', card '{card}': {afmt}".format(name=name, card=n, afmt=a))
        with a.open(mode="r", encoding="utf-8") as f:
            afmt = f.read()
        templates.append({'name':n, 'qfmt':qfmt, 'afmt':afmt})

    return Model(model_id = model_id, name=name, fields=fields, templates=templates, css=css, model_type=model_type)