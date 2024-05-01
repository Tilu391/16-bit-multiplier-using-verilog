import ply.lex as lex
import ply.yacc as yacc

tokens = [
        'ID', 
        'L_PARENTHESIS', 
        'R_PARENTHESIS',
        'L_BRACES',
        'R_BRACES',
        'SEMICOLON',
        'NEWLINE',
        'EQUALS',
        'GREATER_THAN_OR_EQUAL_TO',
        'LESSER_THAN_OR_EQUAL_TO',
        'GREATER_THAN',
        'LESSER_THAN',
        'INCREMENT',
        'DECREMENT',
        'ASSIGN',
        'NUMBER',
        'NOTEQUALS',
        'DOUBLE_COLLON',
        'COMMA'
        ]

reserved = {
    'while': 'while',
    'statement':'statement',
    'for':'for',
    'do':'do',
   
}
t_COMMA =r"\,"
t_ignore = " \t"
t_NEWLINE=r"\n"
t_SEMICOLON=r"\;"
t_DOUBLE_COLLON = r"\:"
t_L_PARENTHESIS=r"\("
t_R_PARENTHESIS=r"\)"
t_L_BRACES=r'\{'
t_R_BRACES=r'\}'
t_ASSIGN = r'\='
t_EQUALS = r'\=='
t_NOTEQUALS = r'\!='
t_GREATER_THAN_OR_EQUAL_TO = r'\>='
t_LESSER_THAN_OR_EQUAL_TO = r'\<='
t_GREATER_THAN = r'\>'
t_LESSER_THAN = r'\<'
t_INCREMENT = r'\++'
t_DECREMENT = r'\--'
t_NUMBER = r'\d+'

tokens += list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_FOR(t):
    r'\for'
    return t


def t_WHILE(t):
    r'\while'
    return t

def t_DO(t):
     r'\do'
     return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

lexer = lex.lex()

def p_main(p):
    '''main : program'''
    print("Syntax is Correct.")

def p_program(p):
    '''program : For
                | While
                | Dowhile
                
                '''

def p_While(p):
    '''While : while WhileCondition Block '''

def p_WhileCondition(p):
    '''WhileCondition : L_PARENTHESIS Check R_PARENTHESIS '''

def p_Block(p):
    '''Block : Newline L_BRACES Newline Body Newline R_BRACES'''

def p_For(p):
    '''For : for forCondition Block'''

def p_condition(p):
    '''forCondition : L_PARENTHESIS Assign SEMICOLON Check SEMICOLON Action R_PARENTHESIS
                    | L_PARENTHESIS Assign COMMA Assign SEMICOLON Check COMMA Check  SEMICOLON Action COMMA Action R_PARENTHESIS '''

def p_Dowhile(p):
    '''Dowhile : do Block while WhileCondition '''

def p_condition_part_one(p):
    '''Assign : ID ASSIGN ID
                | ID ASSIGN NUMBER'''

def p_condition_part_two(p):
    '''Check : Alnum EQUALS Alnum
             | Alnum NOTEQUALS Alnum
             | Alnum GREATER_THAN Alnum
             | Alnum LESSER_THAN Alnum
             | Alnum GREATER_THAN_OR_EQUAL_TO Alnum
             | Alnum LESSER_THAN_OR_EQUAL_TO Alnum'''


def p_condition_part_three(p):
    '''Action : ID INCREMENT
                | ID DECREMENT
                | INCREMENT ID
                | DECREMENT ID
                | ID ASSIGN ID'''

def p_alnum(p):
    '''Alnum : ID
             | NUMBER'''

def p_newline(p):
    '''Newline : Newline NEWLINE
                | '''

def p_body(p):
    '''Body : statement 
            | statement Body
            | program Body
            | '''

def p_error(p):
    print("Syntax error!")
    quit()

yacc.yacc()

data='''for(i=0,J=0;i<6,J<8;i++J++)
{
    while(i<4)
    {
        do
        {
            statement
        }
        while(i<2)
    }
}
'''


yacc.parse(data)