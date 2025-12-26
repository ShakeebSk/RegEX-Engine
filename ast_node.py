from dataclasses import dataclass
from typing import Set, List, Optional

r""" 
https://mermaid.live/view#pako:eNqtls1y2jAQx19F1SlpDQOBgO2hyVDS6XQmTdqmp-BMRtgL1sSWXFluoYRrH6CP2Cfpmk9jBOFQLtja__682g-NptSXAVCX-hFL0yvORorFniD4m6-Q7t23G1SQ6WIx_3U6bJBqxXx9cbFYnXmi6NMLmSo7vfFx0SXoZ3S5krroYQD28icjNXXJHeg-oh8KFgEjpiFwyUDKyEj9rCCAIRcQ7GHnq496ksD-uL9kTGg-5GDaMI_w88sEFgwxF4--zIR2CRe6aGDjleE20VwKFvVRUdzVSAEEkwOb6knhM20ORoFwyTVPdX8Z1IMR0Y00KMHyAHY4bGX7AekxrA9KZsnxqRnl8keRxQNQheyUoDdS9FiiM8XF6PgPlCDvmP-kYAiYFB92AMcF0hV-KHcrz-bLL3TOtZRPLAQWHJ-dRKY8z_yB8ufUAYRc_C_sav47z5XKerANpuUA73FaD5jBbhhDg2p70EyfWTe-wVhqaYNi3UcGm7HfDLqdljJFsm4Zg3GrJ_bYN9Vdlah0BlUqF2svl_hSaMZFupAWTodDsvIJcEi7GcBDKvPIHvLYno-XlIWe3yddiIXUQIZSlbPm0W6SRBxSoiVhYkLm44JyzLMn3o9ZnET5kcdeW2TwxiL-pUWCacM6n3m0RC4k2aMf0Y_7XJMUvmfYF7j_DQ9xA5_8_f1n6XPSZ0hH-MPpDrVcE4_efiUyAcW0VFvI58HzAlpwOUTe1MOjiyJhFmKm_RAComGskT7XkMV5iFmoW-TMIg2LVKvVHd525Tx6D0pWfvJAhwTnG1QeDyJPLt-i9ylBj5PLV_mjkVSo7AFUp8DqLGHUojGomPEA7zfzk9CjOoQYPOriIx46LIt0_tEZSlmm5d1E-NTVKgOL4oZH4eolSwK8TCyvR6tFCDim_tPy_pT_WTRh4l7KtQRfqTulY-qe29V23Wk7rZrdbDXqjbpFJ9S1q7Vm23HaDbuOpmb9bGbRX3P_WtWx63W7aTuOXWs57VbDoiOVb2UZHogAVC-_LVDXmf0D8LgZww


The above link contains the simple diagram of how the we are going to make the abstract node structure for our regex engine.
"""


@dataclass
class ASTNode:
    pass


@dataclass
class CharNode(ASTNode):
    char: str

    def __repr__(self):
        return f"Char({self.char!r})"


@dataclass
class DotNode(ASTNode):
    def __repr__(self):
        return "Dot(.)"


@dataclass
class CharClassNode(ASTNode):
    chars: Set[str]
    negated: bool = False

    def __repr__(self):
        prefix = "^" if self.negated else ""
        chars_str = "".join(sorted(self.chars)[:10])
        if len(self.chars) > 10:
            chars_str += "..."
        return f"CharClass([{prefix}{chars_str}])"


@dataclass
class PredefinedClassNode(ASTNode):
    class_type: str  # e.g., \d, \w, \s

    def __repr__(self):
        return f"PredefinedClass({self.class_type!r})"


@dataclass
class QuantifierNode(ASTNode):
    child: ASTNode
    min_count: int
    max_count: Optional[int]
    greedy: bool = True  # false for lazy quantifiers (*?,+?,??,{n,m})

    def __repr__(self):
        if self.min_count == 0 and self.max_count == 1:
            q = "?" if self.greedy else "??"

        elif self.min_count == 0 and self.max_count is None:
            q = "*" if self.greedy else "*?"

        elif self.min_count == 1 and self.max_count is None:
            q = "+" if self.greedy else "+?"

        else:
            q = f"{{{self.min_count},{self.max_count}}}"
            if not self.greedy:
                q += "?"
        return f"Quatifier({self.child} {q})"


@dataclass
class ConcatNode(ASTNode):
    children: List[ASTNode]

    def __repr__(self):
        return f"Concat({self.children})"


@dataclass
class AlternationNode(ASTNode):
    alternatives: List[ASTNode]

    def __repr__(self):
        return f"Alternation({self.alternatives})"


@dataclass
class GroupNode(ASTNode):
    child: ASTNode
    group_number: int

    def __repr__(self):
        return f"Group#{self.group_number}({self.child})"


@dataclass
class NonCapturingGroupNode(ASTNode):
    child: ASTNode

    def __repr__(self):
        return f"NonCapturingGroup({self.child})"


@dataclass
class BackreferenceNode(ASTNode):
    group_number: int

    def __repr__(self):
        return f"Backref(\\{self.group_number})"


@dataclass
class AnchorNode(ASTNode):
    anchor_type: str  # '^', '$', 'b', 'B'

    def __repr__(self):
        symbols = {"^": "^", "$": "$", "b": r"\b", "B": r"\B"}
        return f"Anchor({symbols.get(self.anchor_type,self.anchor_type)})"


@dataclass
class LookaheadNode(ASTNode):
    child: ASTNode
    positive: bool = True

    def __repr__(self):
        prefix = "?=" if self.positive else "?!"
        return f"Lookahead({prefix}{self.child})"


@dataclass
class LookbehindNode(ASTNode):
    child: ASTNode
    positive: bool = True

    def __repr__(self):
        prefix = "?<=" if self.positive else "?<!"
        return f"Lookahead({prefix}{self.child})"
