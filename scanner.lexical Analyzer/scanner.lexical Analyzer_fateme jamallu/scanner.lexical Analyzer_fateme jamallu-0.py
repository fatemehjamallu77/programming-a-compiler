rs_table=[["integer","(RS,INT DATATYPE)"],["real","(RS,REAL DATATYPE)"],["word","(RS,STRING)"],
          ["char","(RS,CHARACTER)"],["brook","(RS,ARRAY)"],["though","(RS,IF_CONDITION)"],
          ["barring","(RS,ELSE IF_CONDITION)"],["otherwise","(RS,ELSE_CONDITION)"],
          ["\t","(RS,TAB IN START OF LINE)"],["continue","(RS,WHILE_LOOP)"],["keep","(RS,FOR_LOOP)"]]
  
dl_op_table=[[":=","(DLM_OP,ASSIGN)"],["=","(DLM_OP,EQUAL)"],[">","(DLM_OP,GREATER THAN)"],
             ["<","(DLM_OP,LESS THAN)"],["<=","(DLM_OP,LESS THAN OR EQUAL TO)"],
             [">=","(DLM_OP,GREATER THAN OR EQUAL TO)"],["!=","(DLM_OP,NOT EQUAL)"],
             ["+","(DLM_OP,ADD)"],["-","(DLM_OP,SUBTRACT)"],["*","(DLM_OP,MULTIPLY)"],
             ["/","(DLM_OP,DIVISION)"],["^","(DLM_OP,POWER)"],["&","(DLM_OP,AND)"],
             ["|","(DLM_OP,OR)"],["//","(DLM_OP,REMAIN)"]]

block=[["(","(BLOCK,LEFT_BRACKET)"],[")","(BLOCK,RIGHT_BRACKET)"],
       ["%","(BLOCK,SEMICOLON)"],["|.","(BLOCK,START OF MULTILINE_COMMENT)"],
       [".|","(BLOCK,END OF MULTILINE_COMMENT)"],["||","(BLOCK,STARTR OF SINGLELINE_COMMENT)"],
      ["\n","(BLOCK,ENTER_BLOCK)"]]
variables=[]
symbol_table=[["integer","(RS,INT DATATYPE)"],["real","(RS,REAL DATATYPE)"],["word","(RS,STRING)"],["char","(RS,CHARACTER)"],
              ["brook","(RS,ARRAY)"],["though","(RS,IF_CONDITION)"],["barring","(RS,ELSE IF_CONDITION)"],["otherwise","(RS,ELSE_CONDITION)"],
              ["\t","(RS,START OF CONDITION/LOOP)"],["continue","(RS,WHILE_LOOP)"],["keep","(RS,FOR_LOOP)"],[":=","(DLM_OP,ASSIGN)"],
              ["=","(DLM_OP,EQUAL)"],[">","(DLM_OP,GREATER THAN)"],["<","(DLM_OP,LESS THAN)"],["<=","(DLM_OP,LESS THAN OR EQUAL TO)"],
              [">=","(DLM_OP,GREATER THAN OR EQUAL TO)"],["!=","(DLM_OP,NOT EQUAL)"],["+","(DLM_OP,ADD)"],["-","(DLM_OP,SUBTRACT)"],["*","(DLM_OP,MULTIPLY)"],
              ["/","(DLM_OP,DIVISION)"],["^","(DLM_OP,POWER)"],["&","(DLM_OP,AND)"],["|","(DLM_OP,OR)"],["//","(DLM_OP,REMAIN)"],
              ["(","(BLOCK,LEFT_BRACKET)"],[")","(BLOCK,RIGHT_BRACKET)"],["%","(BLOCK,SEMICOLON)"],["|.","(BLOCK,START OF MULTILINE_COMMENT)"],
              [".|","(BLOCK,END OF MULTILINE_COMMENT)"],["||","(BLOCK,STARTR OF SINGLELINE_COMMENT)"],["\n","(BLOCK,ENTER_BLOCK)"]]

def lookup_rs(tok1):
    lexeme_code=-1
    counter=-1
    for key in rs_table:
        counter=counter +1
        if(tok1==key[0]):
            lexeme_code=counter
    if(lexeme_code !=-1):
        return lexeme_code      
    else:
        return -1  


def lookup_block(tok3):
    lexeme_code=-1
    counter=-1
    for key in block:
        counter=counter +1
        if(tok3==key[0]):
            lexeme_code=counter
    if(lexeme_code !=-1):
        return lexeme_code      
    else:
        return -1   

