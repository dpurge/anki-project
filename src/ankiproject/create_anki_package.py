from pathlib import Path, PurePath
from genanki import Deck, Package, Model

from .get_anki_model import get_anki_model
from .get_data_template import get_data_template
from .get_anki_items import get_anki_items
from .get_anki_note import get_anki_note

def create_anki_package(pkg):

    pkg_dir = PurePath(pkg.filename).parent
    Path(pkg_dir).mkdir(parents=True, exist_ok=True)

    deck = Deck(pkg.deck.id, pkg.deck.name)
    for n in pkg.deck.notes:
        model = get_anki_model(n.model)
        template = get_data_template(n.template)
        for d in n.data:
            items = get_anki_items(d)
            for item in items:
                note = get_anki_note(item = item, model = model, template = template)
                # print(note.guid, note.tags)
                deck.add_note(note)

    package = Package(deck)
    package.write_to_file(pkg.filename)

    return pkg.filename