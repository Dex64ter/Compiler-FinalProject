from JasminGenerator import JasminCodeGenerator, CustomListener
from gen.CompilerListener import CompilerListener
from gen.CompilerParser import CompilerParser
from CustomExceptions import *


class MyListener(CompilerListener):
    symbol_table = {}
    functions_args = {}
    stack_block = []

    def __init__(self, filename):
        self.jasmin = JasminCodeGenerator(filename, self.symbol_table)
        self.label_id = 0

    def __is_inside_function(self):
        return 'function' in self.stack_block

    # Enter a parse tree produced by CompilerParser#prog.
    def enterProg(self, ctx: CompilerParser.ProgContext):
        pass

    # Exit a parse tree produced by CompilerParser#prog.
    def exitProg(self, ctx: CompilerParser.ProgContext):
        self.jasmin.close_file()

    # Enter a parse tree produced by CompilerParser#decFuncao.
    def enterDecFuncao(self, ctx: CompilerParser.DecFuncaoContext):
        self.stack_block.append('function')
        function_id = ctx.ID(0).getText()
        if function_id in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, function_id)

        self.symbol_table[function_id] = MyListener(type=ctx.TYPE(0).getText())

        args = []
        args_names = []
        content = list(zip(ctx.ID()[1:], ctx.TYPE()[1:]))
        for arg_id, arg_type in content:
            if arg_id.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, arg_id.getText())
            self.symbol_table[arg_id.getText()] = MyListener(type=arg_type.getText(), local=True)
            args.append(arg_type.getText())
            args_names.append(arg_id.getText())

        self.functions_args[function_id] = args
        self.jasmin.write_function_declaration(function_id, args_names)

    # Exit a parse tree produced by CompilerParser#decFuncao.
    def exitDecFuncao(self, ctx: CompilerParser.DecFuncaoContext):
        self.jasmin.write_function_end()
        self.stack_block.pop()

    # Enter a parse tree produced by CompilerParser#call.
    def enterCall(self, ctx: CompilerParser.CallContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)

    # Exit a parse tree produced by CompilerParser#call.
    def exitCall(self, ctx: CompilerParser.CallContext):
        function_id = ctx.ID().getText()

        if len(self.functions_args[function_id]) != len(ctx.expr()):
            raise MissingArgument(ctx.start.line, len(self.functions_args[function_id]), len(ctx.expr()))

        for expected, received in list(zip(self.functions_args[function_id], ctx.expr())):
            if expected != received.type:
                raise UnexpectedTypeError(ctx.start.line, expected, received.type)

        ctx.type = self.symbol_table[ctx.ID().getText()].type

    # Enter a parse tree produced by CompilerParser#callFunction.
    def enterCallFunction(self, ctx: CompilerParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by CompilerParser#callFunction.
    def exitCallFunction(self, ctx: CompilerParser.CallFunctionContext):
        ctx.type = self.symbol_table[ctx.ID().getText()].type
        args = []
        types = []
        for exp in ctx.expr():
            args.append(exp.val)
            types.append(exp.type)
        ctx.val = self.jasmin.write_function_call(ctx.ID().getText(), args, types)

    # Enter a parse tree produced by CompilerParser#return.
    def enterReturn(self, ctx: CompilerParser.ReturnContext):
        if not self.__is_inside_function():
            raise ReturnException(ctx.start.line)

    # Exit a parse tree produced by CompilerParser#return.
    def exitReturn(self, ctx: CompilerParser.ReturnContext):
        self.jasmin.write_function_return(ctx.expr().val, ctx.expr().type)

    # Enter a parse tree produced by CompilerParser#comandos.
    def enterComandos(self, ctx: CompilerParser.ComandosContext):
        pass

    # Exit a parse tree produced by CompilerParser#comandos.
    def exitComandos(self, ctx: CompilerParser.ComandosContext):
        pass

    # Enter a parse tree produced by CompilerParser#main.
    def enterMain(self, ctx: CompilerParser.MainContext):
        self.jasmin.write_main_function_declaration()

    # Exit a parse tree produced by CompilerParser#main.
    def exitMain(self, ctx: CompilerParser.MainContext):
        self.jasmin.write_main_function_end()

    # Exit a parse tree produced by CompilerParser#decVar.
    def exitDecVar(self, ctx: CompilerParser.DecVarContext):
        token = ctx.ID()
        if token.getText() in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, token.getText())
        self.symbol_table[token.getText()] = MyListener(address=0, type=ctx.TYPE().getText(), local=True)
        self.jasmin.create_local(token.getText(), ctx.TYPE().getText())

    # Exit a parse tree produced by CompilerParser#funcprint.
    def exitFuncprint(self, ctx: CompilerParser.FuncprintContext):
        type_val = []
        for expr in ctx.expr():
            type_val.append((expr.type, expr.val))
        self.jasmin.print(type_val)

    # Exit a parse tree produced by CompilerParser#funcinput.
    def exitFuncinput(self, ctx: CompilerParser.FuncinputContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)

        self.jasmin.write_inputfunction_code(ctx_id)

    # Enter a parse tree produced by CompilerParser#condicional.
    def enterCondicional(self, ctx: CompilerParser.CondicionalContext):
        ctx.expr().inh_type = 'if'

    # Exit a parse tree produced by CompilerParser#condicional.
    def exitCondicional(self, ctx: CompilerParser.CondicionalContext):
        if ctx.expr().type != 'boolean':
            raise UnexpectedTypeError(ctx.start.line, 'boolean', ctx.expr().type)
        self.jasmin.write_labelname('if_' + str(ctx.expr().end_label))

    # Enter a parse tree produced by CompilerParser#cmdWhile.
    def enterCmdWhile(self, ctx: CompilerParser.CmdWhileContext):
        ctx.expr().inh_type = 'while'
        ctx.expr().inh = self.jasmin.write_dowhileenter_code(len(self.stack_block))
        self.stack_block.append('loop')

    # Exit a parse tree produced by CompilerParser#cmdWhile.
    def exitCmdWhile(self, ctx: CompilerParser.CmdWhileContext):
        if ctx.expr().type != 'boolean':
            raise UnexpectedTypeError(ctx.start.line, 'boolean', ctx.expr().type)
        self.stack_block.pop()
        self.jasmin.write_dowhileexit_code(len(self.stack_block))

    # Exit a parse tree produced by CompilerParser#opMath.
    def exitOpMath(self, ctx: CompilerParser.OpMathContext):
        variable_name = ctx.VARNAME().getText()
        operator = ctx.op.getText()

        if ctx.expressaoAritmetica():
            arith_expr = ctx.expressaoAritmetica()
            result = self.evaluate_arithmetic_expression(arith_expr)
        elif ctx.expressaoBooleana():
            bool_expr = ctx.expressaoBooleana()
            result = self.evaluate_boolean_expression(bool_expr)

    # Exit a parse tree produced by CompilerParser#expressaoAritmetica.
    def exitExpressaoAritmetica(self, ctx: CompilerParser.ExpressaoAritmeticaContext):
        pass

    # Enter a parse tree produced by CompilerParser#termo.
    def enterTermo(self, ctx: CompilerParser.TermoContext):
        pass

    # Exit a parse tree produced by CompilerParser#termo.
    def exitTermo(self, ctx: CompilerParser.TermoContext):
        pass

    # Enter a parse tree produced by CompilerParser#fator.
    def enterFator(self, ctx: CompilerParser.FatorContext):
        pass

    # Exit a parse tree produced by CompilerParser#fator.
    def exitFator(self, ctx: CompilerParser.FatorContext):
        ctx.type = ctx.factor().type
        ctx.val = ctx.factor().val

    # Enter a parse tree produced by CompilerParser#expressaoBooleana.
    def enterExpressaoBooleana(self, ctx: CompilerParser.ExpressaoBooleanaContext):
        pass

    # Exit a parse tree produced by CompilerParser#expressaoBooleana.
    def exitExpressaoBooleana(self, ctx: CompilerParser.ExpressaoBooleanaContext):
        pass

    # Enter a parse tree produced by CompilerParser#condicao.
    def enterCondicao(self, ctx: CompilerParser.CondicaoContext):
        pass

    # Exit a parse tree produced by CompilerParser#condicao.
    def exitCondicao(self, ctx: CompilerParser.CondicaoContext):
        pass

    # Enter a parse tree produced by CompilerParser#expressaoRelacional.
    def enterExpressaoRelacional(self, ctx: CompilerParser.ExpressaoRelacionalContext):
        pass

    # Exit a parse tree produced by CompilerParser#expressaoRelacional.
    def exitExpressaoRelacional(self, ctx: CompilerParser.ExpressaoRelacionalContext):
        pass

    # Enter a parse tree produced by CompilerParser#operadorRelacional.
    def enterOperadorRelacional(self, ctx: CompilerParser.OperadorRelacionalContext):
        pass

    # Exit a parse tree produced by CompilerParser#operadorRelacional.
    def exitOperadorRelacional(self, ctx: CompilerParser.OperadorRelacionalContext):
        pass

    # Exit a parse tree produced by CompilerParser#valorBool.
    def exitValorBool(self, ctx: CompilerParser.ValorBoolContext):
        ctx.type = 'boolean'
        ctx.val = self.jasmin.write_store_code(0 if ctx.getText() == 'False' else 1, ctx.type)
