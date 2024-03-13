import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # Test Identifier (101 - 108)
    def test101(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>",101))
    
    def test102(self):
        self.assertTrue(TestLexer.test("1PPL", "1,PPL,<EOF>", 102))
    
    def test103(self):
        self.assertTrue(TestLexer.test("P11.3e3PL", "P11,Error Token .", 103))
        
    def test104(self):
        self.assertTrue(TestLexer.test("__AEfe", "__AEfe,<EOF>", 104))
    
    def test105(self):
        self.assertTrue(TestLexer.test("__@fe", "__,Error Token @", 105))
    
    def test106(self):
        self.assertTrue(TestLexer.test("___", "___,<EOF>", 106))
    
    def test107(self):
        self.assertTrue(TestLexer.test("____", "____,<EOF>", 107))
    
    def test108(self):
        self.assertTrue(TestLexer.test("ab_23_aa", "ab_23_aa,<EOF>", 108))
    
    def test109(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 109))
    
    # Test character set 
    def test110(self):
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))
    
    # Test operators
    def test111(self):
        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))
        
    # Test number literal
    def test112(self):
        input = "0 -0 199 001 012. 12. 0. 12.3 12.3e3 12.3e-30 2.e3 0.e-30 31e+3 31e-3 0e+3 0e-3"
        expect = "0,-,0,199,001,012.,12.,0.,12.3,12.3e3,12.3e-30,2.e3,0.e-30,31e+3,31e-3,0e+3,0e-3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
    
    def test113(self):
        self.assertTrue(TestLexer.test(".12e-3","Error Token .",113))
    
    def test114(self):
        self.assertTrue(TestLexer.test("12.2h-3","12.2,h,-,3,<EOF>",114))
    
    # Test string literal
    def test115(self):
        input = """ "He asked me: \'"Where is John?\'"" """
        expect = "He asked me: \'\"Where is John?\'\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect,115))
    
    def test116(self):
        self.assertTrue(TestLexer.test(""" "" """,",<EOF>",116)) # chuỗi rỗng
    
    def test117(self):
        self.assertTrue(TestLexer.test(""" "'"Thai '" Binh '"" ""","'\"Thai '\" Binh '\",<EOF>",117))
    
    def test118(self):
        self.assertTrue(TestLexer.test(""" "Tien \\f \\n ccc" """, """Tien \\f \\n ccc,<EOF>""", 118))
    
    def test119(self):
        input = """ "abc'abc" """
        output = """abc'abc,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,119))
    
    def test120(self):
        input = r""" "Hello World \t \f \b \\ \'" """
        expect = r"""Hello World \t \f \b \\ \',<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 120)) 
    
    def test121(self):
        input = """(("a'""..."a\\'") == "a'"a\\'")[3,2]"""
        expect = """(,(,a'",...,a\\',),==,a'"a\\',),[,3,,,2,],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect,121))
        
    #Test legal escape
    def test122(self):
        input = """ "\\b \\f \\r \\n \\t \\\\ Asm \\b \\f \\r \\n \\t \\\\  PPL \\b \\f \\r \\n \\t \\\\" """
        expect = "\\b \\f \\r \\n \\t \\\\ Asm \\b \\f \\r \\n \\t \\\\  PPL \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,122))  
    
    
    #Test unclosed string
    def test123(self):
        self.assertTrue(TestLexer.test(""" "PPL \n" """, "Unclosed String: PPL ", 123))
    
    def test124(self):
        self.assertTrue(TestLexer.test(""" "PPL \n Asm" """, "Unclosed String: PPL ", 124))
    
    def test125(self):
        self.assertTrue(TestLexer.test(""" "PPL  """, "Unclosed String: PPL  ", 125))
    
    def test126(self):
        self.assertTrue(TestLexer.test(""" "PPL \\n \n """, "Unclosed String: PPL \\n ", 126))
    
    def test127(self):
        self.assertTrue(TestLexer.test(""" "PPL ' \\n \\b """, "Unclosed String: PPL ' \\n \\b ", 127))
    
    def test128(self):
        self.assertTrue(TestLexer.test(""" "PPL ' " " """, "PPL ' ,Unclosed String:  ", 128))
    
    def test129(self):
        self.assertTrue(TestLexer.test(""" "PPL \\' ""1 """, "PPL \\' ,Unclosed String: 1 ", 129)) 
    
    #Test illegal escape
    def test130(self):
        self.assertTrue(TestLexer.test(""" "PPL \\1  """, "Illegal Escape In String: PPL \\1", 130))
    
    def test131(self):
        self.assertTrue(TestLexer.test(""" "PPL \\2 \\n \n """, "Illegal Escape In String: PPL \\2", 131))
    
    def test132(self):
        self.assertTrue(TestLexer.test(""" "PPL \\e \\n \\r """, "Illegal Escape In String: PPL \\e", 132)) 
    
    def test133(self):       
        self.assertTrue(TestLexer.test(""" "PPL \\321 \\n \\r """, "Illegal Escape In String: PPL \\3", 133))
    
    def test134(self):
        self.assertTrue(TestLexer.test(""" "PPL \\"1 " """, "Illegal Escape In String: PPL \\\"", 134))  
    
    # Test comment and newline
    def test135(self):
        self.assertTrue(TestLexer.test("## PPL Asm","<EOF>",135)) 
    
    def test136(self): 
        self.assertTrue(TestLexer.test("###","<EOF>",136))
    
    def test137(self): 
        self.assertTrue(TestLexer.test("a##<-5","a,<EOF>",137))
    
    def test138(self): 
        self.assertTrue(TestLexer.test("a#","a,Error Token #",138))
    
    def test139(self):    
        self.assertTrue(TestLexer.test("a\n##1\nb","a,\n,\n,b,<EOF>",139))
      
    # Test string with comment
    def test140(self):
        input = (
            """ "This is a complex string with \\'quote\\' and has comment ##abcd" """
        )
        expect = """This is a complex string with \\'quote\\' and has comment ##abcd,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 140))
    
    def test141(self):
        input = r"""
            ## "This should not be printed"
            "##This should be printed"
        """
        expect = "\n,\n,##This should be printed,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))
    
    # Test string with escape
    def test142(self):
        input = """ "Hello163 \t " """
        expect = "Hello163 	 ,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))
    
    def test143(self):
        input = r""" "abcd\" """
        expect = r"""Illegal Escape In String: abcd\""""
        self.assertTrue(TestLexer.test(input, expect, 143))
    
    #Test string with concat
    def test144(self):
        input = """
            a <- "PPL"
            b <- "Asm"
            c <- a...b
        """
        expect = (
            """\n,a,<-,PPL,\n,b,<-,Asm,\n,c,<-,a,...,b,\n,<EOF>"""
        )
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test145(self):
        self.assertTrue(TestLexer.test("1...3", "1.,Error Token .",145))
    
    def test146(self):
        input = """
            ":)))" ":(((" ":v"
            ":o" "c"
        """
        expect = """\n,:))),:(((,:v,\n,:o,c,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 146))
        
    def test147(self): # Test multiple string
        input = """
            "a" "b" "c" "d" "e"
        """
        expect = """\n,a,b,c,d,e,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 147))
    
    #Test array
    def test148(self):
        self.assertTrue(TestLexer.test("number a[5] <- [1,2,3,4,5]", "number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],<EOF>",148))
    
    def test149(self):
        self.assertTrue(TestLexer.test(" [[1, 2], [4, 5], [3, 5]]", "[,[,1,,,2,],,,[,4,,,5,],,,[,3,,,5,],],<EOF>",149))
    
    def test150(self): ## Array expression
        self.assertTrue(TestLexer.test("[1*2, 12e3, 9e8, 4 / 2]", "[,1,*,2,,,12e3,,,9e8,,,4,/,2,],<EOF>",150))
    
    
    def test151(self):
        input = """if (3 >= 2 = true) ## This is a comment  
a <- a + 1"""
        expect = """if,(,3,>=,2,=,true,),
,a,<-,a,+,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect,151))
      
    def test152(self):
        input = """ ## This is a single comment.
