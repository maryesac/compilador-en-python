from lark import Lark


class Parser:
    def __init__(self):
        self.grammar = """
            
            sentence: keyword -> palabra_reservada
            | if_sentence -> sentencia_if 
            | create_var -> crear_variable
            
            if_sentence: keyword OPEN_PARENTHESIS END_PARENTHESIS OPEN_BRACKET (if_sentence)? END_BRACKET (if_sentence)?
            
            
            create_var: DATA_TYPE WORD ( EQUAL_SYMBOL VAR_VALUE )? END_LINE
            keyword: KEYWORD
            data_types: DATA_TYPE          
            
            
            
            KEYWORD: "if"
            DATA_TYPE: "char" | "int" | "boolean"
            END_BRACKET: "}"
            OPEN_BRACKET: "{"
            
            VAR_VALUE: ESCAPED_STRING | SIGNED_NUMBER
            
            END_PARENTHESIS: ")"
            OPEN_PARENTHESIS: "("
            END_LINE: ";"
            EQUAL_SYMBOL: "="
            
            %import common.WS
            %import common.WORD
            %import common.ESCAPED_STRING
            %import common.SIGNED_NUMBER
            %ignore WS
        """
        self.compiler = Lark(self.grammar, start='sentence', ambiguity='explicit')

    def compile(self, text):
        return self.compiler.parse(text)