from ..TextProcessor.Token import tokenizer
import ply.yacc as yacc
import ply.lex as lex


class Node:
    def __init__(self):
        self.documents = list()

    def get_documents(self, files):
        pass


class AND(Node):
    def __init__(self, left, right):
        super(Node, self).__init__()
        self.left = left
        self.right = right

    def get_documents(self, files):
        return self.left.get_documents(files) & self.right.get_documents(files)


class OR(Node):
    def __init__(self, left, right):
        super(Node, self).__init__()
        self.left = left
        self.right = right

    def get_documents(self, files):
        return self.left.get_documents(files) | self.right.get_documents(files)


class NOT(Node):
    def __init__(self, term):
        super(Node, self).__init__()
        self.term = term

    def get_documents(self, files):
        return set(files) - self.term.get_documents(files)


class TOKEN(Node):
    def __init__(self, token):
        super(Node, self).__init__()
        self.token = token

    def get_documents(self, files):
        docs = set()
        for file in files:
            if self.token in file.tokens:
                docs.add(file)
        return docs


class Lexer:

    def __init__(self):
        self.lexer = lex.lex(module=self)

    @property
    def tokens(self):
        return ['AND', 'OR', 'NOT', 'LP', 'RP', 'TOKEN']

    t_LP = r'\('
    t_RP = r'\)'

    def t_AND(self, t):
        r'AND'
        t.type = 'AND'
        return t

    def t_OR(self, t):
        r'OR'
        t.type = 'OR'
        return t

    def t_NOT(self, t):
        r'NOT'
        t.type = 'NOT'
        return t

    def t_TOKEN(self, t):
        r'[a-zA-Z_0-9]+'
        try:
            t.value = tokenizer(t.value)[0]
        except:
            pass
        t.type = 'TOKEN'
        return t

    def t_error(self, t):
        pass

    t_ignore = ' \t\r\f'


class Parser:

    def __init__(self):
        self.lexer = Lexer()
        self.tokens = self.lexer.tokens
        self.parser = None

    def run(self, query):
        self.parser = yacc.yacc(module=self)
        ast = self.parser.parse(input=query, lexer=self.lexer.lexer)
        return ast

    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('right', 'NOT'),
    )

    def p_expr_or(self, parse):
        '''expr : expr OR expr'''
        parse[0] = OR(parse[1], parse[3])

    def p_expr_and(self, parse):
        '''expr : expr AND expr'''
        parse[0] = AND(parse[1], parse[3])

    def p_expr_not(self, parse):
        '''expr : NOT expr'''
        parse[0] = NOT(parse[2])

    def p_expr_brace(self, parse):
        '''expr : LP expr RP'''
        parse[0] = parse[2]

    def p_expr_token(self, parse):
        '''expr : TOKEN'''
        parse[0] = TOKEN(parse[1])

    def p_error(self, parser):
        pass


class BooleanModel:

    def __init__(self, files):
        self.files = files
        self.get_vocabulary()
        self.compute_vectors()

    def get_vocabulary(self):
        self.vocabulary = set()
        for file in self.files:
            self.vocabulary.update(file.tokens)
        self.vocabulary = list(self.vocabulary)

    def compute_vectors(self):
        self.file_vectors = list()
        for file in self.files:
            v = [0 for _ in self.vocabulary]
            for i in range(len(v)):
                v[i] = 1 if self.vocabulary[i] in file.tokens else 0
            self.file_vectors.append(v)

    def query_parser(self, query):
        q_parser = Parser()
        tree = q_parser.run(query)
        return tree

    def similarity(self, query, k):
        q = self.query_parser(query)

        docs = q.get_documents(self.files)

        ret = list()
        for file in docs:
            ret.append((1.0, file.name))

        return ret, []
