from dataclasses import dataclass
from typing import Any, Optional, TokenType
from enum import Enum,auto

""" 
What is DataClass:
A Dataclass is a decorator that is used to automatically generate special methods like __init__(), __repr__(), __eq__(), and others for user-defined classes. It is part of the dataclasses module introduced in python 3.7.
"""
class TokenType(Enum):
    """All Possible Token Types in our Regex Engine """
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
    
    
    
    
@dataclass
class Token:
    type: TokenType
    value: Optional[str] = None
    position: int = 0
    
    
class Lexer:
    pass

