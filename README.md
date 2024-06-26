# Assignments for Principle of Programming Language Course (HK232)
_🗒️ All assignments are strictly correlated. In other words, you can not implement the present project without finishing all the previous ones._

## Assignment 1: Lexer/Parser
* Lexer (or Tokenizer): Implement a lexer to tokenize the input source code into a sequence of tokens. Tokens are the smallest units of meaning in a programming language, such as keywords, identifiers, operators, and literals.
* Parser: Develop a parser to analyze the sequence of tokens generated by the lexer and build a syntactic structure, typically represented as an Abstract Syntax Tree (AST). The parser checks whether the input adheres to the language's grammar rules.
* This assignment is only matter of getting used to with ANTLR and codebase, so I was able to get 100/100 for both lexer and parser.

## Assignment 2: AST Generation
* Create a data structure to represent the hierarchical structure of the source code. The AST captures the syntactic relationships among different elements in the code. The goal is to have a structured representation that reflects the program's logic.
* This is the easiest assignment in all three assignments. The instructor also taught you how to do this assignment in the easier way. I get 100/100 for this assignment.

## Assignment 3: Static Check
* Perform static analysis on the AST to check for potential errors or violations of language rules without executing the code. This may include type checking, scope analysis, and other static checks to ensure the code's correctness before runtime.
* This assignment is tricky and complex, particularly on how you can store and call the variables in its scope. Thanks to our instructor using not tricky testcases for marking, I painstakingly got 97/100.
