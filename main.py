r"""
Regex Engine:
What is regEx :RegEx stands for Regular Expression
The RegEx is a sequence of characters that forms a search pattern. It is mainly used for string pattern matching. and behind the scenes there is something known as RegEx Engine which is responsible for the 
actual pattern matching process. and these pattern matching process is done through a combination of algorithms and data structures. so let's dive deep into the RegEx Engine and understand 
how it works under the hood.

This is the Code for Building the RegEx engine from the Scratch
This one can handle the core features like character classes [a-zA-Z0-9],
Quantifiers -> * + ? {n,m} , Alternation -> |, (?:...) -> Non Capturing Groups and Capturing groups (?=:...),

"""

"Regex Enginne can be implemented in multiple ways: 1.Thompson's NFA 2.DFA 3.Recursive Descent "

r""" 
Regex Uses Tree and Backtracking
"""


r""" 
How Does a Regex Engine Works:
The User Provides a pattern string and also provide something known as a text.But
Eg. LEt's say we have a hypothetical function called  match .The User will provide two things over here:- The very first string is going to be pattern string  and then a text. 
the goal of this function is to written either a true of false value:

If the pattern string matches this text or not. so let's say the user specifies this particular String.This is a pattern  string and this pattern string goes through a  lexer/tokenizer 
is that characters are converted into tokens.



What are Tokens: Tokens are like a smallest chunk of meaning. the regex engine cannot really make sense of the pattern  unless it first  breakes into smaller chunks.
This is the same reason we don't parse the entire  paragraph letter by letter when we read in the english language. and then our brain groups letters into words  before understanding the sentence. 
words are tokens in english language. They are the smallest chunk of the meaning.The reason we need token because the character alone does nit carry the structure .
The moment you introduce symbol with special behaviour then the raw character stop being enough.     

forExample: As soon as we have this partyicular speacial token 'match("a[bcd]e","abe")' this sqaure bracket things start to make sense differently .
That's why we need to identify these special token and there are a lot of special tokens in regex. So once these characters are converted into tokens and we have a lists  of token object ,
they go they're passed to a parser.



What is a parser: Parser essentially tries to create a relationship between all of these tokens . let's say after the lexer or tokenizer process, 
i have a list of token objects.they are just a list and they does not tell me anything about the relationship of one token with another token we just have the list that simply states that these are the 
tokens objects now parser will create a relation ship surrounding it and it will be in the tree format.
These Tree structure which is specifically called an Abstract syntax tree is created and now That Abstract tree from the parser is given to the matcher engine. 
what this matcher engine does is that the it matches against the text so now the relation ship tree that was created is matched in front of this text because remember that the 
ast we have created is based out of this pattern because well we gave this pattern string into a tokenizer and then that token object was given to a parser to create the tree. 
so indirectly this tree was created out of this pattern string Now we will take that relation ship so that we match it against this 'match("a[bcd]e","abe")' string of token which the text 
'abe' so now the tree follow this text structure and if it does not then we just return a match object which give us the starting the ending and all the captured groups. 
if no match is found then it returns the null and else we will get the result



This is all how the regex engine works at a very high level



what is captured group 
"""


r""" 
Lexer

What is lexer: Lexer is also known as Tokenizer. The main purpose of the lexer is to convert the pattern string into a list of token objects. 
Each token object represents a specific character or a group of characters in the pattern string. The lexer goes through each character in the pattern string and identifies 
what type of character it is and creates a token object accordingly.

Why does the regex engine need a lexer: The regex engine needs a lexer because the pattern string can contain special characters that have specific meanings. 
For example, in the pattern string 'a\d{1,3}(?:foo|bar)?', the '\d' represents a digit, '{1,3}' represents a quantifier, '(?:foo|bar)' represents a non-capturing group and '?' 
represents an optional character. The lexer identifies these special characters and creates token objects accordingly so that the parser can create a relationship between them.
"""

