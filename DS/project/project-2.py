class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def add_text(self, new_text):
        # Save current state to undo stack before making changes
        self.undo_stack.append(self.text)
        # Clear redo stack as new action invalidates redo history
        self.redo_stack.clear()
        # Add new text
        self.text += new_text

    def remove_text(self, length):
        # Save current state to undo stack before making changes
        self.undo_stack.append(self.text)
        # Clear redo stack as new action invalidates redo history
        self.redo_stack.clear()
        # Remove text from the end
        self.text = self.text[:-length]

    def undo(self):
        if self.undo_stack:
            # Push the current state to redo stack
            self.redo_stack.append(self.text)
            # Pop from undo stack and set as current state
            self.text = self.undo_stack.pop()
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.redo_stack:
            # Push the current state to undo stack
            self.undo_stack.append(self.text)
            # Pop from redo stack and set as current state
            self.text = self.redo_stack.pop()
        else:
            print("Nothing to redo.")

    def get_text(self):
        return self.text

# Example usage
def main():
    editor = TextEditor()
    while True:
        print("\nText Editor")
        print("1. Add Text")
        print("2. Remove Text")
        print("3. Undo")
        print("4. Redo")
        print("5. View Text")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_text = input("Enter text to add: ")
            editor.add_text(new_text)
        elif choice == '2':
            length = int(input("Enter number of characters to remove from the end: "))
            editor.remove_text(length)
        elif choice == '3':
            editor.undo()
        elif choice == '4':
            editor.redo()
        elif choice == '5':
            print(f"Current text: {editor.get_text()}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
