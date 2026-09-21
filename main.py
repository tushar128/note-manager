"""main.py - menu-driven CLI for the note manager."""

from note_manager import Note, save_notes, load_notes


def show_menu():
    print("\n===== NOTE MANAGER =====")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")
    print("6. Filter by Tag (bonus)")


def autosave(notes):
    save_notes([n.save() for n in notes])


def add_note(notes):
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    content = input("Content: ").strip()
    raw_tags = input("Tags (comma-separated): ")
    tags = [t.strip() for t in raw_tags.split(",") if t.strip()]
    notes.append(Note(title, content, tags))
    autosave(notes)
    print("Note added and saved.")


def view_all(notes):
    if not notes:
        print("No notes yet.")
        return
    for i, note in enumerate(notes, start=1):
        print(f"\n[{i}]")
        note.display()


def search_notes(notes):
    term = input("Search keyword: ").strip()
    if not term:
        print("Please enter a keyword.")
        return
    results = [n for n in notes if n.matches_search(term)]
    if not results:
        print("No matching notes found.")
        return
    print(f"\nFound {len(results)} matching note(s):")
    for note in results:
        print()
        note.display()


def delete_note(notes):
    if not notes:
        print("No notes to delete.")
        return
    view_all(notes)
    try:
        index = int(input("\nEnter note number to delete: "))
    except ValueError:
        print("Invalid input - please enter a number.")
        return
    if 1 <= index <= len(notes):
        removed = notes.pop(index - 1)
        autosave(notes)
        print(f"Deleted '{removed.title}'.")
    else:
        print("Invalid note number.")


def filter_by_tag(notes):
    tag = input("Tag to filter by: ").strip()
    if not tag:
        print("Please enter a tag.")
        return
    results = [n for n in notes if n.has_tag(tag)]
    if not results:
        print(f"No notes tagged '{tag}'.")
        return
    print(f"\nNotes tagged '{tag}':")
    for note in results:
        print()
        note.display()


def main():
    notes = load_notes()
    print(f"Loaded {len(notes)} note(s).")

    actions = {
        "1": add_note,
        "2": view_all,
        "3": search_notes,
        "4": delete_note,
        "6": filter_by_tag,
    }

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "5":
            autosave(notes)  # auto-save before quitting
            print("Notes saved. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(notes)
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
