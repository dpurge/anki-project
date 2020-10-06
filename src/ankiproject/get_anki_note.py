import markdown
from genanki import Note, guid_for

md = markdown.Markdown()

def get_anki_note(item, model, template):
    fmt = item.meta['format']
    if fmt == 'data/dictionary':
        tags = template['Tags']['template'].render(**item.data).split(' ')
        _id = template['ID']['template'].render(**item.data)
    elif  fmt == 'data/text':
        tags = template['Tags']['template'].render(Text = item.data).split(' ')
        _id = template['ID']['template'].render(Text = item.data)
    elif fmt == 'data/list':
        tags = template['Tags']['template'].render(Items = item.data).split(' ')
        _id = template['ID']['template'].render(Items = item.data)
    else:
        raise Exception('Unsupported item format: {fmt}'.format(fmt = fmt))

    tags.insert(0, item.meta['file'])

    fields = []
    for f in model.fields:
        fieldname = f['name']
        tpl = template[fieldname]['template']
        
        if fmt == 'data/dictionary':
            contents = tpl.render(**item.data)
        elif  fmt == 'data/text':
            contents = tpl.render(text = item.data)
        elif fmt == 'data/list':
            contents = tpl.render(items = item.data)

        if template[fieldname]['markdown']:
            contents = md.convert(contents)
            md.reset()
        
        fields.append(contents)

    # print(fields)
    return Note(
        guid = guid_for(_id),
        model = model,
        fields = fields,
        tags = tags
    )