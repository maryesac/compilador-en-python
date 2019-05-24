from Parser import Parser


parser = Parser()


texto = """
    if (){
        if(){
            if(){
            if(){
            }
            if(){
            }
            if(){
            }
            }
        }
    }

"""

print( parser.compile(texto) )