def lookup_dl_op(tok2):
    lexeme_code=-1
    counter=-1
    for key in dl_op_table:
        counter=counter +1
        if(tok2==key[0]):
            lexeme_code=counter
    if(lexeme_code !=-1):
        return lexeme_code      
    else:
        return -1


file_scann=open('C:/Users/Active/Desktop/testcase.txt',"r")
#line_token =file_scann.readline()
text_input=file_scann.read()
tokenize=text_input.split("\n")
newline=False
number_of_line=0
mline_com=False
sline_com=False
end_enter=True
what_is=0
counter_part=-1
variables_count=-1
id_count=len(rs_table)+len(dl_op_table)+len(block)-1

while(number_of_line<len(tokenize)):
    txt_line=tokenize[number_of_line]
    if(txt_line[0]==" "):
        print("(RS,TAB IN START OF LINE)") 
    newline=False
    counter_part=-1
    list_token=tokenize[number_of_line].split(" ")
    length_of_list=len(list_token)
    if(mline_com==False and sline_com==False):
        end_enter=True
        for part in list_token:
            counter_part=counter_part+1
            if(lookup_block(part)!= -1):
                if(part=="||" and sline_com==False and mline_com==False ):
                    if(sline_com==False):
                        end_enter=False
                        sline_com=True
                        newline=True
                        print("start single line comment")
                        print("\n")

                if(part=="||" and sline_com==True and mline_com==False ):
                    pass 

                elif(part=="|." and sline_com==True and mline_com==False ):
                    pass
                elif(part==".|" and sline_com==True and mline_com==False ):
                    pass

                elif(part=="|." and sline_com==False ):
                    mline_com=True
                    end_enter=False
                    print("start multi line comment from right side")
                    break
                
                else:
                    tuple0=block[lookup_block(part)]
                    print(str(tuple0[1]))                    
                                    
            if(lookup_rs(part)==-1  and sline_com==False and mline_com==False):
                for char in range(0,len(part)):
                    if( part.isdigit() and len(part)>=1 and part!="\n"):
                        what_is=0
                        break
                    elif(char<len(part)-2 and part[char].isdigit() and part[char+2].isdigit() and part.isdigit()==False):
                        what_is=-1
                        break
                    else:
                        what_is=1
                        break
                        
                if(what_is==0):
                    variables.append(str(["INT",str(part)]))
                    print(str(("INT",str(part))))
                                        
                elif(what_is==-1):
                    variables.append(str(["REAL",str(part)]))
                    print(str(("REAL",str(part))))
                    
                    
                elif(what_is==1 and lookup_dl_op(part)== -1 and lookup_rs(part)==-1 and lookup_block(part)==-1 and len(part)>=1 ):
                     variables_count=variables_count+1
                     id_count=id_count+1
                     str_code=str(id_count)
                     variables.append([str(part),str(("ID",str_code))])
                     print(str(("ID",str_code)))                                        
                    
            if(lookup_dl_op(part) !=-1 and sline_com==False and mline_com==False ):
                tuple1=dl_op_table[lookup_dl_op(part)]
                print(str(tuple1[1]))
                    
            if(lookup_rs(part)!=-1 and len(part)>1 and sline_com==False and mline_com==False and part!="\t" ):
                tuple2=rs_table[lookup_rs(part)]
                print(str(tuple2[1]))                
                                     
            if(lookup_rs(part)!=-1 and part=="\t"  and counter_part==0 and sline_com==False and mline_com==False  ):
                tuple3=rs_table[lookup_rs(part)]
                print(str(tuple3[1]))                 
                    
            if(part=="\t" and counter_part!=0):
                pass                            
                           
            if(sline_com==True and counter_part==length_of_list-1):
                sline_com=False
                number_of_line=number_of_line+1
                counter_part=-1
                break                
            
            if(sline_com==True and counter_part!=length_of_list-1):
                pass
                                      
    if(mline_com==True and list_token[length_of_list-1]==".|" ):
        mline_com=False
        number_of_line=number_of_line+1
        newline=True
        print("end of multi line comment from left side")
        print("\n")
        end_enter=True
                   
    elif(mline_com==True):
        number_of_line=number_of_line+1
        newline=True
                
    if not newline:
        number_of_line=number_of_line+1
        newline=False
        
#    if(mline_com==False and end_enter==True):
#        print(str((("BLOCK","ENTER_BLOCK"))))     

if(mline_com==True):
    pass
                    
symbol_table.append(variables)
file_scann.close()

                
