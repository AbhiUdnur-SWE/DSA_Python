class TrieNode:
    """TrieNode"""

    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:
    """Trie"""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """insert"""
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if not node:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end_of_string = True
        print("success")

    def search(self, word: str):
        """search"""
        current = self.root
        for i in word:
            node = current.children.get(i)
            if not node:
                return False
            current = node
        return current.end_of_string

    def delete(self, word: str):
        """delete"""
        return Trie.delete_helper(self.root, word, 0)

    @staticmethod
    def delete_helper(root: TrieNode, word: str, index: int):
        """Recursively delete a word from the Trie.
        Returns True if the word was found and deleted, False otherwise.
        """
        if index >= len(word):
            return False

        ch = word[index]
        if ch not in root.children:
            return False

        current = root.children[ch]
        is_last_char = index == len(word) - 1

        if is_last_char:
            # Reached end of word
            if not current.end_of_string:
                return False  # Word doesn't exist in Trie

            # Mark as not end of string - word is deleted
            current.end_of_string = False

            # Clean up empty nodes
            if len(current.children) == 0:
                root.children.pop(ch)

            return True  # Word was successfully deleted

        # Recursively delete next character
        word_deleted = Trie.delete_helper(current, word, index + 1)

        # Clean up empty nodes
        if word_deleted and len(current.children) == 0 and not current.end_of_string:
            root.children.pop(ch)

        return word_deleted
