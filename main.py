r"""
Regex Engine:
What is regEx :RegEx stands for Regular Expression

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
Eg. LEt's say we have a hypthetical function called  match .The User will provide two things over here:- The very first string is going to be pattern string  and then a text. the goal of this function is to written either a true of false value:

If the pattern string matches this text or not. so let's say the user specifies this particular String.This is a pattern  string and this pattern string goes through a  lexer/tokenizer is that characters are converted into tokens.



What are Tokens: Tokens are like a smallest chunk of meaning. the regex engine cannot really make sense of the pattern  unless it first  breakes into smaller chunks.This is the same reason we don't parse the entire  paragraph letter by letter when we read in the english language. and then our brain groups letters into words  before understanding the sentence. words are tokens in english language. They are the smallest chunk of the meaning.The reason we need token because the character alone does nit carry the structure .The moment you introduce symbol with special behaviour then the raw character stop being enough.     forExample: As soon as we have this partyicular speacial token 'match("a[bcd]e","abe")' this sqaure bracket things start to make sense differently .That's why we need to identify these special token and there are a lot of special tokens in regex. So once these characters are converted into tokens and we have a lists  of token object ,they go they're passed to a parser.



What is a parser: Parser essentially tries to create a relationship between all of these tokens . let's say after the lexer or tokenizer process, i have a list of token objects.they are just a list and they does not tell me anything about the relationship of one token with another token we just have the list that simply states that these are the tokens objects now parser will create a relation ship surrounding it and it will be in the tree format.
These Tree structure which is specifically called an Abstract syntax tree is created and now That Abstract tree from the parser is given to the matcher engine. what this matcher engine does is that the it matches against the text so now the relation ship tree that was created is matched in front of this text because remember that the ast we have created is based out of this pattern because well we gave this pattern string into a tokenizer and then that token object was given to a parser to create the tree. so indirectly this tree was created out of this pattern string Now we will take that relation ship so that we match it against this 'match("a[bcd]e","abe")' string of token whic the text 'abe' so now the tree follow this text structure and if it does not then we just return a match object which give us the starting the ending and all the captured groups. if no match is found then it returns the null and else we will get the result



This is all how the regex engine works at a very high level



what is captured group 
"""


r""" 
Lexer

What is lexer: Lexer is also known as Tokenizer. The main purpose of the lexer is to convert the pattern string into a list of token objects. Each token object represents a specific character or a group of characters in the pattern string. The lexer goes through each character in the pattern string and identifies what type of character it is and creates a token object accordingly.

Why does the regex engine need a lexer: The regex engine needs a lexer because the pattern string can contain special characters that have specific meanings. For example, in the pattern string 'a\d{1,3}(?:foo|bar)?', the '\d' represents a digit, '{1,3}' represents a quantifier, '(?:foo|bar)' represents a non-capturing group and '?' represents an optional character. The lexer identifies these special characters and creates token objects accordingly so that the parser can create a relationship between them.
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

then we are goping to check that pos < length  so it just mean that we have a while loop so in while loop we just check that we completed parsing or going over this enitre pattern because the length is the length of this pattern string [r\d+\(?=px\)] and position is the current index of the pattern
yes and if the condition is right (yes) then we get the current character by doing the pattern at the current position and then we get the character type
and the character type can be multipe things and there are multiple possibilities like 
forexample '\' if it is a backslash than we are just going to do escape the sequence handler we advance that means we move to the very next token or the very next character and now we check that the very next character is either on of these: (d,D,w,W,s,S) -> all of these are predefined tokens whjich just means that the character that we'r going to have here should be a digit or a word or a whitespace  d stand for Digit, w stands for word and s stands for  white space other than that the another character can be (b,B) and B is a boundary token and after that we can have (1-9) what this is a back reference which are some thing like these '\1' or '\2' that are used to get us the first and the second captured group and then we have (n,t,r) this would mean that we have '\n' , '\t' and 'r' which have basically the same meaning as what we have in python. it can be a new line,a tab or '\r'. after that there can be another token where we just go ahead and create a character token with the escaped literal so all of these can be happen when we have a '\' back-slash




What is boundary token : 

"""

r""" 
Now let's say if there is no backslash instead of that we have an opening paranthesis () that is Group Handler then and after that now we chect that if the next character is a question mark ? The reason we  check it is because this has a special meaning because if the next character is a question mark then we go and get the next character again and cjheck if it is the colon (?: -> till now it will look like this and then it will be a non capturing group
now instead of colon if there is an equal to  = then it will be (?=  that means we are creating a look ahead position then let's say if we don't have is equal to = instead we have ! it will be (?! then it is called Look ahead negative token  now let's say if the next character is a smaller than bracket < then we again try to get the next character to create the LookBehind Position and after < this if the next character is equal to = it is a LookBehind Position  so now we have (?<= and instead of = we have a question mark ? then it will be (?<? then it will be a lookBehind Negative Position token.

Now Instead of backslash and opening paranthesis we have a speacial character these are [ * + ? &{  &}  ,   |   [  ]  ^  $   .    - ]

Other than that we can have a regular character and if it matches none of them 

noe let's say if any of these matches with our pattern string then we just add it to our token list  and we do it until the position is greater than our length of the pattern string then what we are going to do after that is to add an EOF token which means end of file.This tells the RegEx Engine that we have completed the entire pattern and now you are at the  end.
and after that we will return the token list this is how the lexer works.


"""

r""" 
Note: For Lexer our entire motive is toh get the each and every character of the pattern string and convert it into a token object so that we can create a relationship between them in the parser phase.

according to our code we go through each and every character of the pattern string and we check what type of character it is and accordingly we create a token object and add it to our token list and at the end we return the token list.
Below is the example/output of the lexer for the pattern string r"a\d{1,3}(?:foo|bar)?"

Output:
[Token(type=<TokenType.CHAR: 1>, value='a', position=0), Token(type=<TokenType.DIGIT: 18>, value='\\d', position=1), Token(type=<TokenType.LBRACE: 5>, value='{', position=3), Token(type=<TokenType.CHAR: 1>, value='1', position=4), Token(type=<TokenType.COMMA: 7>, value=',', position=5), Token(type=<TokenType.CHAR: 1>, value='3', position=6), Token(type=<TokenType.RBRACE: 6>, value='}', position=7), Token(type=<TokenType.NON_CAPTURING: 31>, value='(?:', position=8), Token(type=<TokenType.CHAR: 1>, value='f', position=11), Token(type=<TokenType.CHAR: 1>, value='o', position=12), Token(type=<TokenType.CHAR: 1>, value='o', position=13), Token(type=<TokenType.PIPE: 8>, value='|', position=14), Token(type=<TokenType.CHAR: 1>, value='b', position=15), Token(type=<TokenType.CHAR: 1>, value='a', position=16), Token(type=<TokenType.CHAR: 1>, value='r', position=17), Token(type=<TokenType.RPAREN: 10>, value=')', position=18), Token(type=<TokenType.QUESTION: 4>, value='?', position=19), Token(type=<TokenType.EOF: 32>, value=None, position=20)]

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
"""