print("a\d{1,3}(?:foo|bar)?")
r""" 
let's go with the above example for explanation/understanding
if tokens are treated as character :
then -> a \ d {1,3} (? : f o o | b a r ) ?  each of this will be considerd seperatly but this is not how  a things work so to solve this we need lexer

and 
In reality, how this regex should be seen is:

a ->  literal character  
\d ->  predefined chracter taken as this is for the digits
{1,3} ->  quantifires token that the minimum value should be 1 and the maximum value should be 3 
(?:foo|bar)  this again is segmented
(?:  ->  start of the non capturing group 
foo  ->  literal character run 
|  ->  alternation
bar  ->  literal character run 
)  -> end of the group 
?  -> this question marks denotes that the either 0(zero)  or  1(one) should be there of this regex


Now let's focus on the  '\d' part as some times we can also have some thing like these:
'\' '\d'  '\\'  '\D'  '\B'  ->  all of this is known through a lexer/tokenizer 
"""


r""" 
let's div into the diagrams for the Lexer

let's take anoter pattern string:
r\d+\(?=px\)

given the pattern string we want to first initialize the lexer. The Lexer will start with postion = 0 and an empty list of tokens = []  
The Position here specifically mean that at what postion at we are in when try to loop over the pattern string so it's going to be 0 at \ and 1 at d 2 will be + and so on.

then we are goping to check that pos < length  so it just mean that we have a while loop so in while loop we just check that we completed parsing or going over this enitre pattern because the length 
is the length of this pattern string [r\d+\(?=px\)] and position is the current index of the pattern
yes and if the condition is right (yes) then we get the current character by doing the pattern at the current position and then we get the character type
and the character type can be multipe things and there are multiple possibilities like 
forexample '\' if it is a backslash than we are just going to do escape the sequence handler we advance that means we move to the very next token or the very next character and 
now we check that the very next character is either on of these: (d,D,w,W,s,S) -> all of these are predefined tokens whjich just means that the character that we'r going to have 
here should be a digit or a word or a whitespace  d stand for Digit, w stands for word and s stands for  white space other than that the another character can be (b,B) and B is a 
boundary token and after that we can have (1-9) what this is a back reference which are some thing like these '\1' or '\2' that are used to get us the first and the second captured group 
and then we have (n,t,r) this would mean that we have '\n' , '\t' and 'r' which have basically the same meaning as what we have in python. it can be a new line,a tab or '\r'. after that there 
can be another token where we just go ahead and create a character token with the escaped literal so all of these can be happen when we have a '\' back-slash




What is boundary token : 

"""

r""" 
Now let's say if there is no backslash instead of that we have an opening paranthesis () that is Group Handler then and after that now we chect that if the next character is a question mark '?' 
The reason we  check it is because this has a special meaning because if the next character is a question mark then we go and get the next character again and cjheck if it is the colon 
(?: -> till now it will look like this and then it will be a non capturing group
now instead of colon if there is an equal to  = then it will be (?=  that means we are creating a look ahead position then let's say if we don't have is equal to = instead we have '!' 
it will be (?! then it is called Look ahead negative token  now let's say if the next character is a smaller than bracket < then we again try to get the next character to create the LookBehind Position 
and after < this if the next character is equal to = it is a LookBehind Position  so now we have (?<= and instead of = we have a question mark ? then it will be (?<? then it will be a lookBehind Negative 
Position token.

Now Instead of backslash and opening paranthesis we have a speacial character these are [ * + ? &{  &}  ,   |   [  ]  ^  $   .    - ]

Other than that we can have a regular character and if it matches none of them 

noe let's say if any of these matches with our pattern string then we just add it to our token list  and we do it until the position is greater than our length of the pattern string then 
what we are going to do after that is to add an EOF token which means end of file.This tells the RegEx Engine that we have completed the entire pattern and now you are at the  end.
and after that we will return the token list this is how the lexer works.


"""

