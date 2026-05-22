from dataclasses import dataclass
from lexer.token_types import TokenType

@dataclass
class ScriptToken:
    """
    File name token.py was taken. ScriptToken name is for consistency
    """
    token_type: TokenType
    lexeme: str
    literal: object
    line: int

    def to_string(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.token_type.name + self.lexeme + " " + str(self.literal)
    
