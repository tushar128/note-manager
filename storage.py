"""storage.py - handles reading/writing notes to notes.json."""

import json
from pathlib import Path

from .note import Note

# notes.json lives in the project root (next to main.py)
NOTES_FILE = Path(__file__).resolve().parent.parent / "notes.json"


def save_notes(notes_list):
    """Write a list of notes to notes.json.

    Accepts a list of dictionaries (as in the spec) or Note objects,
    which are converted with Note.save().
    """
    data = [n.save() if isinstance(n, Note) else n for n in notes_list]
    try:
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except OSError as e:
        print(f"Error: could not save notes ({e}).")
        return False


def load_notes():
    """Return a list of Note objects from notes.json.

    Returns an empty list if the file is missing, corrupted, or has
    an unexpected structure - the program never crashes on load.
    """
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("notes.json must contain a list")
        return [Note.from_dict(item) for item in data if isinstance(item, dict)]
    except FileNotFoundError:
        return []  # first run - nothing saved yet
    except json.JSONDecodeError:
        print("Warning: notes.json is corrupted. Starting with an empty list.")
        return []
    except (ValueError, AttributeError, OSError) as e:
        print(f"Warning: could not load notes ({e}). Starting with an empty list.")
        return []
