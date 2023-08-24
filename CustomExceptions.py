class ExpressionTypeError(Exception):
    def __init__(self, line_number, operation_value, type1_name, type2_name=None):
        super().__init__()


class VariableDeclarationError(Exception):
    def __init__(self, line_number, type2_name=None):
        super().__init__()


class NonDeclaredVariableError(Exception):
    def __init__(self, line_number, identifier_name):
        super().__init__()


class UnexpectedTypeError(Exception):
    def __init__(self, line_number, expected_type, received_type):
        super().__init__()


class BreakException(Exception):
    def __init__(self, line_number):
        super().__init__()


class ReturnException(Exception):
    def __init__(self, line_number):
        super().__init__()


class ArgumentMismatchError(Exception):
    def __init__(self, line, expected_args_num, received_args_num):
        super().__init__()


class UndeclaredFunction(Exception):
    def __init__(self, line_number, identifier_name):
        super().__init__()


class AlreadyDeclaredError(Exception):
    def __init__(self, line_number, identifier_name):
        super().__init__()