r""" 
Note: For Lexer our entire motive is toh get the each and every character of the pattern string and convert it into a token object so that we can create a relationship between them in the parser phase.

according to our code we go through each and every character of the pattern string and we check what type of character it is and accordingly we create a token object and add it to our token list and at the end we return the token list.
Below is the example/output of the lexer for the pattern string r"a\d{1,3}(?:foo|bar)?"

Output:
[Token(type=<TokenType.CHAR: 1>, value='a', position=0), Token(type=<TokenType.DIGIT: 18>, value='\\d', position=1), 
Token(type=<TokenType.LBRACE: 5>, value='{', position=3), Token(type=<TokenType.CHAR: 1>, value='1', position=4), 
Token(type=<TokenType.COMMA: 7>, value=',', position=5), Token(type=<TokenType.CHAR: 1>, value='3', position=6), Token(type=<TokenType.RBRACE: 6>, value='}', position=7), 
Token(type=<TokenType.NON_CAPTURING: 31>, value='(?:', position=8), Token(type=<TokenType.CHAR: 1>, value='f', position=11), 
Token(type=<TokenType.CHAR: 1>, value='o', position=12), Token(type=<TokenType.CHAR: 1>, value='o', position=13), 
Token(type=<TokenType.PIPE: 8>, value='|', position=14), Token(type=<TokenType.CHAR: 1>, value='b', position=15), Token(type=<TokenType.CHAR: 1>, value='a', position=16), 
Token(type=<TokenType.CHAR: 1>, value='r', position=17), Token(type=<TokenType.RPAREN: 10>, value=')', position=18), Token(type=<TokenType.QUESTION: 4>, value='?', position=19), 
Token(type=<TokenType.EOF: 32>, value=None, position=20)]

"""

r""" 
Now That the Lexer Is done so now let's understand the Parser: What is it, why do we need it and how does it works
"""


