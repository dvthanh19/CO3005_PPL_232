from Utils import *
# from StaticCheck import *
# from StaticError import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from AST import *
from CodeGenError import *

class ZType:
    def __init__(self, paramType, returnType):
        self.paramType = paramType
        self.returnType = returnType
        
    def __str__(self):
        return 'Foo({},{})'.format(
            ','.join([str(x) for x in self.paramType]),
            str(self.returnType)
        )

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, name, typ, param):
        self.typ = typ
        self.name = name
        self.param = param
        self.line = 0 #! hàng trong buff
    def __str__(self):
        return f"FuncZcode(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},name={self.name},line={self.line})"

class VarZcode(Zcode):
    def __init__(self, name, typ, index, init = False):
        self.typ = typ
        self.name = name
        self.index = index #! vị trí biến trong bộ nhớ
        self.line = 0 #! hàng trong buff
        self.init = init
    def __str__(self):
        return f"VarZcode(type={self.typ},name={self.name},index={self.index},line={self.line},init={self.init})"




class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list() 
        self.jvm = JasminCode()     #! gọi quá

    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is BoolType:      #* kiểu bool
            return "Z"
        elif typeIn is NumberType:  #* kiểu float
            return "F"
        elif typeIn is StringType:  #* kiểu string
            return "Ljava/lang/String;"
        elif typeIn is VoidType:     #* kiểu void
            return "V"
        elif typeIn is ArrayType:   #* kiểu array
            return "[" * len(inType.size)  + self.getJVMType(inType.eleType)
        elif typeIn is Zcode:       #* kiểu Zcode trương trình
            return "LZCodeClass;"
        elif typeIn is ZType:
                return f'({"".join([self.getJVMType(x) for x in inType.paramType])}){self.getJVMType(inType.returnType)}'

        return "Ljava/lang/Object;"

    """_Directives Generation APIs_
    
    """
    #* khởi tạo ban đầu của một class
    def emitPROLOG(self, name, parent):
        #& name: String, Tên class (name = ZCodeClass)
        #& parent: String, Tên class cha hiện tại là mặt định (parent = "")

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/lang/Object" if parent == "" else parent))
        
        return ''.join(result)

    #* ghi vào file .j để thực hiện biên dịch
    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    #* khơi tạo hàm 
    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        #& lexeme: String (tên hàm)
        #& in_: Type (type của hàm FUNCZcode)
        #& isStatic: Boolean (chỉ có contrutor là không static còn lại là phải hết)
        #& frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    #* gọi hàm static
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        #& lexeme: String (tên hàm)
        #& in_: Type (kiểu FUNZCODE)
        #& frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.paramType))
        if not type(typ.returnType) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))
    
    #* gọi class cha invokespecial java/lang/Object/<init>()V
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        #& lexeme: String (bỏ qua luôn vì là java/lang/Object/<init>()V)
        #& in_: Type (bỏ qua luôn)
        #& frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.param))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    #* gọi concat, so sánh
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame, pop = 0):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        if type(typ) not in [VoidType, NumberType, BoolType, ArrayType, NumberType, StringType]:
            list(map(lambda x: frame.pop(), typ.paramType))
        for i in range(0, pop):
            frame.pop()
        
        if type(typ) is VoidType:
            frame.pop()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))
    
    
    #* cuối hàm dùng để xác định limit stack, limit locals
    def emitENDMETHOD(self, frame):
        # frame: Frame
        
        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    #* return 
    def emitRETURN(self, in_, frame):
        #& in_: Type
        #& frame: Frame

        if type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        
        elif type(in_) is NumberType:
            frame.pop()
            return self.jvm.emitFRETURN()
        
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()
        
        elif (type(in_) is StringType) or (type(in_) is ArrayType):
            frame.pop()
            return self.jvm.emitARETURN()

    #* khởi tạo biến toàn cục thành biến static
    def emitATTRIBUTE(self, lexeme, in_, isFinal = False, value = None):
        #& lexeme: String (tên)
        #& in_: Type (kiểu)
        #& isFinal: Boolean (BTL này không sài cho FALSE)
        #& value: String (không sài luôn)

        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal)

    #* lấy giá trị của biến toàn cục
    def emitGETSTATIC(self, lexeme, in_, frame):
        #& lexeme: String (tên biến toàn cục)
        #& in_: Type (kiểu của biến toàn cục)
        #& frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    #* cập nhật giá trị của biến toàn cục
    def emitPUTSTATIC(self, lexeme, in_, frame):
        #& lexeme: String (tên biến toàn cục)
        #& in_: Type (kiểu của biến toàn cục)
        #& frame: Frame

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    #* limit stack _
    def emitLIMITSTACK(self, num):
        # num: Int
        return self.jvm.emitLIMITSTACK(num)
    #* limit locals _
    def emitLIMITLOCAL(self, num):
        # num: Int
        return self.jvm.emitLIMITLOCAL(num)

    #* cập nhật dòng lệnh vào self.buff
    def printout(self, in_):
        # in_: String
        self.buff.append(in_)
    
    #* lấy vị trí hàng vừa khởi tạo lưu vào line trong zcode
    def printIndexNew(self):
        return len(self.buff) - 1
    
    #* chỉnh lại type từ Node -> kiểu type chính thức
    def setType(self, in_):
        if type(in_) is VarZcode: typ = self.getJVMType(in_.typ)
        else: typ = self.getJVMType(in_)
        self.buff[in_.line] = self.buff[in_.line].replace("None", typ)

    #* xóa tất cả
    def clearBuff(self):
        self.buff.clear()
        
    #* cập nhật hàng có NoneType
    def updateType(self, index, type):
        pass
         
    """_Operation Generation APIs_
    
    """
    #* Phép cộng, trừ 2 number (number ở đây là float)
    def emitADDOP(self, lexeme, in_, frame):
        #& lexeme: String (dấu +,-)
        #& in_: Type (numberType)
        #& frame: Frame (TOÁN TỬ LẤY 2 GIÁ TRỊ VÀ TRẢ LẠI 1 GIÁ TRỊ)
        #& ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            return self.jvm.emitFADD()
        else:
            return self.jvm.emitFSUB()

    #* Phép nhân, chia 2 number
    def emitMULOP(self, lexeme, in_, frame):
        #& lexeme: String (dấu *,/)
        #& in_: Type (numberType)
        #& frame: Frame (TOÁN TỬ LẤY 2 GIÁ TRỊ VÀ TRẢ LẠI 1 GIÁ TRỊ)
        #& ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            return self.jvm.emitFMUL()
        else:
            return self.jvm.emitFDIV()

    #* Phép and 2 bool
    def emitANDOP(self, frame):
        #& frame: Frame (TOÁN TỬ LẤY 2 GIÁ TRỊ VÀ TRẢ LẠI 1 GIÁ TRỊ)

        frame.pop()
        return self.jvm.emitIAND()
    
    #* Phép or 2 bool
    def emitOROP(self, frame):
        #& frame: Frame (TOÁN TỬ LẤY 2 GIÁ TRỊ VÀ TRẢ LẠI 1 GIÁ TRỊ)

        frame.pop()
        return self.jvm.emitIOR()

    #* so sánh 2 number trả về true/false
    def emitREOP(self, op, in_, frame):
        #& op: String
        #& in_: Type
        #& frame: Frame
        #& ..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        result.append(self.jvm.emitFCMPL())
        if op == "=":
            result.append(self.jvm.emitIFEQ(labelF))   
            result.append(self.emitPUSHCONST(False, BoolType(), frame))
            frame.pop()
            result.append(self.emitGOTO(labelO, frame))
            result.append(self.emitLABEL(labelF, frame))
            result.append(self.emitPUSHCONST(True, BoolType(), frame))
            result.append(self.emitLABEL(labelO, frame)) 
            return ''.join(result)
        elif op == ">":
            result.append(self.jvm.emitIFLE(labelF))
        elif op == ">=":
            result.append(self.jvm.emitIFLT(labelF))
        elif op == "<":
            result.append(self.jvm.emitIFGE(labelF))
        elif op == "<=":
            result.append(self.jvm.emitIFGT(labelF))
        elif op == "!=":
            result.append(self.jvm.emitIFEQ(labelF))   
        result.append(self.emitPUSHCONST(True, BoolType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST(False, BoolType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)
    
    #* lấy dấu âm
    def emitNEGOP(self, in_, frame):
        #& in_: Type
        #& frame: Frame
        #& ..., value -> ..., result

        return self.jvm.emitFNEG()

    #* hàm not
    def emitNOT(self, in_, frame):
        #& in_: Type
        #& frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST(True, in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST(False, in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    #* CHUYỂN float->int
    def emitF2I(self, frame):
        # frame: Frame
        return '\tf2i\n'
    
    #* chuyển int->float
    def emitI2F(self, frame):
        # frame: Frame
        return self.jvm.emitI2F()
    
    
    def emitMOD(self, frame):
        # frame: Frame
        frame.pop()
        return self.jvm.emitFREM()
    
    
    """_Read/Write Variables APIs_
    """
    #* khởi tạo giá trị mặt định
    def emitPUSHCONST(self, in_, typ, frame):
        #& in_: String (giá trị)
        #& typ: Type (kiểu number/string/bool)
        #& frame: Frame
        frame.push()
        if type(typ) is NumberType:
            f = float(in_)
            rst = "{0:.4f}".format(f)
            if (rst == "0.0") or (rst == "1.0") or (rst == "2.0"):
                return self.jvm.emitFCONST(rst)
            else:
                return self.jvm.emitLDC(rst)    
        elif type(typ) is StringType:
            return self.jvm.emitLDC(in_)
        elif type(typ) is BoolType:
            if in_:
                return self.jvm.emitICONST(1)
            else:
                return self.jvm.emitICONST(0)
        else:
            raise IllegalOperandException(in_)
    
    def emitPUSHICONST(self, in_, frame):
        # in_: Int or Sring
        # frame: Frame

        frame.push()
        if type(in_) is int:
            i = in_
            if (i >= -1) and (i <= 5):
                return self.jvm.emitICONST(i)
            elif (i >= -128) and (i <= 127):
                return self.jvm.emitBIPUSH(i)
            elif (i >= -32768) and (i <= 32767):
                return self.jvm.emitSIPUSH(i)
            
        elif type(in_) is str:
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)
    
    
    
    #* khởi tạo biến cục bộ
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        #& in_: Int (vị trí index)
        #& varName: String (tên)
        #& inType: Type (kiểu)
        #& fromLabel: Int (tầm vực bắt đầu)
        #& toLabel: Int (tầm vực kết thúc)
        #& frame: Frame

        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitWRITEVAR(self, name, inType, index, frame):
        #& name: String
        #& inType: Type
        #& index: Int
        #& frame: Frame
        #& ..., value -> ...

        frame.pop()
        if type(inType) is NumberType:
            return self.jvm.emitFSTORE(index)
        elif type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is StringType:
            return self.jvm.emitASTORE(index)
        elif type(inType) is ArrayType:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)  
        
    #* Đọc biến cục bộ các kiểu (number,bool,string)
    def emitREADVAR(self, name, inType, index, frame):
        #& name: String (tên biến để nén ra lỗi thôi)
        #& inType: Type (NumberType / StringType)
        #& index: Int (vị trí trong frame)
        #& frame: Frame (TRẢ LẠI 1)
        #& ... -> ..., value

        frame.push()
        if name == "this":
            return self.jvm.emitALOAD(index)
        elif type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is NumberType:
            return self.jvm.emitFLOAD(index)
        elif type(inType) is StringType:
            return self.jvm.emitALOAD(index)
        elif type(inType) is ArrayType:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

   #* Đọc mảng
    def emitALOAD(self, in_, frame):
        # in_: Type 
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()
        if type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is NumberType:
            return self.jvm.emitFALOAD()
        elif type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))        
        
    #* lưu mảng
    def emitASTORE(self, in_, frame):
        #& in_: Type
        #& frame: Frame
        #& ..., arrayref, index, value -> ...

        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFASTORE()
        if type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif  type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))


    """_biểu thức điều kiện và vòng lặp
    """
    #*nếu true thì nhảy
    def emitIFTRUE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)
    #* nếu false thì nhảy
    def emitIFFALSE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)
    #* nhãn
    def emitLABEL(self, label, frame):
        # label: Int
        # frame: Frame
        return self.jvm.emitLABEL(label)
    #* nhảy không cần điều kiện
    def emitGOTO(self, label, frame):
        # label: Int
        # frame: Frame
        return self.jvm.emitGOTO(str(label))

    """_new array
    """
    #* taoj ra array 1 chieue
    def emitNEWARRAY(self, in_, frame):
        # frame: Frame
        # in_: Type
        val = ""
        if type(in_) is NumberType:
            val = "float"
        elif type(in_) is BoolType:
            val = "boolean"
        elif type(in_) is StringType:
            return self.emitANEWARRAY(in_, frame)
        return self.jvm.emitNEWARRAY(val)
    
    #* tạo ra array 1 chiều địa chỉ
    def emitANEWARRAY(self, in_, frame):
        # frame: Frame
        # in_: Type
        val = ""
        if type(in_) is NumberType:
            val = "float"
        elif type(in_) is BoolType:
            val = "boolean"
        elif type(in_) is StringType:
            val = "java/lang/String"
        elif type(in_) is ArrayType:
            val = self.getJVMType(in_)
        return self.jvm.emitANEWARRAY(val)

    #* tạo ra array nhiều chiều
    def emitMULTIANEWARRAY(self, in_, frame):
        # frame: Frame
        # in_: Type
        if type(in_) is ArrayType:
            dimens = len(in_.size)
            return self.jvm.emitMULTIANEWARRAY(self.getJVMType(in_), str(dimens))
    
    #* nhân 2 vùng stack dùng cho array  
    def emitDUP(self, frame):
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()
         
    # def emitIFICMPGT(self, label, frame):
    #     # label: Int
    #     # frame: Frame

    #     frame.pop()
    #     return self.jvm.emitIFICMPGT(label)

    # def emitIFICMPLT(self, label, frame):
    #     # label: Int
    #     # frame: Frame

    #     frame.pop()
    #     return self.jvm.emitIFICMPLT(label)



    # def emitPOP(self, frame):
    #     # frame: Frame

    #     frame.pop()
    #     return self.jvm.emitPOP()



 

