from operator import itemgetter


class Frequence:
    """
    Generate the frequency of each character in the initial text
    """
    def get_frequence(text):
        """
        Get frequency of each character

        Attrs:
            text (str): text we want to know the frequency of each character

        Returns:
            list: List composed of character and frequency list
        """

        lex = [[], []]

        for c in text:
            if c not in lex[0]:
                lex[0].append(c)
                lex[1].append(1)

            else:
                index = lex[0].index(c)
                lex[1][index] += 1

        newLex = []
        for i in range(len(lex[0])):
            newLex.append((lex[0][i], lex[1][i]))

        newLex.sort(key=itemgetter(1))

        return newLex
