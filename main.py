"""
    contient une fonction ispalindrome 
    qui retourne si la string passée en paramètre est un palindrome
    et un fonction main qui fait appel à ispalindrome
"""
import string
from unidecode import unidecode
#### Fonction secondaire


def ispalindrome(p):
    """
        retourne si la string passée en paramètre est un palindrome
    """
    p_min = p.lower()
    p_sans_espace = p_min.replace(" ","")
    p_sans_accent = unidecode(p_sans_espace)
    p_final = p_sans_accent.translate(str.maketrans("","", string.punctuation))
    return p_final == p_final[::-1]
#### Fonction principale


def main():
    """
    fait appel à la fonction ispalindrome
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
