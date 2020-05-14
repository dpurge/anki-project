from jinja2 import Environment, FileSystemLoader
from .datarecord import Record

def apply_template(records, template_folder, template_name):

    loader = FileSystemLoader(template_folder)
    env = Environment(loader=loader)

    tpl = env.get_template(template_name)
    formats = 'data/text', 'data/dictionary', 'data/list', 'data/markdown'

    for record in records:
        if record.meta['format'] in formats:
            meta = record.meta
            data = tpl.render(data = record.data)
            meta['format'] = 'data/html'

            yield Record(meta = meta, data = data)
        else:
            yield record