a <- 5"""  
        end = "\n,a,<-,5,<EOF>"
        self.assertTrue(TestLexer.test(input, end, 152))
    
        
    def test153(self):
        input = """## this is \r \b 
a <- 5"""
        output = """\n,a,<-,5,<EOF>"""
        self.assertTrue(TestLexer.test(input,output,153))

    def test154(self):
        input = r"""for i until i < 10 by 1 
                writeInt(i)
        """
        expect = "for,i,until,i,<,10,by,1,\n,writeInt,(,i,),\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test155(self):
        input = r""" foo(2 + x, 4.0 / y)
            goo()
        """
        expect = "foo,(,2,+,x,,,4.0,/,y,),\n,goo,(,),\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))
    
    def test156(self):
        input = """
        func main ()
        begin
            for i until i >= 5 by 2
                printInteger("Yoooo!")
        end
        """
        expect = "\n,func,main,(,),\n,begin,\n,for,i,until,i,>=,5,by,2,\n,printInteger,(,Yoooo!,),\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))
    
    def test157(self):
        input = """
        func main () begin
            for i until i >= 5*2 by 2
                for j until j >= 5*2 by 1
                    printInteger(i+j)
        end
        """
        expect = """
,func,main,(,),begin,
,for,i,until,i,>=,5,*,2,by,2,
,for,j,until,j,>=,5,*,2,by,1,
,printInteger,(,i,+,j,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 157))
    
    def test158(self):
        input = """
        func void () begin
            for i until i >= getMax() by 1 begin
                if(i = threshold)
                    break
                if (i<0)
                    continue
                else printInteger(i)
            end
        end
        """
        expect = """\n,func,void,(,),begin,\n,for,i,until,i,>=,getMax,(,),by,1,begin,\n,if,(,i,=,threshold,),\n,break,\n,if,(,i,<,0,),\n,continue,\n,else,printInteger,(,i,),\n,end,\n,end,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158))
        
    ## Test function call
    def test159(self):
        input ="""function main () begin
            hello()
            hello("Sang")
            hello("Sang","Kha")
            hello(hello("Sang"),"Kha")
        end"""
        
        expect = """function,main,(,),begin,
