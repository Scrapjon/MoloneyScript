from enum import Enum


"""
Placeholder tokens taken from CraftingInterpreters.
This will be changed to be specific to this language.
There also surely has to be a way to define this better without explicitly specifying the token number for each token.
"""
class TokenType(Enum):
    # Single character tokens:
    LEFT_PAREN = 0,
    RIGHT_PAREN = 1,
    LEFT_BRACE = 2,
    RIGHT_BRACE = 3,
    COMMA = 4,
    DOT = 5,
    MINUS = 6,
    PLUS = 7,
    SEMICOLON = 8,
    SLASH = 9,
    STAR = 10,

    # One or two character tokens:
    BANG = 11,
    BANG_EQUAL = 12,
    EQUAL = 13,
    EQUAL_EQUAL = 14,
    GREATER = 15,
    GREATER_EQUAL = 16,
    LESS = 17,
    LESS_EQUAL = 18,

    # Literals
    IDENTIFIER = 19,
    STRING = 20,
    NUMBER = 21,

    # Keywords
    AND = 22,
    CLASS = 23,
    ELSE = 24,
    FALSE = 25,
    FOR = 26,
    IF = 27,
    NIL = 28,
    OR = 29,
    PRINT = 30,
    RETURN = 31,
    SUPER = 32,
    THIS = 33,
    TRUE = 34,
    VAR = 35,
    WHILE = 36
