"""
Regex Engine:
What is regEx :RegEx stands for Regular Expression

This is the Code for Building the RegEx engine from the Scratch
This one can handle the core features like character classes [a-zA-Z0-9],
Quantifiers -> * + ? {n,m} , Alternation -> |, (?:...) -> Non Capturing Groups and Capturing groups (?=:...),

"""

"Regex Enginne can be implemented in multiple ways: 1.Thompson's NFA 2.DFA 3.Recursive Descent "

""" 
Regex Uses Tree and Backtracking
"""


""" 
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


""" 
Lexer

What 
"""

print("a\d{1,3}(?:foo|bar)?")
""" 
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
bar  ->  literal cvhracter run 
)  -> end of the group 
?  -> this question matrks denotes that the either 0(zero)  or  1(one) should be there of this regex


Now let's focus on the  '\d' part as some times we can also have some thing like these:
'\' '\d'  '\\'  '\D'  '\B'  ->  all of this is known through a lexer/tokenizer 
"""


""" 
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