,hello,(,),
,hello,(,Sang,),
,hello,(,Sang,,,Kha,),
,hello,(,hello,(,Sang,),,,Kha,),
,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 159))
    
    def test160(self):
        input = """
        func main () begin
            f(f())
            f(f(f(f(f()))))
            f(f(f(f(f(f())))),f(f(f(f(f())))))
        end
        """
        expect="""
,func,main,(,),begin,
,f,(,f,(,),),
,f,(,f,(,f,(,f,(,f,(,),),),),),
,f,(,f,(,f,(,f,(,f,(,f,(,),),),),),,,f,(,f,(,f,(,f,(,f,(,),),),),),),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 160))
    
    def test161(self):
        input = """
        func main ()begin   
            f(1*x,_123,"sss"..."aaa",dsa("dsa"),x%5)
        end
        """
        expect = "\n,func,main,(,),begin,\n,f,(,1,*,x,,,_123,,,sss,...,aaa,,,dsa,(,dsa,),,,x,%,5,),\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))
    
    ## Test block statement 
    def test162(self):
        input = """
        func main () begin
            begin
            end
            begin
                hello()
            end
            begin
                a <- 1
            end
        end
        """
        expect = "\n,func,main,(,),begin,\n,begin,\n,end,\n,begin,\n,hello,(,),\n,end,\n,begin,\n,a,<-,1,\n,end,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))
    
    def test163(self):
        input = """
        func main() begin
            begin
                hello()
                a<-1
            begin
                hello()
                a<-1
            end
        end
        """
        output ="\n,func,main,(,),begin,\n,begin,\n,hello,(,),\n,a,<-,1,\n,begin,\n,hello,(,),\n,a,<-,1,\n,end,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,output, 163))

    def test_164(self):
            input = "forforforforforforforforfor"
            expect = "forforforforforforforforfor,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,164))

    def test_165(self):
            input = "123for123-131415*99990______1bc928902___a__a___jkl_forifelseelifbeginend"
            expect = "123,for123,-,131415,*,99990,______1bc928902___a__a___jkl_forifelseelifbeginend,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,165))

    def test_166(self):
            input = "bool a <- falseeee"          
            expect = "bool,a,<-,falseeee,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,166))

    def test_167(self):
            input = "bool a <- trueeeeee"
            expect = "bool,a,<-,trueeeeee,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,167))

    def test_168(self):
            input = "=====================================>"
            expect = "==,==,==,==,==,==,==,==,==,==,==,==,==,==,==,==,==,==,=,>,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,168))

    def test_169(self):
            input = "<======================================"
            expect = "<=,==,==,==,==,==,==,==,==,==,==,==,==,==,==,==,==,==,==,=,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,169))

    def test_170(self):
            input = """
