from typing import List, Set
from lexer import Token, TokenType
from ast_node import *


r"""
https://mermaid.live/view#pako:eNqFV21z2jgQ_isa35d2xiXYQHiZSzvEuAlTYgiQ6fSAYVRbgCdG4ozplWL---nFsmVjknzISLvPPl7ti7ScNJd4SOtoq4D8525gGIFpb44B_ZtEdPdhNiWvCNNNiOB28RF8-vQZjGC4R90gmu3YYgmDCIUYRj7Bf_8Mbz4Pht_tyRSMxrZl92zHshdzLCilYcZiEezCyEiYXL5bKOBEnxk8HyBO8f-yjb_ykafaCIjiaUS20gLSdcEdpuVgtpoed-jEFoCtvpwlVOoYMLYeu-MYWDRaDg2eMZOrRQm2N5zGoEcigUwWpcD-Q3-qg-_DcU8HKHIrMRiFyEMrYSnWPkaeFcD9_hrL4H7ctb7ZU-Eeh6bBpYKlyySlhqPu2HZi8BCSw06arNmmDO0MnaXVHU1fxn3nIQYOwRZMrTDBSxfuokPo4_V1jsFw-K37aHd7y9FwEoMBIa_dDYKepAmoADIB2JG9H_m_0Nssjv2gsJgXLBit4Vss9_Zj31GcuUcbH-e8-ckl77qTEKX-CCLzkugtj-5pGsf21xjcQ_c1lFWQbFCIsIuu1YBFM0krqTccDFiddrG7IUmlZusyQ1Z7y_vhi9Prjn-ohmbeUJim9c-bx9og91V03ukR7kHamiFrIoaXTVCEJ72Y1Xo5IKvncr0o3HJdUp_lyqzw3tGb1_VJrbwHuMKgprgcoaTiEiDjk4p4MidTlnwuELl_TjPC9vym3vr4rqqDLfx9R0Mka6LINBq8TBQm8xqT8S7T8wt9GPpDR2GrveOXcYWKX3R2DMYQr8WNP5trosNCJsrehpBTnvBZByesi__b81y7Qszcp7SIXl9YvBxizVslLf4srlk-BvDP0Tix_2BLvFztZ8ErwAvqWqk6O-OFWjkDl_AjsP77EoMJirhsRhdgHSLkHe--wmCfy05m5ZDE6IFDc2bT8JA1vuTlzojgJK9yEql8RhepVUJ8YSeJlaCLg_LHn7bP7vREQgT8CG33MqQqQQGdhiWV8AP-QHsdYBKBUX9k34z5g3djD-kdm40N5rXJosDlkDgR9Wi9nJ4OQeTvAsXF4jxi5ucRMz-P5KYRMzeN5A_DviYPIz0Q7T3Xsh2veHfjBx59KDpgVqlUFlnB54nYSUQsJ_S5DlCaxT3f8hMt8k5kdU9nOZ4eVnEsqvnkJIQqMp2nglxeYnXaM8umQdWAuUz3-cinU-gvVExAQlscIhVf8mGlAhnTbjbbpoFVv1QMrspVjKxZiKzCs1B8yaJrY-9DevvQiXpMSLT4eBlhU6Ilyz46Uv502l75QdD5Cxmrxmp1AZATtgCtVqs6Mi5ASZslRK1VA7Uvv8T7NqFxUR25KkS9ZtNPtd36BUZcLVchWRteg8hKUfWarm1RuIW-R3_qnBh6rkUbtEVzrUOXdPKAtI7m2hyfKRQeIjI5YlfrRPTe0zU6Waw3cnPYeTBCPR-uQ7iVQuT5EQmfxE8p_otKp48R_oeQFEK3Wuek_dY6n2qNWqXVvK3V6o1mq2kYzYauHZm8Wq-0jarZbLeout5o3Z517Q_nMCpNo1VvV5vVdr3aaNze6to6ZKdJPETYQ6FFDjjSOrVm4_w_j2-YfA


The above link contain the diagram of how does the parser works in RegEx Engine


"""

r"""
Before Coding it up let's have an example (ab*c|d) how we are going to parse this regex:Each character here represents a token and having all of the token how would we create an abstract syntax tree out of it? So to crate an abstract tree we would go left to right and keep going untill we see this | Alternation operator . Because this alternation operator has the lowest precedence of all. So we going to go ahead and have 'a' then 'b' then we going to have '*' and then b and * will be considred as one unit because the * has higher precedence and it means that basically we are saying that we have a quantifier on a 'b' so they will be treated as one unit then we have concatenation operator with this as one of the child and b star * is going to be other child and then we have 'c' which is an another child and then we have an alternation operator  and then 'd'  




"""


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.group_counter = 0

    def current_token(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]

    def advance(self) -> Token:
        token = self.current_token()
        if token.type != TokenType.EOF:
            self.pos += 1
        return token

    def expect(self, token_type: TokenType) -> Token:
        token = self.current_token()
        if token.type != token_type:
            raise ValueError(
                f"Expected {token_type}, got {token.type} at position {token.position}"
            )
        return self.advance()

    def parse(self) -> ASTNode:
        self.parse_alternation()

    def parse_alternation(self) -> ASTNode:
        self.parse_concat()

    def parse_concat(self) -> ASTNode:
        # self
        items = []

        while True:
            token = self.current_token()

            if token.type in (TokenType.PIPE, TokenType.RPAREN, TokenType.EOF):
                break

            if token.type in (TokenType.DASH, TokenType.COMMA):
                self.advance()
                items.append(CharNode(token.value))
                continue

            items.append(self.parse_quantified())

        if len(items) == 0:
            return ConcatNode([])

        if len(items) == 1:
            return items[1]

        return ConcatNode(items)

    def parse_quantified(self) -> ASTNode:
        self.parse_atom()

    def parse_atom(self) -> ASTNode:
        token = self.current_token()

        if token.type == TokenType.CHAR:
            self.advance()
            return CharNode(token.value)

        elif token.type == TokenType.DOT:
            self.advance()
            return DotNode()

        elif token.type == TokenType.CARET:
            self.advance()
            return AnchorNode("^")

        elif token.type == TokenType.DOLLAR:
            self.advance()
            return AnchorNode("$")

        elif token.type == TokenType.WORD_BOUNDARY:
            self.advance()
            return AnchorNode("b")

        elif token.type == TokenType.NON_WORD_BOUNDARY:
            self.advance()
            return AnchorNode("B")

        elif token.type == TokenType.DIGIT:
            self.advance()
            return PredefinedClassNode("d")

        elif token.type == TokenType.NON_DIGIT:
            self.advance()
            return PredefinedClassNode("D")

        elif token.type == TokenType.WORD:
            self.advance()
            return PredefinedClassNode("w")

        elif token.type == TokenType.NON_WORD:
            self.advance()
            return PredefinedClassNode("W")

        elif token.type == TokenType.WHITESPACE:
            self.advance()
            return PredefinedClassNode("s")

        elif token.type == TokenType.NON_WHITESPACE:
            self.advance()
            return PredefinedClassNode("S")

        else:
            pass

    def peek_token():
        pass
