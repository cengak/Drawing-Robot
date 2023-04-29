# lexer.input(data). Reset the lexer and store a new input string.
# lexer.token(). Return the next token. Returns a special LexToken instance on success or None if the end of the input text has been reached.
# lexer = lex.lex()


from pickle import TRUE
from re import T, X
import lex
import yacc
import turtle

pattern = turtle.Turtle()
# pattern.forward(100)
# turtle.done()


# List of token names.   This is always required
tokens = (
    'NUMBER',
    'RED',
    'GREEN',
    'BLUE',
    'BLACK',
    'FORW',
    'RIGHT',
    'LOOP',
    'COLOR',
    'PEN',
    'LSQB',
    'RSQB',
    'EMPTY'
    
)
 
# Regular expression rules for simple tokens
t_FORW    = r'F'
t_RIGHT   = r'R'
t_LOOP   = r'L'
t_COLOR  = r'COLOR'
t_PEN  = r'PEN'
t_LSQB  = r'\['
t_RSQB  = r'\]'
t_RED  = r'K'
t_GREEN  = r'Y'
t_BLUE  = r'M'
t_BLACK  = r'S'
t_EMPTY = r'\ '


 
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

# Test it out
data = 'F 100 R 90 F 50'
 
# Give the lexer some input
lexer.input(data)

token_list=[]

# Tokenize 
for tok in lexer:
   token_list.append(tok)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)


########################################
#PARSER



def my_forward(index):
          
    a = token_list[index]   
    b = int(a)
    
    pattern.forward(b)
    # turtle.done()
    
# def my_right(index):
  
#     c = token_list[index]
#     d = int(c)
            
#     pattern.right(d)
#     # turtle.done()

my_list = []

i=0
for x in token_list:
    z = x
    s = str(z)
    my_list.append(s)
    i=i+1

    print(my_list)


    
    
turtle.done()  


       
# def p_grammer_statement(p):
#  'statement : function value option' 
#  p[0] = p[1]

# def p_option(p):
#  '''option : statement 
#            | loop 
#            | EMPTY '''

#  if p[1] == 'statement':
#     p[0] = p[1]

#  elif p[1] == 'loop':
#     p[0] = p[1]

#  elif p[1] == 'EMPTY':
#     p[0] = p[1]

# def t_FORW():
#  i=0
#  for token in token_list:
#     if i>=0:
#      i=i+1
#      pattern = turtle.Turtle()                   
#      pattern.forward(token_list[i])
        
# def p_function(p):
#   'function : FORW'
  
#   if p[1] == 'FORW':
#     print('hello')


    
# def p_value(p):
#  '''value : NUMBER'''

#  if p[1] == 'NUMBER':
#      p[0] = p[1]


 
# def p_colors(p):
#  'colors : RED'
#  if p[1] == 'RED':
#   p[0] = p[1]

# def p_loop(p):
#  'loop : LSQB statement RSQB'
#  p[0] = p[2]
 
# def p_error(p):
#      print("Syntax error in input!")
 
# # Build the parser
# parser = yacc.yacc()

# print(token_list)