func main()
begin
    number a
    number b
    number temp
    number i
    a <- 12
    b <- 6
    for i until true by 1
    begin
        if (a < b)
        begin
            if (a = 1) break
            else
            begin
                number temp <- a
                a <- b - a
                b <- temp
            end
        end
        else
        begin
            if (b = 1) break
            else
            begin
                number temp <- b
                b <- a - b
                a <- temp
            end
        end
    end
    return max(a, b)
end
"""
            expect = """
,func,main,(,),
,begin,
,number,a,
,number,b,
,number,temp,
,number,i,
,a,<-,12,
,b,<-,6,
,for,i,until,true,by,1,
,begin,
,if,(,a,<,b,),
,begin,
,if,(,a,=,1,),break,
,else,
,begin,
,number,temp,<-,a,
,a,<-,b,-,a,
,b,<-,temp,
,end,
,end,
,else,
,begin,
,if,(,b,=,1,),break,
,else,
,begin,
,number,temp,<-,b,
,b,<-,a,-,b,
,a,<-,temp,
,end,
,end,
,end,
,return,max,(,a,,,b,),
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,170))

    def test_171(self):
            input = """
func create_string()
begin
    string res <- ""
    number i <- 1
    for i until 100 by 1
    begin
        res <- res ... str(i)
    end
    return res
end
"""
            expect = """
,func,create_string,(,),
,begin,
,string,res,<-,,
,number,i,<-,1,
,for,i,until,100,by,1,
,begin,
,res,<-,res,...,str,(,i,),
,end,
,return,res,
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,171))

    def test_172(self):
            input = """bool done[100] <- [true, true, true, false, true, not false, ...]"""
            expect = "bool,done,[,100,],<-,[,true,,,true,,,true,,,false,,,true,,,not,false,,,...,],<EOF>"
            self.assertTrue(TestLexer.test(input,expect,172))

    def test_173(self):
            input = "bool flag = !false"
            expect = "bool,flag,=,Error Token !"
            self.assertTrue(TestLexer.test(input,expect,173))

    def test_174(self):
            input = """
func min(number a, number b, number c)
begin
    if (a < b) b <- a
    if (c < b) b <- c
    return b
end
"""
            expect = """
,func,min,(,number,a,,,number,b,,,number,c,),
,begin,
,if,(,a,<,b,),b,<-,a,
,if,(,c,<,b,),b,<-,c,
,return,b,
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,174))

    def test_175(self):
            input = """
func date(number month)
begin
    if (month = 2) return 29
    elif ((month = 1) or (month = 3)) return 31
    elif ((month = 4) or (month = 6)) return 30
    else return 32
end
"""
            expect = """
,func,date,(,number,month,),
,begin,
,if,(,month,=,2,),return,29,
,elif,(,(,month,=,1,),or,(,month,=,3,),),return,31,
,elif,(,(,month,=,4,),or,(,month,=,6,),),return,30,
,else,return,32,
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,175))

    def test_176(self):
            input = """
func sort(number arr[100])
begin
    ## Go to something default sort functions
    number sorted_arr[100] <- arr
    return sorted_arr[100]
end
"""
            expect = """
