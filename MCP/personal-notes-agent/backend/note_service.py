from .models import Note

def save_note(db, text):

    note = Note(
        note_text=text
    )

    db.add(note)
    db.commit()

    return note


def get_notes(db):

    return db.query(Note).all()


def delete_note(db, note_id):

    note = db.query(Note).filter(
        Note.id == note_id
    ).first()

    if note:
        db.delete(note)
        db.commit()

    return True