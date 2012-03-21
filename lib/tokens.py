SEN = '#'
END = ';'
SEP = ','

SUB = '-'
ADD = '+'
MUL = '*'
DIV = '/'
MOD = '%'
UNA_MIN = '_'
POW = '^'
FAC = '!'

PAR_LEFT = '('
PAR_RIGHT = ')'

ABS = 'abs'
ACOS = 'acos'
ASIN = 'asin'
ATAN = 'atan'
CEIL = 'ceil'
FLOOR = 'floor'
LOG = 'log'
LOG10 = 'log10'
LN = 'ln'
COS = 'cos'
SIN = 'sin'
TAN = 'tan'
SQRT = 'sqrt'

FUNCTIONS = {
    ABS: 1,
    ACOS: 1,
    ASIN: 1,
    ATAN: 1,
    CEIL: 1,
    COS: 1,
    FLOOR: 1,
    LOG: 2,
    LOG10: 1,
    LN: 1,
    SIN: 1,
    SQRT: 1,
    TAN: 1,
}

PI = 'pi'
E = 'e'

CONSTANTS = [PI, E]
UNARY_OPS = [UNA_MIN]
RIGHT_OPS = [FAC]
BINARY_OPS = [SUB, ADD, MUL, DIV, POW, MOD]
SPECIAL_OPS = [SEN, END, SEP]


def get_precedence(token):
    if token in [SEN, END]:
        return 0
    elif token in [SUB, ADD]:
        return 1
    elif token in [MUL, DIV, MOD]:
        return 2
    elif token == UNA_MIN:
        return 3
    elif token == POW:
        return 4
    elif token == FAC:
        return 5
    elif token in [PAR_LEFT, PAR_RIGHT]:
        return 6
    elif token in FUNCTIONS:
        return 7