,func,sort,(,number,arr,[,100,],),
,begin,
,
,number,sorted_arr,[,100,],<-,arr,
,return,sorted_arr,[,100,],
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,176))

    def test_177(self):
        input = """
            func isOdd (number x)
                return x != 0
            func getArr (number x) begin
                return [x,x*2,x*3]
            end
        """
        expect = "\n,func,isOdd,(,number,x,),\n,return,x,!=,0,\n,func,getArr,(,number,x,),begin,\n,return,[,x,,,x,*,2,,,x,*,3,],\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test_178(self):
            input = """
func foo()
begin
    if (a = b) do(b)
    elif (a < b) do(b)
    else do(a)
end
"""
            expect = """
,func,foo,(,),
,begin,
,if,(,a,=,b,),do,(,b,),
,elif,(,a,<,b,),do,(,b,),
,else,do,(,a,),
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,178))

    def test_179(self):
            input = """
iff(a > c) do(a)
iffff(a > c) do(c)
iffffffff(a < c) do(a, c)
"""
            expect = """
,iff,(,a,>,c,),do,(,a,),
,iffff,(,a,>,c,),do,(,c,),
,iffffffff,(,a,<,c,),do,(,a,,,c,),
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,179))

    def test_180(self):
            input = "abc    \n  abc"
            expect = "abc,\n,abc,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,180))

    def test_181(self):
            input = """
func test(number a, string s, bool done[12])
begin
    number b <- a
    number c <- a + b * b
    string ss <- (s ... s) ... s
    bool flag <- not (ss == s) and (b > a)
    done[0] <- flag
    return done
end
"""
            expect = """
,func,test,(,number,a,,,string,s,,,bool,done,[,12,],),
,begin,
,number,b,<-,a,
,number,c,<-,a,+,b,*,b,
,string,ss,<-,(,s,...,s,),...,s,
,bool,flag,<-,not,(,ss,==,s,),and,(,b,>,a,),
,done,[,0,],<-,flag,
,return,done,
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,181))

    def test_182(self):
            input = """
class Shape()
begin
    number height
    number width
    
    func calcArea()
    begin
        return height * width
    end
    
    func calcCircum()
    begin
        return (height + width) * 2
    end
end
"""
            expect = """
,class,Shape,(,),
,begin,
,number,height,
,number,width,
,
,func,calcArea,(,),
,begin,
,return,height,*,width,
,end,
,
,func,calcCircum,(,),
,begin,
,return,(,height,+,width,),*,2,
,end,
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,182))

    def test_183(self):
            input = """
def test_183(self)
    input = ""
    expect = "<EOF>"
    self->assertTrue(TestLexer->test(input,expect,183))
"""
            expect = """
,def,test_183,(,self,),
,input,=,,
,expect,=,<EOF>,
,self,-,>,assertTrue,(,TestLexer,-,>,test,(,input,,,expect,,,183,),),
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,183))

    def test_184(self):
            input = """
## Well, we cannot use the dot (.) operator
number a <- x.height
"""
            expect = """
,
,number,a,<-,x,Error Token ."""
            self.assertTrue(TestLexer.test(input,expect,184))

    def test_185(self):
            input = """
func main()
begin
    number option
    cin >> option
    if (option = 1) cout << "Hello world"
    elif (option = 2)
    begin
        string name
        cin >> name
        cout << "Hello " << name
    end
    else
    begin
        string name
        number age
        cin >> name >> age
        cout << "Hello " << age << " years old " << name
    end
end 
"""
            expect = """
,func,main,(,),
,begin,
,number,option,
,cin,>,>,option,
,if,(,option,=,1,),cout,<,<,Hello world,
,elif,(,option,=,2,),
,begin,
,string,name,
,cin,>,>,name,
,cout,<,<,Hello ,<,<,name,
,end,
,else,
,begin,
,string,name,
,number,age,
,cin,>,>,name,>,>,age,
,cout,<,<,Hello ,<,<,age,<,<, years old ,<,<,name,
,end,
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,185))

    def test_186(self):
            input = """
func calcSum(number n)
begin
    number i <- 1
    number sum <- 0
    for i until n by 1
    begin
        sum <- sum + i
    end
    return sum
end
"""
            expect = """
,func,calcSum,(,number,n,),
,begin,
,number,i,<-,1,
,number,sum,<-,0,
,for,i,until,n,by,1,
,begin,
,sum,<-,sum,+,i,
,end,
,return,sum,
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,186))

    def test_187(self):
            input = """
