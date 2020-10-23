# Interpreter

from abc import ABC, abstractmethod

class Interpreter(Exception):
    pass

class Context:
    def __init__(self, text):
        self.__tokens = text.split()
        self.__idx = 0
    
    @property
    def tokens(self):
        return self.__tokens
    
    @property
    def idx(self):
        return self.__idx
    
    @idx.setter
    def idx(self, idx):
        self.__idx = idx
    
    def delete_token(self, start, end):
        del self.__tokens[start: end]

class Node(ABC):
    @abstractmethod
    def parse(self, context: Context):
        pass

class ProgramNode(Node):
    def parse(self, context: Context):
        try:
            # print(context.tokens)
            while context.idx < len(context.tokens):
                idx = context.idx
                current_token = context.tokens[idx]
                # print(f'idx: {idx}, current_token: {current_token}')
                
                if current_token == '+':
                    node = PlusNode()
                elif current_token == '-':
                    node = MinusNode()
                elif current_token == '*':
                    node = MultiplyNode()
                elif current_token == '/':
                    node = DivideNode()
                else:
                    context.idx += 1
                    continue
                answer = node.parse(context)
                context.delete_token(idx - 2, idx + 1)
                context.tokens.insert(idx - 2, answer)
                context.idx = idx - 1
                # print(context.tokens)

            if len(context.tokens) == 1:
                return context.tokens[0]
            else:
                raise InterpreterException('文字式が誤っています')
        except:
            raise InterpreterException('文字式が誤っています')


class PlusNode(Node):
    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx - 2]) + int(context.tokens[idx - 1])

class MinusNode(Node):
    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx - 2]) - int(context.tokens[idx - 1])

class MultiplyNode(Node):
    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx - 2]) * int(context.tokens[idx - 1])

class DivideNode(Node):
    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx - 2]) / int(context.tokens[idx - 1])

context = Context('2 4 * 3 2 * + 2 /')
node = ProgramNode()
print(node.parse(context))