r"""
Parser: Parser is used to create a relationship between all of these tokens that we have got from the lexer phase.
let's take an examplepattern string : ab*c/d
here in the above case the pattern string can have 2 possible matches:
1. (ab*c)/d -> here ab*c is one group and then it is followed by /d and it's output can be like these: abc, abbc, abbbc or only d but noty both together.
2. ab*(c/d) -> here c/d is one group and then it is preceded by ab* and it's output can be like these: abcd, abbd, abbbd or only ab* but not both together.
so now the parser's job is to create a relationship between these tokens so that we can know which token is related to which token and how they are related. so to solve this we use Abstract Syntax Tree(AST) to create this relationship. and uses the precedence and associativity rules to create this relationship.

so for more easier understanding let's take an example of maths:
5+4*3 here in this case we can solve it in 2 cases : 1. (5+4)*3 = 27 2. 5+(4*3) = 17 so among these 2 cases the correct one is the second one because according to the maths rules we have precedence and associativity rules like PEMDAS/BODMAS and we cannot just solve it from left to right so in the similar way the regex parser doesn't always goes from left to right and we have to follow the precedence and associativity rules

so now to solve this we use the precedence and associativity rules:
Precedence: It tells us which operator should be evaluated first. in the above case * has higher precedence than + so we will evaluate 4*3 first and then add 5 to it.
Associativity: It tells us the order in which operators of the same precedence should be evaluated.

so the answer for the above case -> ab*c/d is : (ab*c)/d i.e is the 1st one because the * has higher precedence than / so we will evaluate ab*c first and then divide it by d and also the regex engine just doesn't goes up there and put the brackets manually there it just sees the alternation operator i.e / and then just seperate out these (ab*c)/(d).

So how we are going to visualize this? 
Let's again take this example 5+4*3 
The AST for this will be:it will be divided in nodes and there are 5 nodes that are: 5, +, 4, *, 3  -> Below is the representation of the AST:
    +
   / \
  5   *
     / \
    4   3

The similar way we can create the AST for the regex pattern string ab*c/d -> Below is the representation of the AST:
        AlTERNATION '|'
          |       |
        Concat    d
        /  |  \
       a   b   c
           |
           *         

but did i do this: so just follow the rules ->
Grammar (in order of precedence, lowest to highest):
1. Alternation ::= concat ('|' concat)*
2. Concat ::= quantified*
3. Quantified ::= atom quantifiers?
4. Atom ::= CHAR | DOT | PREDEFIEND | GROUP | NON_CAPTURING_GROUP | LOOKAHEAD | LOOKBEHIND | LOOKAHEAD_NEGATIVE | LOOKBEHIND_NEGATIVE | BACKREFERENCE | CHAR_CLASS | NEGATED_CHAR_CLASS | '(' Alternation ')'
5. Quantifiers ::= '*' | '+' | '?' | '{' NUMBER (',' NUMBER?)?

Now let's see how the above grammar works so let's go to the first rule: that the alternation also known as or (has the lowest precedence) ::= concat ('|' concat)* it means that let's take this x|x => here first we have to resolve x it self than only we can go to or '|'  and then only we can go to the next x so this is how the first rule works and we have asterisk sign * at the end which means that this can repeat multiple times so we can have x|x|x|x|x and so on. or we can have only one x or no x at all and also there is no complusion that we need to have alternation operator in the pattern string. let's move ahead to the second rule: Concat ::= quantified*  it means that we have to resolve the quantified part first and then only we can go to the concatenation part and here also we have asterisk sign * at the end which means that this can repeat multiple times so we can have x y z a b c and so on or we can have only one x or no x at all. let's move ahead to the third rule: Quantified ::= atom quantifiers?  it means that we have to resolve the atom part first and then only we can go to the quantifiers part and here we have a question mark ? at the end which means that this part is optional so we can have atom with quantifiers or without quantifiers. let's move ahead to the fourth rule: Atom ::= CHAR | DOT | PREDEFIEND | GROUP | NON_CAPTURING_GROUP | LOOKAHEAD | LOOKBEHIND | LOOKAHEAD_NEGATIVE | LOOKBEHIND_NEGATIVE | BACKREFERENCE | CHAR_CLASS | NEGATED_CHAR_CLASS | '(' Alternation ')'  it means that atom can be any of these things like character, dot, predefined, group, non capturing group, lookahead, lookbehind, lookahead negative, lookbehind negative, backreference, char class, negated char class or alternation within paranthesis. let's move ahead to the fifth rule: Quantifiers ::= '*' | '+' | '?' | '{' NUMBER (',' NUMBER?)?  it means that quantifiers can be any of these things like *, +, ?, {n}, {n,}, {n,m} where n and m are numbers. 

let's take this example of pattern string : ab*c|d => the Parser is going to first look at the first char and as in our case it is a character a and then it's going to look at the next character which is b and both of them will be concatenated together and then it's going to look at the next character which is * and as per our grammar rules * has higher precedence than | so it's going to create a node for * with b as its left child and then it's going to look at the next character which is c and it's going to concatenate it with the result of b* and then it's going to look at the next character which is | and as per our grammar rules | has the lowest precedence so it's going to create a node for | with ab* c as its left child and then it's going to look at the next character which is d and it's going to create a node for d as its right child.



Now let's take an even interesting example of pattern string : a\d{1}(?:foo|bar)  How will it be parsed? Let's break it down step by step:
In this case we don't have an alternaton operator | that's dividing the pattern string except for the 'foo|bar' part and this is not creating a divide between the entire pattern string so first we go ahead and parse 'a' which is a character and then we go ahead  but then we go ahead and parse '\d{1}' here '\d' is a predefined token which means digit and then we have '{1}' here there is an '{' which is a quantifier and has the highest precedence, so we create a node for '{1}' with '\d' as its left child and then we go ahead and parse '(?:foo|bar)+' here '(?:foo|bar)' is a non capturing group and then we have '+' which is a quantifier so we create a node for '+' with '(?:foo|bar)' as its left child and then we go ahead and parse 'd?' here 'd' is a character and then we have '?' which is a quantifier so we create a node for '?' with 'd' as its left child. finally we concatenate all of these together to form the final AST.
Below is the representation of the AST for the pattern string a\d{1}(?:foo|bar) 

Representation AST Tree of a\d{1}(?:foo|bar):
         
                CONCATENATION
                /  |        \                
              /    |         \
           'a'   Quantified   NON_CAPTURING
                   |              |
                  \d         ALTERNATION
                   |            /        \
                  {1}       'foo'      'bar'
                            /              \
                        CONCAT             CONCAT
                        f   o   o         b   a   r






What is AST: AST stands for Abstract Syntax Tree. It is a tree representation of the abstract syntactic structure of the source code written in a programming language.Each node of the tree denotes a construct occuring in the source code.


Parser Implementation: So as we have seen in the above examples that how does an parser implements the grammer rules and creates the AST tree structure. now let's see how we can implement it in code is first we will create a function called parse_alternation() this function will be responsible for parsing the alternation operator | and then we will create a function called parse_concatenation() this function will be responsible for parsing the concatenation operator and then we will create a function called parse_quantified() this function will be responsible for parsing the quantifiers and then we will create a function called parse_atom() this function will be responsible for parsing the atoms and then we wil create the parse_quantifier() function which will be responsible for parsing the quantifiers finally we will create a function called parse() which will be responsible for calling the all the functions in the correct order to create the AST tree structure.

Order of the Functions:
1. parse_alternation()    ----> This is the first function to be called as it has the lowest precedence and then it calls the next function parse_concatenation()
2. parse_concatenation()  ----> This is the second function to be called as it has the second lowest precedence and then it calls the next function parse_quantified()
3. parse_quantified()     ----> This is the third function to be called as it has the middle precedence and then it calls the next function parse_atom()
4. parse_atom()           ----> This is the fourth fuction to be called as it has the second highest precedence and then it calls the next function parse_quantifier()
5. parse_quantifier()     ----> This is the fifth function to be called as it has the highest precedence and then it calls the next function parse()
6. parse()


Note: The parser implementation is done using recursive descent parsing technique. Each function is responsible for parsing a specific part of the grammar and calls the next function in the correct order to create the AST tree structure. and we cannot call the the parse_quantifier funtion just because it has the higgest precedence as it id some thing of like an STACK[LIFO] where the lowest precedence function is called first and then it calls the next function in the correct order to create the AST tree structure.
This above parsing technique is known as Recursive Descent Parsing.: 
Generally in a recursive descent parser, each non-terminal in the grammar is implemented as a separate function in the parser. The function for each non-terminal is responsible for recognizing the corresponding part of the input and constructing the appropriate parse tree node. The functions call each other recursively to handle nested structure in the form of the grammar.

This is also known as Top-Down Parsing or predictive parsing. and these type of prasing technique works really well for LLK Grammars LL(k).what this means is that these LLK is just a shorthand for Left-to-right scanning of the input, Leftmost derivation of the parse tree and k tokens of lookahead to make parsing decisions. so for example if we have something of like these: LL(1) it means that we are scanning the input from left to right and we are constructing the leftmost derivation of the parse tree and we are using 1 token of lookahead to make parsing decisions.
for example let's take this as a pattern string : ab*c|d

In this we read left to right so the first token is 'a' which is a character and then we go ahead and read the next token which is 'b' which is also a character and then we go ahead and read the next token which is '*' which is a quantifier and then we go ahead and read the next token which is 'c' which is also a character and then we go ahead and read the next token which is '|' which is an alternation operator and then we go ahead and read the next token which is 'd' which is also a character. so in this way we are scanning the input from left to right and we are constructing the leftmost derivation of the parse tree and we are using 1 token of lookahead to make parsing decisions. so at each step we are looking at the current token and the next token which is basically 'K' token to lookahead to make parsing decisions.This is just fun fact it doesn't affect the implementation of the parser.

The abstract syntax code is in ast_node.py file.
The Workflow of the Abstract Syntax tree is with the name WorkFlow of AST.svg file.
The Parser code is in the parser.py file.
The Workflow of the Parser is with the name WorkFlow of Parser.svg file.

"""