func recursion(number i, number n)
begin
    if (i = n) return n
    else return recursion(i + 1, n) + i
end
"""
            expect = """
,func,recursion,(,number,i,,,number,n,),
,begin,
,if,(,i,=,n,),return,n,
,else,return,recursion,(,i,+,1,,,n,),+,i,
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,187))

    def test_188(self):
            input = """
func buildHouse()
begin
    number width -> readNumber()
    number length -> readNumber()
    number budget -> readNumber()
    print("Starting building house")
    print("Creating strong base")
    print("Buying brick, cement and hiring labours")
    print("Working on materials")
    print("Completing the house, cleaning dirt")
    print("Decorating the house")
    print("Having fun with new house")
end
"""
            expect = """
,func,buildHouse,(,),
,begin,
,number,width,-,>,readNumber,(,),
,number,length,-,>,readNumber,(,),
,number,budget,-,>,readNumber,(,),
,print,(,Starting building house,),
,print,(,Creating strong base,),
,print,(,Buying brick, cement and hiring labours,),
,print,(,Working on materials,),
,print,(,Completing the house, cleaning dirt,),
,print,(,Decorating the house,),
,print,(,Having fun with new house,),
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,188))

    def test_189(self):
            input = """
func callingDestroyer()
begin
    call()
    call(call())
    call(call(call()))
    call(call(call(call())))
    call(call(call(call(call()))))
    call(call(call(call(call(call())))))
    call(call(call(call(call(call(call()))))))
    call(call(call(call(call(call(call(call())))))))
    call(call(call(call(call(call(call(call(call()))))))))
    call(call(call(call(call(call(call(call(call(call())))))))))
    call(call(call(call(call(call(call(call(call(call(call()))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call())))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call()))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call())))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call(call()))))))))))))))
    call(call(call(call(call(call(call(call(call(call(call(call(call(call(call(call())))))))))))))))
end
"""
            expect = """
,func,callingDestroyer,(,),
,begin,
,call,(,),
,call,(,call,(,),),
,call,(,call,(,call,(,),),),
,call,(,call,(,call,(,call,(,),),),),
,call,(,call,(,call,(,call,(,call,(,),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),),),),),),),),
,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,call,(,),),),),),),),),),),),),),),),),
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,189))

    def test_190(self):
            input = """
func subDestroyer()
begin
    number a <- (b)
    number a <- ((b))
    number a <- (((b)))
    number a <- ((((b))))
    number a <- (((((b)))))
    number a <- ((((((b))))))
    number a <- (((((((b)))))))
    number a <- ((((((((b))))))))
    number a <- (((((((((b)))))))))
    number a <- ((((((((((b))))))))))
    number a <- (((((((((((b)))))))))))
    number a <- ((((((((((((b))))))))))))
    number a <- (((((((((((((b)))))))))))))
    number a <- ((((((((((((((b))))))))))))))
    number a <- (((((((((((((((b)))))))))))))))
end
"""
            expect = """
,func,subDestroyer,(,),
,begin,
,number,a,<-,(,b,),
,number,a,<-,(,(,b,),),
,number,a,<-,(,(,(,b,),),),
,number,a,<-,(,(,(,(,b,),),),),
,number,a,<-,(,(,(,(,(,b,),),),),),
,number,a,<-,(,(,(,(,(,(,b,),),),),),),
,number,a,<-,(,(,(,(,(,(,(,b,),),),),),),),
,number,a,<-,(,(,(,(,(,(,(,(,b,),),),),),),),),
,number,a,<-,(,(,(,(,(,(,(,(,(,b,),),),),),),),),),
,number,a,<-,(,(,(,(,(,(,(,(,(,(,b,),),),),),),),),),),
,number,a,<-,(,(,(,(,(,(,(,(,(,(,(,b,),),),),),),),),),),),
,number,a,<-,(,(,(,(,(,(,(,(,(,(,(,(,b,),),),),),),),),),),),),
,number,a,<-,(,(,(,(,(,(,(,(,(,(,(,(,(,b,),),),),),),),),),),),),),
,number,a,<-,(,(,(,(,(,(,(,(,(,(,(,(,(,(,b,),),),),),),),),),),),),),),
,number,a,<-,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,b,),),),),),),),),),),),),),),),
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,190))

    def test_191(self):
            input = """
