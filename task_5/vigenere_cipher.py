"""  Class  """

class VigenereCipher:
    """VigenereCipher class  
    """
    def __init__(self, keyword):
        """Initial methdod
        keyword - word that will be used for cipher
        """
        self.keyword = keyword.upper()

    def _code(self, text, combine_func):
        """ private method for encoding and decoding"""
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for letter,k in zip(text, keyword):
            combined.append(combine_func(letter,k))
        return "".join(combined)

    def encode(self, plaintext):
        """ Encoding method """
        return self._code(plaintext, self.combine_character)

    def decode(self, ciphertext):
        """ Decoding method """
        return self._code(ciphertext, self.separate_character)

    @staticmethod
    def separate_character(cypher, keyword):
        """Separate two values to have first text"""
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)

    @staticmethod
    def combine_character(plain, keyword):
        """Combines two character to find ciphre"""
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)

    def extend_keyword(self, number):
        """Dublicate word to cover all text length"""
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]
