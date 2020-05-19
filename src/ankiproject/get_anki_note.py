from genanki import Note, guid_for

#class AnkiNote(Note):
#  @property
#  def guid(self):
#    return genanki.guid_for(self.fields[0], self.fields[1], self.fields[2])

def get_anki_note(item, model, template):
    fmt = item.meta['format']
    if fmt == 'data/dictionary':
        tags = template['Tags']['template'].render(**item.data).split(' ')
        _id = template['ID']['template'].render(**item.data)
    elif  fmt == 'data/text':
        tags = template['Tags']['template'].render(text = item.data).split(' ')
        _id = template['ID']['template'].render(text = item.data)
    elif fmt == 'data/list':
        tags = template['Tags']['template'].render(items = item.data).split(' ')
        _id = template['ID']['template'].render(items = item.data)
    else:
        raise Exception('Unsupported item format: {fmt}'.format(fmt = fmt))

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
        
        fields.append(contents)

    return Note(
        guid = guid_for(_id),
        model = model,
        fields = fields,
        tags = tags
    )