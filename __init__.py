"""note_manager package - exports the Note class and storage functions."""

from .note import Note
from .storage import save_notes, load_notes

__all__ = ["Note", "save_notes", "load_notes"]
