from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl

from JasminGenerator import *
from gen.CompilerParser import *
from gen.CompilerListener import *
from CustomExceptions import *


class MyListener(CompilerListener):
    symbol_table = {}
    functions_args = {}
    stack_block = []

    def __init__(self, filename):
        self.label_id = 0
        self.argument_info = {}  # Store argument names and types for each function
        self.jasmin = JasminCodeGenerator(filename, self.symbol_table)
        self.label_id = 0

    def __is_numeric(self, type):
        return (type == 'real') or (type == 'int') or (type == 'integer')

    def flag(self, ctx_print):
        declaration = ctx_print.getText()
        print(f"{declaration}")

    def __is_inside_function(self):
        return 'function' in self.stack_block

    def enterProg(self, ctx: CompilerParser.ProgContext):
        print('Enter Prog', self.flag(ctx))

    def exitProg(self, ctx: CompilerParser.ProgContext):
        pass
        print('Exit Prog', self.flag(ctx))

    def enterDecFuncao(self, ctx: CompilerParser.DecFuncaoContext):
        print('Enter DecFunc', self.flag(ctx))
        self.stack_block.append('function')
        func_name = ctx.VARNAME().getText()
        print(ctx.VARNAME().getText(), "\n", ctx.VARTYPE().getText())
        if func_name in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, func_name)
        func_type = ctx.VARTYPE().getText()

        self.symbol_table[func_name] = CustomListener(type=f"{func_type}")

        args = []
        args_names = []
        varnames = []
        vartypes = []

        # Iterate through the children of ctx and filter for VARNAME and VARTYPE tokens
        for child in ctx.children:
            if isinstance(child, TerminalNodeImpl):
                if child.getSymbol().type == CompilerParser.VARNAME:
                    varnames.append(child.getText())
                elif child.getSymbol().type == CompilerParser.VARTYPE:
                    vartypes.append(child.getText())

        # Zip varnames and vartypes together
        content = list(zip(varnames[1:], vartypes[1:]))
        print(content)
        for arg_nm, arg_type in content:
            if arg_nm.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, arg_nm.getText())
            self.symbol_table[arg_nm.getText()] = CustomListener(
                type=arg_type.getText(), local=True)
            args.append(arg_type.getText())
            args_names.append(arg_nm.getText())
        self.functions_args[func_name] = args
        self.jasmin.write_function_declaration(func_name, args_names)

    def exitDecFuncao(self, ctx: CompilerParser.DecFuncaoContext):
        print('Exit DecFunc', self.flag(ctx))
        self.jasmin.write_function_end()
        self.stack_block.pop()

    def enterCallFunction(self, ctx: CompilerParser.CallFunctionContext):
        print('Enter CallFunc', self.flag(ctx))
        ctx_name = ctx.VARNAME().getText()
        if ctx_name not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_name)

    def exitCallFunction(self, ctx: CompilerParser.CallFunctionContext):
        print('Exit CallFunc', self.flag(ctx))
        ctx_name = ctx.VARNAME().getText()
        argument_names = self.argument_info.get(ctx_name, {}).get("names", [])
        argument_types = self.argument_info.get(ctx_name, {}).get("types", [])

        # Check if the number of arguments in the call matches the function's expected number of arguments
        if len(argument_names) != len(ctx.valsCallFunc().expressaoAritmetica()):
            raise ArgumentMismatchError(ctx.start.line, len(argument_names),
                                        len(ctx.valsCallFunc().expressaoAritmetica()))

        for expected, received in list(zip(argument_names, ctx.valsCallFunc().expressaoAritmetica())):
            if expected != received.type:
                raise UnexpectedTypeError(ctx.start.line, expected, received.type)

        ctx.type = self.symbol_table[ctx_name]
        ctx.val = self.jasmin.write_function_call(ctx_name, argument_names, argument_types)

    def enterValsCallFunc(self, ctx: CompilerParser.ValsCallFuncContext):
        print('Enter ValsCallFunc', self.flag(ctx))
        self.argument_expressions = []

    def exitValsCallFunc(self, ctx: CompilerParser.ValsCallFuncContext):
        print('Exit ValsCallFunc', self.flag(ctx))
        # Extract argument expressions and generate code to evaluate them
        for arg_expr in ctx.expressaoAritmetica():
            self.argument_expressions.append(arg_expr)

    def enterReturn(self, ctx: CompilerParser.ReturnContext):
        print('Enter Return', self.flag(ctx))
        if not self.__is_inside_function():
            raise ReturnException(ctx.start.line)

    def exitReturn(self, ctx: CompilerParser.ReturnContext):
        print('Exit Return', self.flag(ctx))
        if ctx.opMathR().isBool:
            self.jasmin.write_function_return(ctx.opMathR().val, ctx.opMathR().type)
        else:
            self.jasmin.write_function_return(ctx.opMathR().val, ctx.opMathR().type)

    def enterComandos(self, ctx: CompilerParser.ComandosContext):
        print('Enter Comandos', self.flag(ctx))

    def exitComandos(self, ctx: CompilerParser.ComandosContext):
        print('Exit Comandos', self.flag(ctx))

    def enterMain(self, ctx: CompilerParser.MainContext):
        print('Enter Main', self.flag(ctx))
        self.jasmin.write_main_function_declaration()

    def exitMain(self, ctx: CompilerParser.MainContext):
        print('Exit Main', self.flag(ctx))
        self.jasmin.write_main_function_end()

    def enterDecVar(self, ctx: CompilerParser.DecVarContext):
        print('Enter DecVar', self.flag(ctx))
        if not self.__is_inside_function():
            raise VariableDeclarationError(ctx.start.line, ctx.varlist().VARNAME())

    def exitDecVar(self, ctx: CompilerParser.DecVarContext):
        print('Exit DecVar', self.flag(ctx))

    def enterVarlist(self, ctx: CompilerParser.VarlistContext):
        print('Enter Varlist', self.flag(ctx))

    def exitVarlist(self, ctx: CompilerParser.VarlistContext):
        print('Exit Varlist', self.flag(ctx))
        ctx_name = ctx.VARNAME().getText()
        ctx_type = ctx.VARTYPE().getText()
        if ctx_name in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, ctx_name)
        self.symbol_table[ctx_name] = CustomListener(
            address=0, type=ctx_type, local=True)
        self.jasmin.create_local(ctx_name, ctx_type)

    def enterConsts(self, ctx: CompilerParser.ConstsContext):
        print('Enter Consts', self.flag(ctx))

    def exitConsts(self, ctx: CompilerParser.ConstsContext):
        print('Exit Consts', self.flag(ctx))

    def enterFuncprint(self, ctx: CompilerParser.FuncprintContext):
        print('Enter Funcprint', self.flag(ctx))

    def exitFuncprint(self, ctx: CompilerParser.FuncprintContext):
        print('Exit Funcprint', self.flag(ctx))
        val_type = []
        for expr in ctx.expressaoAritmetica():
            val_type.append((expr.type_, expr.val))
        self.jasmin.print(val_type)

    def enterFuncinput(self, ctx: CompilerParser.FuncinputContext):
        print('Enter Funcinput', self.flag(ctx))

    def exitFuncinput(self, ctx: CompilerParser.FuncinputContext):
        print('Exit Funcinput', self.flag(ctx))
        ctx_name = ctx.VARNAME().getText()
        if ctx_name not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_name)
        self.jasmin.write_inputfunction_code(ctx_name)

    def enterCondicional(self, ctx: CompilerParser.CondicionalContext):
        print('Enter Condicional (IF)', self.flag(ctx))
        ctx.expressaoBooleana().inh_type = 'if'

    def exitCondicional(self, ctx: CompilerParser.CondicionalContext):
        print('Exit Condicional (IF)', self.flag(ctx))
        if ctx.expressaoBooleana().type != 'bool':
            raise UnexpectedTypeError(
                ctx.start.line, 'bool', ctx.expressaoBooleana().type)
        self.jasmin.write_labelname('if_' + str(ctx.expressaoBooleana().end_label))

    def enterCondElse(self, ctx: CompilerParser.CondElseContext):
        print('Enter CondElse (ELSE)', self.flag(ctx))

    def exitCondElse(self, ctx: CompilerParser.CondElseContext):
        print('Exit CondElse (ELSE)', self.flag(ctx))

    def enterCmdWhile(self, ctx: CompilerParser.CmdWhileContext):
        print('Enter CmdWhile', self.flag(ctx))
        ctx.expressaoBooleana().inh_type = 'while'
        ctx.expressaoBooleana().inh = self.jasmin.write_dowhileenter_code(len(self.stack_block))
        self.stack_block.append('loop')

    def exitCmdWhile(self, ctx: CompilerParser.CmdWhileContext):
        print('Exit CmdWhile', self.flag(ctx))
        if ctx.expressaoBooleana().type != 'bool':
            raise UnexpectedTypeError(
                ctx.start.line, 'bool', ctx.expressaoBooleana().type)
        self.stack_block.pop()
        self.jasmin.write_dowhileexit_code(len(self.stack_block))

    def exitVar_name(self, ctx: CompilerParser.Var_nameContext):
        ctx_name = ctx.VARNAME().getText()

        if ctx_name not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_name)
        ctx.type_ = self.symbol_table[ctx_name].type_
        ctx.val = self.jasmin.write_variable_load(ctx_name)

    def exitFloat_value(self, ctx: CompilerParser.Float_valueContext):
        print(f'Float Value: {ctx.getText()}')
        ctx.type_ = 'float'
        ctx.val = self.jasmin.write_store_code(ctx.getText(), ctx.type_)

    def exitInt_value(self, ctx: CompilerParser.Int_valueContext):
        print(f'Int_value: {ctx.getText()}')
        ctx.type_ = 'int'
        ctx.val = self.jasmin.write_store_code(ctx.getText(), ctx.type_)

    def exitStr_val(self, ctx: CompilerParser.Str_valContext):
        print(f'Str_val: {ctx.getText()}')
        ctx.type_ = 'string'
        ctx.val = self.jasmin.write_store_code(ctx.getText(), ctx.type_)

    def exitFunc_call(self, ctx: CompilerParser.Func_callContext):
        target = ctx.callFunction()
        ctx.type_ = target.type_
        ctx.val = target.val

    def exitExpr(self, ctx: CompilerParser.ExprContext):
        ctx.type_ = ctx.expr().type_
        ctx.val = ctx.expr().val

    def exitE_termo(self, ctx:CompilerParser.E_termoContext):
        ctx.type_ = ctx.expr().type_
        ctx.val = ctx.expr().val

    def exitSum_minus(self, ctx:CompilerParser.Sum_minusContext):
        if not self.__is_numeric(ctx.expressaoAritmetica().type_):
            raise ExpressionTypeError(
                ctx.start.line, ctx.op.text, ctx.expressaoAritmetica().type_
            )
        elif not self.__is_numeric(ctx.termo().type_):
            raise ExpressionTypeError(
                ctx.start.line, ctx.op.text, ctx.expressaoAritmetica().type_
            )
        elif ctx.termo().type_ == 'float' and ctx.expressaoAritmetica().type_ == 'float':
            ctx.type_ = 'float'
            val1, val2 = ctx.expressaoAritmetica().val, ctx.termo().val
        elif ctx.expressaoAritmetica().type_ == 'float':
            ctx.type_ = 'float'
            val1 = ctx.expressaoAritmetica().val
            val2 = self.jasmin.write_integertofloat_code(ctx.termo().val)
        elif ctx.termo().type_ == 'float':
            ctx.type_ = 'float'
            val1 = self.jasmin.write_integertofloat_code(ctx.expressaoAritmetica().val)
            val2 = ctx.termo().val
        else:
            ctx.type_ = 'int'
            val1, val2 = ctx.expressaoAritmetica().val, ctx.termo().val

        if ctx.op.text == '+':
            ctx.val = self.jasmin.write_addoperator_code(ctx.type_, val1, val2)
        else:
            ctx.val = self.jasmin.write_suboperator_code(ctx.type_, val1, val2)


    def exitE_factor(self, ctx:CompilerParser.E_factorContext):
        ctx.type_ = ctx.expr().type_
        ctx.val = ctx.expr().val

    def exitTime_div(self, ctx:CompilerParser.Time_divContext):
        if not self.__is_numeric(ctx.termo().type_):
            raise ExpressionTypeError(
                ctx.start.line, ctx.op.text, ctx.termo().type_
            )
        elif not self.__is_numeric(ctx.fator().type_):
            raise ExpressionTypeError(
                ctx.start.line, ctx.op.text, ctx.fator().type_
            )
        elif ctx.termo().type_ == 'float' and ctx.fator().type_ == 'float':
            ctx.type_ = 'float'
            val1, val2 = ctx.termo().val, ctx.fator().val
        elif ctx.termo().type_ == 'float':
            ctx.type_ = 'float'
            val1 = ctx.termo().val
            val2 = self.jasmin.write_integertofloat_code(ctx.fator().val)
        elif ctx.fator().type_ == 'float':
            ctx.type_ = 'float'
            val1 = self.jasmin.write_integertofloat_code(ctx.termo().val)
            val2 = ctx.fator().val
        else:
            ctx.type_ = 'int'
            val1, val2 = ctx.termo().val, ctx.fator().val

        if ctx.op.text == '*':
            ctx.val = self.jasmin.write_multiplication_code(
                ctx.type_, val1, val2)
        else:
            ctx.val = self.jasmin.write_division_code(ctx.type_, val1, val2)

    def enterOpMath(self, ctx: CompilerParser.OpMathContext):
        print('Enter OpMath', self.flag(ctx))
        var_name = ctx.VARNAME().getText()
        operator = ctx.getChild(1).getText()  # Assuming the operator is the second child node
        expression = ctx.getChild(2)  # Get the expression context

        # Access the return values specified in the grammar
        type = ctx.type_
        inh_type = ctx.inh_type
        isBool = ctx.isBool
        val = ctx.val

    def exitOpMath(self, ctx: CompilerParser.OpMathContext):
        print('Exit OpMath', self.flag(ctx))

    def enterOpMathR(self, ctx: CompilerParser.OpMathRContext):
        print('Enter OpMathR', self.flag(ctx))
        expression = ctx.getChild(0)  # Get the expression context (can be either Aritmetica or Booleana)

        # Access the return values specified in the grammar
        type = ctx.type_
        inh_type = ctx.inh_type
        isBool = ctx.isBool
        val = ctx.val

    def exitOpMathR(self, ctx: CompilerParser.OpMathRContext):
        print('Exit OpMathR', self.flag(ctx))

    def enterExpressaoBooleana(self, ctx: CompilerParser.ExpressaoBooleanaContext):
        print('Enter ExpressaoBooleana', self.flag(ctx))

    def exitExpressaoBooleana(self, ctx: CompilerParser.ExpressaoBooleanaContext):
        print('Exit ExpressaoBooleana', self.flag(ctx))

    def exitExpressaoRelacional(self, ctx:CompilerParser.ExpressaoRelacionalContext):
        ctx_t1 = ctx.expressaoAritmetica()
        ctx_t2 = ctx.getChild(2)

        if ctx_t1.type_ != ctx_t2.type_:
            raise ExpressionTypeError(
                ctx.start.line, ctx.op.text, ctx_t1.type_, ctx_t2.type_
            )
        ctx.type_ = 'bool'
        ctx.val = self.jasmin.write_equaloperator_code(ctx_t1.type_, ctx_t2.val,
                                                       ctx_t2.type_, ctx_t2.val,
                                                       self.label_id, ctx.op.text)

    def exitValorBool(self, ctx:CompilerParser.ValorBoolContext):
        ctx.type_ = 'bool'
        ctx.val = self.jasmin.write_store_code(
            0 if ctx.getText() == 'False' else 1, ctx.type_)

