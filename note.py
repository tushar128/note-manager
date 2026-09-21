"""note.py - defines the Note class."""

from datetime import datetime


class Note:
    """A single note with a title, content, tags and a creation timestamp."""

    def __init__(self, title, content, tags=None, timestamp=None):
        self.title = title
        self.content = content
        # Store a copy so outside code can't mutate our list by accident
        self.tags = list(tags) if tags else []
        # ISO-format string, e.g. "2025-12-03T10:45:00.123456"
        self.timestamp = timestamp or datetime.now().isoformat()

    def save(self):
        """Return all attributes as a JSON-serialisable dictionary."""
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a Note from a dictionary (used when loading from JSON)."""
        return cls(
            title=data.get("title", "Untitled"),
            content=data.get("content", ""),
            tags=data.get("tags", []),
            timestamp=data.get("timestamp"),
        )

    def display(self):
        """Print the note in a formatted layout."""
        print(f"Title: {self.title}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Tags: {', '.join(self.tags)}")
        print(f"Content: {self.content}")
        print("-" * 27)

    def matches_search(self, term):
        """True if `term` appears in the title, content, or any tag (case-insensitive)."""
        term = term.lower()
        return (
            term in self.title.lower()
            or term in self.content.lower()
            or any(term in tag.lower() for tag in self.tags)
        )

    def has_tag(self, tag):
        """True if the note has exactly this tag (case-insensitive). Used by the bonus filter."""
        return tag.lower() in (t.lower() for t in self.tags)

    def __repr__(self):
        return f"Note(title={self.title!r}, tags={self.tags!r})"