r""" 
Matcher Module:The Matcher module is responsible for taking the Abstract Syntax Tree (AST) generated by the parser and using it to match input strings against the defined regular expressions. It traverses the AST nodes and applies the corresponding matching logic for each node type.

How does the Matcher works: The Matcher module works by recursively traversing the AST nodes and applying the matching logic for each node type. It starts from the root node of the AST and processes each node based on its type, such as character nodes,quantifier nodes, alternation nodes, and so on. The matcher keeps track of the current position in the input string and attempts to match the pattern defined by the AST against the input string.

The Matcher module also handles backtracking, which is a crucial aspect of regex matching. When a match attempt fails at a certain point in the input string, the matcher can backtrack to previous positions and try alternative paths in the AST to find a successful match.


The Matcher code is in the matcher.py file.

The Workflow of the Matcher is with the name WorkFlow of Matcher.svg file.

Note: The Diagram is a bit complex so please take your time to understand it properly. But still if you have any doubts please feel free to ask me. & i will try to explain it in a theory just below it.

What does a matcher get? for example in a parser module we get a list of token objects from the lexer and then we create a relationship between them in the form of an AST tree structure and then we pass that AST tree to the matcher module so that it can match the input string against the defined regular expression.

In the lexer we gave this particular pattern string ab*|c and this pattern needs to be matched to a text so  we match it to a text string like (abbc,d,abcd)   and this text will be provided by the user. andf this is the particular phase that's where the text comes into picture. we don't need to convert that into a lexer or pass through it to a lexer or we even don't need to do any of the tokenization all of that dosen't need to be done here because we already have a tree structure in the form of AST which was created from the pattern string so now we just need to match that tree structure against this text string by looping/traversing it.


                      alternation
                      /          \
                  Concatenation  'd'
                /       |      \    
              literal  '*'     'c'
              node(a)   |
                      Char
                      Node(b)
                      
Let's take the above example of AST tree structure for the pattern string ab*c|d and let's say the text string provided by the user is abbc so now the matcher will start from the root node which is alternation node and then it will go to the left child which is concatenation node and then it will go to the left child which is literal node 'a' and then it will check if the current character in the text string is 'a' or not if it is then it will move to the next character in the text string and then it will go to the right child which is quantifier node '*' and then it will go to the left child which is char node 'b' and then it will check if the current character in the text string is 'b' or not if it is then it will move to the next character in the text string and then it will check if there are more 'b's in the text string because of the '*' quantifier if there are more 'b's then it will keep moving to the next character in the text string until there are no more 'b's and then it will go to the right child which is literal node 'c' and then it will check if the current character in the text string is 'c' or not if it is then it will move to the next character in the text string and then it will reach the end of the text string and since all characters have been matched successfully it will return a match object indicating a successful match.

and now let's say if the text string provided by the user is d so now the matcher will start from the root node which is alternation node and then it will go to the left child which is concatenation node and then it will go to the left child which is literal node 'a' and then it will check if the current character in the text string is 'a' or not if it is not then it will backtrack to the root node and then it will go to the right child which is literal node 'd' and then it will check if the current character in the text string is 'd' or not if it is then it will move to the next character in the text string and then it will reach the end of the text string and since all characters have been matched successfully it will return a match object indicating a successful match.

Now let's match it with another string abcd so now the matcher will start from the root node which is alternation node and then it will go to the left child which is concatenation node and then it will go to the left child which is literal node 'a' and then it will check if the current character in the text string is 'a' or not if it is then it will move to the next character in the text string and then it will go to the right child which is quantifier node '*' and then it will go to the left child which is char node 'b' and then it will check if the current character in the text string is 'b' or not if it is then it will move to the next character in the text string and then it will check if there are more 'b's in the text string because of the '*' quantifier if there are no more 'b's then it will go to the right child which is literal node 'c' and then it will check if the current character in the text string is 'c' or not if it is then it will move to the next character in the text string and then it will reach the end of the text string but there is still one more character 'd' left in the text string here is where things gets intersting since the d is also in the concatenation node of the tree has only 3 child so well what will it do? will it go to the next child? so well, whenevr it goes to this next child of the alternation node that is 'd' the entire things reset so what ever progress we made like we started from a in abcd we goes to b and then c so this progress of abc is not continued when we move to the new child so again we start from the beginning of the text that is a but our current-tree-node/current-token is matching it with the 'd' and deginetly it won't match and that's why it will be an error.  so since all characters have not been matched successfully it will return null/False indicating no match found.This is how the Matcher of the Regex Engine works.

This intuition is a very simple and does not completely explain the entire diagram but when we will go through groupings and lookahead/lookbehind it will be more complicated but still the basic idea will remain the same that we will traverse the AST tree and match it with the text string provided by the user. 

Note : The result of the matcher is either going to be True or False Value.





r"""      

 