func unaryDestroyer()
begin
    a <- not not not---not-not-not not-not not not-not not not not----not-----not not---not not not--foo()[0]
end
"""
            expect = """
,func,unaryDestroyer,(,),
,begin,
,a,<-,not,not,not,-,-,-,not,-,not,-,not,not,-,not,not,not,-,not,not,not,not,-,-,-,-,not,-,-,-,-,-,not,not,-,-,-,not,not,not,-,-,foo,(,),[,0,],
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,191))

    def test_192(self):
            input = """
func arrayDestroyer()
begin
    number a <- [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[foo()[1, 2, 3]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
end
"""
            expect = """
,func,arrayDestroyer,(,),
,begin,
,number,a,<-,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,[,foo,(,),[,1,,,2,,,3,],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],],
,end,
,<EOF>"""
            self.assertTrue(TestLexer.test(input,expect,192))

    def test_193(self):
            input = "[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]"
            expect = "[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],<EOF>"
            self.assertTrue(TestLexer.test(input,expect,193))

    def test_194(self):
            input = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()"
            expect = "(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),(,),<EOF>"
            self.assertTrue(TestLexer.test(input,expect,194))

    def test_195(self):
            input = "[[][][][][())))(()())]]][[][[[[[]][]]]]())))))(())))]][]"
            expect = "[,[,],[,],[,],[,],[,(,),),),),(,(,),(,),),],],],[,[,],[,[,[,[,[,],],[,],],],],(,),),),),),),(,(,),),),),],],[,],<EOF>"
            self.assertTrue(TestLexer.test(input,expect,195))

    def test_196(self):
            input = ",,,,,,,,,,,,,,,[],,,,,(),()()(),,(),[][][[[]]]]]]]]])),,,,"
            expect = ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,[,],,,,,,,,,,,(,),,,(,),(,),(,),,,,,(,),,,[,],[,],[,[,[,],],],],],],],],],),),,,,,,,,,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,196))

    def test_197(self):
            input = "00109289001.108905302975320079053277339E-17899753688290382611892"
            expect = "00109289001.108905302975320079053277339E-17899753688290382611892,<EOF>"
            self.assertTrue(TestLexer.test(input,expect,197))

    def test_198(self):
            input = "string a -> \"I think you will need this 50$\"\""
            expect = "string,a,-,>,I think you will need this 50$,Unclosed String: "
            self.assertTrue(TestLexer.test(input,expect,198))

    def test_199(self):
            input = "string a -> \"This is an illegal escape \m"
            expect = "string,a,-,>,Illegal Escape In String: This is an illegal escape \m"
            self.assertTrue(TestLexer.test(input,expect,199))

    def test_200(self):
            input = """
            func mergeSort(number arr[100], number begin, number end) begin
                if (begin >= end)
                    return ## Returns recursively
            
                dynamic mid = begin + (end - begin) / 2
                mergeSort(arr, begin, mid)
                mergeSort(arr, mid + 1, end)
                merge(arr, begin, mid, end)
            end
        """
            expect = "\n,func,mergeSort,(,number,arr,[,100,],,,number,begin,,,number,end,),begin,\n,if,(,begin,>=,end,),\n,return,\n,\n,dynamic,mid,=,begin,+,(,end,-,begin,),/,2,\n,mergeSort,(,arr,,,begin,,,mid,),\n,mergeSort,(,arr,,,mid,+,1,,,end,),\n,merge,(,arr,,,begin,,,mid,,,end,),\n,end,\n,<EOF>"
            self.assertTrue(TestLexer.test(input, expect, 200))
    
    def test_201(self):
        input = """ ## 123 \r \r\n"""
        expect = "\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 201))
    

    
    
    
    
