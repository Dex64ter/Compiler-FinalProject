class CustomListener:
    def __init__(self, address: int = None, type=None, function: bool = False, local: bool = False):
        self.type = type
        self.address = address
        self.function = function
        self.local = local


def translate_type_name(vartype):
    descriptor = {
        'None': 'V',
        'bool': 'Z',
        'int': 'I',
        'integer': 'I',
        'float': 'F',
        'str': 'Ljava/lang/String;',
    }
    print(vartype)
    return descriptor[vartype]


class JasminCodeGenerator:
    MAX_LOCAL_NUMBER = 100

    def __init__(self, name, symbol_table):
        self.name = name
        self.initialize_file(f"{name}.j", symbol_table)

    def initialize_file(self, filename, symbol_table):
        self.file = open(filename, 'w+')
        self.write_jasmin_header()
        self.symbol_table = symbol_table
        self.top_index, self.label_count = 0, 0

    def close_file(self):
        self.file.close()

    # remove tabs de strings antes de escrever a linha
    def __write(self, string):
        for s in string.split('\n'):
            if s.strip():
                self.file.write(s.strip() + "\n")

    def create_local(self, var_name, var_type):
        self.write_variable_store(var_name, 0)

    def write_jasmin_header(self):
        self.__write(
            """
            .class public {}
            .super java/lang/Object
            """.format(self.name)
        )

    def write_main_function_declaration(self):
        self.__write(
            """
            .method public static main([Ljava/lang/String;)V
            .limit stack 10
            .limit locals {}
            """.format(self.MAX_LOCAL_NUMBER)
        )

    def write_main_function_end(self):
        self.__write(
            """
            return
            .end method
            """
        )

    def write_function_declaration(self, name, parameters):
        param = ''
        for p in parameters:
            param += translate_type_name(self.symbol_table[p].type)
        self.__write(
            """
            .method public static {}({}){}
            .limit stack 5
            .limit locals {}
            """.format(name, param, translate_type_name(self.symbol_table[name].type), self.MAX_LOCAL_NUMBER)
        )
        for idx, p in enumerate(parameters):
            self.symbol_table[p].address = idx
            self.symbol_table[p].local = True

    def write_function_end(self):
        self.__write(
            """
            .end method
            """
        )

    def write_function_call(self, func_name, params, types):
        func_type = self.symbol_table[func_name].type
        args = ''
        for p, t in zip(params, types):
            self.write_loadimmediate_code(p, t)
            args += translate_type_name(t)
        self.__write(
            """
            invokestatic {}.{}({}){}
            """.format(self.name, func_name, args, translate_type_name(func_type))
        )
        return self.write_value_store(func_type)

    def write_function_return(self, val, type):
        return_type = translate_type_name(type)
        if return_type == 'V':
            self.__write(
                """
                return
                """
            )
            return
        self.write_loadimmediate_code(val, type)
        if return_type == 'I':
            self.__write(
                """
                ireturn
                """
            )
        elif return_type == 'F':
            self.__write(
                """
                freturn
                """
            )
        elif return_type == 'V':
            self.__write(
                """
                return
                """
            )
        elif return_type == 'Ljava/lang/String;':
            self.__write(
                """
                areturn
                """
            )

    def print(self, type_val):
        for type, val in type_val:
            self.__write(
                """
                getstatic java/lang/System/out Ljava/io/PrintStream;
                """
            )
            self.write_loadimmediate_code(val, type)
            self.__write(
                """
                invokevirtual java/io/PrintStream/print({})V
                """.format(translate_type_name(type))
            )


    def write_multiplication_code(self, type, add1, add2):
        self.write_loadimmediate_code(add1, type)
        self.write_loadimmediate_code(add2, type)
        if type == 'int' or type == 'integer':
            self.__write(
                """
                imul
                """
            )
        elif type == 'float':
            self.__write(
                """
                fmul
                """
            )
        return self.write_value_store(type)

    def write_division_code(self, type, add1, add2):
        self.write_loadimmediate_code(add1, type)
        self.write_loadimmediate_code(add2, type)
        if type == 'int':
            self.__write(
                """
                idiv
                """
            )
        elif type == 'float':
            self.__write(
                """
                fdiv
                """
            )
        return self.write_value_store(type)

    def write_notoperator_code(self, val):
        self.write_loadimmediate_code(val, 'boolean')
        self.__write(
            """
            ldc 1
            ixor
            """
        )
        return self.write_value_store('boolean')

    def write_equaloperator_code(self, type, val1, val2, label_id, op):
        cmp = {
            '!=': 'ne',
            '==': 'eq',
            '<=': 'le',
            '>=': 'ge',
            '>': 'gt',
            '<': 'lt',
        }
        self.write_loadimmediate_code(val1, type)
        self.write_loadimmediate_code(val2, type)
        if type in ['int', 'boolean']:
            self.__write(
                """
                if_icmp{} true{}
                """.format(cmp[op], label_id)
            )
        elif type == 'float':
            self.__write(
                """
                if{} true{}
                """.format(cmp[op], label_id)
            )
        else:
            self.__write(
                """
                if_acmp{} true{}
                """.format(cmp[op], label_id)
            )
        self.__write(
            """
            ldc 0
            goto cmp_end{}
            true{}:
            ldc 1
            cmp_end{}:
            """.format(label_id, label_id, label_id, label_id)
        )
        return self.write_value_store('boolean')

    def write_value_store(self, type):
        if type == 'string':
            self.__write(
                """
                astore {}
                """.format(self.top_index)
            )
        elif type == 'int' or type == 'boolean' or type == 'integer':
            self.__write(
                """
                istore {}
                """.format(self.top_index)
            )
        elif type == 'float':
            self.__write(
                """
                fstore {}
                """.format(self.top_index)
            )
        self.top_index += 1
        return self.top_index - 1

    def write_variable_load(self, var):
        print(var, self.symbol_table)
        var_data = self.symbol_table[var]
        if var_data.local:  # local var
            if var_data.type == 'int' or var_data.type == 'boolean':
                self.__write(
                    """
                     iload {}
                     """.format(var_data.address)
                )
            elif var_data.type == 'float':
                self.__write(
                    """
                    fload {}
                    """.format(var_data.address)
                )
            elif var_data.type == 'string':
                self.__write(
                    """
                    aload {}
                    """.format(var_data.address)
                )
        return self.write_value_store(var_data.type)

    def write_variable_store(self, var, address):
        var_data = self.symbol_table[var]
        if var_data.local:  # local var
            if var_data.type == 'int' or var_data.type == 'boolean':
                self.__write(
                    """
                    iload {}
                    istore {}
                    """.format(var_data.address, address)
                )
            elif var_data.type == 'float':
                self.__write(
                    """
                    fload {}
                    fstore {}
                    """.format(var_data.address, address)
                )
            # TODO: tratar string
        else:  # global var
            self.write_loadimmediate_code(address, self.symbol_table[var].type)
            self.__write(
                """
                putstatic {}/{} {}
                """.format(self.name, var, translate_type_name(self.symbol_table[var].type))
            )

    def write_inputfunction_code(self, name):
        t = self.symbol_table[name].type
        self.__write(
            """
            new java/util/Scanner
            dup
            getstatic java/lang/System/in Ljava/io/InputStream;
            invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
            """
        )
        if t == 'string':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;
                """
            )
        elif t == 'int' or t == 'integer':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextInt()I
                """.format(translate_type_name(self.symbol_table[name].type))
            )
        elif t == 'float':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextFloat()F
                """.format(translate_type_name(self.symbol_table[name].type))
            )
        elif t == 'boolean':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextBoolean()Z
                """.format(translate_type_name(self.symbol_table[name].type))
            )
        addr = self.write_value_store(self.symbol_table[name].type)
        self.write_variable_store(name, addr)

    def write_addoperator_code(self, type, add1, add2):
        self.write_loadimmediate_code(add1, type)
        self.write_loadimmediate_code(add2, type)
        if type == 'int':
            self.__write(
                """
                iadd
                """
            )
        elif type == 'float':
            self.__write(
                """
                fadd
                """
            )
        elif type == 'string':
            self.__write(
                """
                invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
                """
            )
        return self.write_value_store(type)

    def write_suboperator_code(self, type, add1, add2):
        self.write_loadimmediate_code(add1, type)
        self.write_loadimmediate_code(add2, type)
        if type == 'int':
            self.__write(
                """
                isub
                """
            )
        elif type == 'float':
            self.__write(
                """
                fsub
                """
            )
        return self.write_value_store(type)

    def write_loadimmediate_code(self, val, type):
        if type == 'int' or type == 'integer' or type == 'boolean':
            self.__write(
                """
                iload {}
                """.format(val)
            )
        elif type == 'float':
            self.__write(
                """
                fload {}
                """.format(val)
            )
        elif type == 'string':
            self.__write(
                """
                aload {}
                """.format(val)
            )

    def write_store_code(self, val, type):
        self.__write(
            """
            ldc {}
            """.format(val)
        )
        return self.write_value_store(type)

    def write_integertofloat_code(self, val):
        self.write_loadimmediate_code(val, "int")
        self.__write(
            """
            i2f
            """
        )
        return self.write_value_store("float")

    def write_dowhileenter_code(self, loop_idx):
        self.__write(
            """
            enter_while{}:
            """.format(loop_idx)
        )
        return "iload {}\n" + "ldc 1\nif_icmpne break{}".format(loop_idx)

    def write_dowhileexit_code(self, loop_idx):
        self.__write(
            """
            goto enter_while{}
            break{}:
            """.format(loop_idx, loop_idx)
        )

    def write_loopbreak_code(self, break_point):
        self.__write(
            """
            goto break{}
            """.format(break_point)
        )

    def write_inh(self, line):
        self.__write(line)

    def write_ifenter_code(self, id):
        self.write_loadimmediate_code(id, 'integer')
        self.__write(
            """
            ldc 0
            if_icmpeq if_{}
            """.format(self.label_count)
        )
        self.label_count += 1
        return self.label_count - 1

    def write_labelname(self, label_name):
        self.__write(
            """
            {}:
            """.format(label_name)
        )