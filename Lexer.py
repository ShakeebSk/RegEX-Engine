from dataclasses import dataclass
from typing import Any, Optional, TokenType
from enum import Enum, auto

""" 
What is DataClass:
A Dataclass is a decorator that is used to automatically generate special methods like __init__(), __repr__(), __eq__(), and others for user-defined classes. It is part of the dataclasses module introduced in python 3.7.
"""


""" 
Why we are using auto every where:
The `auto()` function is used to automatically assign unique integer values to each enum member. This simplifies the process of defining enum members and ensures that each one has a distinct value without having to manually specify them.
otherwise we have to do something like this:
class TokenType(Enum):
    CHAR = 1
    STAR = 2
    PLUS = 3
    QUESTION = 4
    LBRACE = 5
    RBRACE = 6
    COMMA = 7
    PIPE = 8
    LPAREN = 9
    RPAREN = 10
    LBRACKET = 11
    RBRACKET = 12
    CARET = 13
    DASH = 14
    DOT = 15
    DOLLAR = 16
    BACKSLASH = 17
"""


class TokenType(Enum):
    """All Possible Token Types in our Regex Engine"""

    CHAR = auto()  # Regular Character (A-Z, a-z, 0-9, etc.)
    STAR = {
        auto()  # * (Zero or more) -> for example : ab*c matches "ac" ,"abc" ,"abbc" and more...
    }

    PLUS = {
        auto()  # + (One or more) -> for example: ab+c matches "abc", "abbc", but not "ac"
    }

    QUESTION = {
        auto()  # ? (Zero or one) -> for example: ab?c matches "ac" and "abc" another example is: colou?r matches "color" and "colour"
    }

    # Range Quantifiers: generally used together
    # For Example,
    # {n} : Matches the preceding token exactly n  times.
    # {n,} : Matches the preceding token n or more times.
    # {n,m} : Matches the preceding token at least n times but no motre than m times.

    """ 
    let's  take an example: => a\d{1,3} it means that first we want to match the literal character 'a' followed by a digit (\d) that occurs at least 1 time but no more than 3 times. so let's say if we have a string like 'a5' it will match because '5' is a digit and it occurs once which is within the specified range of 1 to 3. similarly 'a23' will also match because '23' consists of two digits, which is also within the range. however, 'a4567' will not match because '4567' has four digits, exceeding the maximum limit of 3.
    """

    LBRACE = auto()
    RBRACE = auto()
    COMMA = auto()

    PIPE = auto()  # | (Alternation) -> for example: foo|bar matches "foo" or "bar"

    """ 
    Grouping Tokens:
    Generally used to group multiple tokens together and to create sub-expressions within a regex pattern.
    It has two types:
    1. Capturing Group: ( ... ) -> for example: (abc) matches
    2. Non-Capturing Group: (?: ... ) -> for example: (?:abc) matches
    3. Captured Group is used when we want to extract a specific part of the matched string for further processing or analysis. It allows us to create sub-expressions within a regex pattern and capture the matched content for later use.
    
    # 1. Quantifier - (ha)+ matches "ha", "haha", "hahaha". Without parens, ha+ would match "ha", "haa", "haaa".
    # 2. Capture Grouping - to capture the matched text. For example, if we have regex like (\d{3})-(\d{4}) used on "555-1212", it captures "555" as group 1 and "1212" as group 2.
    """
    LPAREN = auto()
    RPAREN = auto()

    """ 
    Character Classes:
    # Matches any single character that is present inside the brackets.
    # Example: gr[ae]y matches both "gray" and "grey". [0-9] matches any single digit.
    """
    LBRACKET = auto()
    RBRACKET = auto()

    # When used as the first character inside a character class ([...]), it negates the set. It matches any single character not in the set.
    # Example: [^aeiou] matches any single character that is not a lowercase vowel (e.g., "b", "c", "1", "$").
    CARET = auto()

    # When used inside a character class ([...]) between two characters, it defines a range.
    # Example: [a-z] matches any lowercase letter. [a-zA-Z0-9] matches any alphanumeric character.

    DASH = auto()  # -

    # Special characters
    # The "wildcard." It matches any single character except (usually) a newline character (\n).
    # Example: h.t matches "hat", "hot", "h8t", "h&t", etc.

    DOT = auto()  # .

    # An anchor. It asserts that the current position is the end of the string (or the end of a line in multiline mode).
    # Example: world$ matches "hello world" but does not match "world peace".
    DOLLAR = auto()  # $

    # The escape character. It has two main jobs:
    # It removes the special meaning from a metacharacter.
    # It signals the start of a special sequence (like \d).
    # Example (Escape): To match a literal dot, you use \.. To match a literal plus sign, you use \+.
    # Example (Sequence): \d matches a digit.

    BACKSLASH = auto()  # \  (for escape sequences)

    # Special escape sequences
    DIGIT = auto()  # \d - Matches any digit. Equivalent to [0-9].
    NON_DIGIT = auto()  # \D -Matches any non-digit. Equivalent to [^0-9].

    WORD = (
        auto()  # \w - Matches any word character (alphanumeric + underscore). Equivalent to [a-zA-Z0-9_].
    )

    NON_WORD = (
        auto()  # \W - Matches any non-word character. Equivalent to [^a-zA-Z0-9_].
    )

    WHITESPACE = (
        auto()  # \s - Matches any whitespace character (spaces, tabs, line breaks). Equivalent to [ \t\n\r\f\v].
    )

    NON_WHITESPACE = (
        auto()  # \S - Matches any non-whitespace character. Equivalent to [^ \t\n\r\f\v].
    )

    # Word boundary - Matches the position between a word character (\w) and a non-word character (\W), or the start/end of the string.
    # Example: \bcat\b matches "cat" in "The cat sat" but does not match "cat" in "tomcat".
    WORD_BOUNDARY = auto()  # \b
    NON_WORD_BOUNDARY = auto()  # \B

    """ 
    Backrefrences: Matches the exact text that was previously captured by the  capturing group ((....)) 
    for ex: \1 refers to the first captured group, \2 refers to the second captured group, and so on.
    Example: (abc)\1 matches "abcabc" because \1 refers to the first captured group (abc).
    Example: \bcat\b matches "cat" in "The cat sat" but does not match "cat" in "tomcat".
    """
    BACKREF = auto()  # \1, \2, .... \9 (Backreferences)

    # Lookahed/Lookbehind markers

    LOOKAHEAD_POS = (
        auto()  # (?= -> Password(?=.*[0-9]) checks if the password contains at least one digit. Example: "Password123" matches, "Password abc" does not but "Password abc 123" does. Asserts that the pattern inside (?=...) must follow the current position, but isn't part of the match.
    )  # (?=...) (Lookahead)
    LOOKAHEAD_NEG = (
        auto()  # (?! -> Password(?!.*[0-9]) checks if the password does not contain any digits. Example: "Password" matches, "Password123" and "Password abc 123" do not match. Asserts that the pattern inside (?!...) must NOT follow the current position, but isn't part of the match
    )  # (?!...) (Negative Lookahead)
    LOOKBEHIND_POS = (
        auto()  # (?<= -> (?<=abc) checks if the string contains "abc" before the current position. Example: "abcxyz" matches, "xyzabc" does not. Asserts that the pattern inside (?<=...) must precede the current position, but isn't part of the match.
    )  # (?<=...) (Lookbehind)
    LOOKBEHIND_NEG = (
        auto()  # (?<! -> (?<!abc) checks if the string does not contain "abc" before the current position. Example: "abcxyz" does not match, "xyzabc" matches. Asserts that the pattern inside (?<!...) must NOT precede the current position, but isn't part of the match.
    )

    NON_CAPTURING = (
        auto()
    )  # (?: -> (?:http|https):// groups "http" and "https" for the | operator, but you can't reference it with \1. Doesnt capture anything.

    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: Optional[str] = None
    position: int = 0


class Lexer:
    pass
