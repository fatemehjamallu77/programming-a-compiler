parse_table=[
             ["S","main","DT$main$($)$BK" ],["S","integer","DT$main$($)$BK"],["S","real","DT$main$($)$BK"],["S","char","DT$main$($)$BK"],["S","word","DT$main$($)$BK"]
             ,["S","def","DT$main$($)$BK"],["S","void","DT$main$($)$BK"],["DC","integer","VC"],["DC","real","VC"],["DC","char","VC"],["DC","word","VC"],
             ["DC","def","FC"],["DC","void","FC"],["DT","main","@"],["DT","integer","DC$DT"],["DT","real","DC$DT"],["DT","char","DC$DT"],
             ["DT","word","DC$DT"],["DT","def","DC$DT"],["DT","void","DC$DT"],["TE","integer","integer"],["TE","real","real"],["TE","char","char"],
             ["TE","word","word"],["IC","ID", "ID$:=$EP"],["IC","brook","BOK"],["IT","ID","IC$IT"],["IT","%","@"],["IT","brook","IC$IT"],
             ["VC","integer","TE$IT$%"],["VC","real","TE$IT$%"],["VC","char","TE$IT$%"],["VC","word","TE$IT$%"],["FC","def","def$TE$ID$($PS$)$BK"],
             ["FC","void","void$ID$($PS$)$BK"],["PS","integer","PT"],["PS","real","PT"],["PS","char","PT"],["PS","word","PT"],["PS",")","PT"],
             ["PS","[","PT"],["PT","integer","PC$,$PT"],["PT","real","PC$,$PT"],["PT","char","PC$,$PT"],["PT","word","PC$,$PT"],["PT",")","@"],
             ["PT","[","PC$,$PT"],["PC","integer","TE$ID"],["PC","real","TE$ID"],["PC","char","TE$ID"],["PC","word","TE$ID"],
             ["PC","[","[$]$TE$ID"],["VT","integer","VC$VT"],["VT","real","VC$VT"],["VT","char","VC$VT"],["VT","word","VC$VT"],["VT","ID","@"],
             ["VT","def","@"],["VT","(","@"],["VT","return","@"],["VT","continue","@"],["VT","keep","@"],
             ["VT","print","@"],["VT","local","@"],["VT","though","@"],["VT","nothing","@"],
             ["VT","INTN","@"],["VT","REAL","@"],["VT","INTP","@"],["VT","brook","@"],["VT","|.","@"],["VT","||","@"],["BK","begin","begin$STT$end"],
             ["STT","ID","ST$STT"],["STT","def","ST$STT"],["STT","(","ST$STT"],["STT","end","@"],["STT","return","ST$STT"],
             ["STT","continue","ST$STT"],["STT","keep","ST$STT"],["STT","print","ST$STT"],["STT","local","ST$STT"],
             ["STT","though","ST$STT"],["STT","nothing","ST$STT"],["STT","INTN","ST$STT"],["STT","REAL","ST$STT"],["STT","INTP","ST$STT"],["STT","brook","ST$STT"],
             ["STT","|.","ST$STT"],["STT","||","ST$STT"],["ST","ID","EP$%$ST"],["ST","def","EP$%$ST"],["ST","(","EP$%$ST"],["ST","return","return$EP$%"],
             ["ST","continue","continue$($EP$)$BK$ST"],["ST","keep","keep$($EP$%$EP$%$EP$%$)$BK$ST"],["ST","print","print$($ID$)$%$ST"],
             ["ST","local","local$VT$ST"],["ST","though","though$($EP$)$BK$ST$EIT"],["ST","nothing","nothing"],["ST","INTN","EP$%$ST"],["ST","REAL","EP$%$ST"],["ST","INTP","EP$%$ST"],
             ["ST","brook","BN"],["ST","|.","CM"],["ST","||","CM"],["EIT","barring","barring$($EP$)$BK$ST$EIT"],["EIT","otherwise","otherwise$BK$ST"],
             ["EP","ID","A$E"],
             ["EP","def","def$ID$($ET$)"],["EP","(","($EP$OR$EP$)"],["EP","INTN","A$E"],["EP","REAL","A$E"],
             ["EP","INTP","A$E"],["CT","REAL","REAL"],["CT","INTN","INTN"],["CT","INTP","INTP"],["CT","ID","ID"],["A","REAL","CT$A1"],["A","INTN","CT$A1"],
             ["A","INTP","CT$A1"],["A","ID","CT$A1"],
             ["A1","ID","@"],["A1",":=","@"],["A1","%","@"],["A1","def","@"],["A1",")","@"],["A1","(","@"],["A1",",","@"],["A1","end","@"],
             ["A1","return","@"],["A1","continue","@"],["A1","keep","@"],["A1","print","@"],["A1","local","@"],["A1","though","@"],["A1","nothing","@"],
             ["A1","barring","@"],["A1","otherwise","@"],["A1","REAL","@"],["A1","INTN","@"],["A1","INTP","@"],["A1","*","*$CT$A1"],["A1","/","/$CT$A1"],
             ["A1","//","//$CT$A1"],["A1","+","@"],["A1","-","@"],["A1","=","@"],["A1","<","@"],["A1",">","@"],["A1",">=","@"],["A1","<=","@"],["A1","!=","@"],
             ["A1","^","@"],["A1","&","@"],["A1","|","@"],["A1","brook","@"],["A1","|.","@"],["A1","||","@"],
             ["E","ID","@"],["E",":=","@"],["E","%","@"],["E","def","@"],["E",")","@"],["E","(","@"],["E",",","@"],["E","end","@"],
             ["E","return","@"],["E","continue","@"],["E","keep","@"],["E","print","@"],["E","local","@"],["E","though","@"],["E","nothing","@"],
             ["E","barring","@"],["E","otherwise","@"],["E","REAL","@"],["E","INTN","@"],["E","INTP","@"],
             ["E","+","+$A$E"],["E","-","-$A$E"],["E","=","@"],["E","<","@"],["E",">","@"],["E",">=","@"],["E","<=","@"],["E","!=","@"],
             ["E","^","@"],["E","&","@"],["E","|","@"],["E","brook","@"],["E","|.","@"],["E","||","@"],             
             ["OR",":=",":="],["OR","=","="],["OR",">",">"],["OR","<","<"],["OR",">=",">="],["OR","<=","<="],["OR","!=","!="],                      
             ["OR","^","^"],["OR","&","&"],["OR","|","|"],
             ["ET","ID","EP$,$ET"],["ET","def","EP$,$ET"],["ET","(","EP$,$ET"],["ET",")","@"],["ET","INTN","EP$,$ET"],
             ["ET","REAL","EP$,$ET"],["ET","INTP","EP$,$ET"],["BOK","brook","brook$ID$[$AVR$]$DN"],["DN","ID","@"],["DN",":=","@"],["DN","%","@"],
             ["DN","[","DN2$DN"],["DN","brook","@"],["DN2","[","[$AVR$]"],["BN","brook","brook$ID$[$AVR$]$DN$:=$EP$%$ST"],["CM","|.","|.$.|$ST"],
             ["CM","||","||$ST"],["AVR","INTP","INTP"],["AVR","ID","ID"]]


def out_rule(top2,sambol2):
    rule="NULL"
    for number1 in parse_table:
        if(number1[0]==top2 and number1[1]==sambol2):
             rule=number1[2]
    if(rule !="NULL"):
        return rule
        
    return "NULL"     
    
    
def comparison(top3,sambol3):
    match_ts=-1
    for number2 in parse_table:
        if(number2[0]==top3 and number2[1]==sambol3):
            match_ts=1
            break
        
    return match_ts        
        
        

def M_function(top1,sambol1):
    if(sambol1==top1 and sambol1!="#" and top1!="#"):
        return 1
    elif(sambol1=="#" and top1=="#"):
        return 2 
    elif(comparison(top1,sambol1)==1):
        return 3
    else:
        return 4
    
  
parser_file=open('C:/Users/Active/Desktop/New folder (5).testing.txt',"r" )
reading=parser_file.read()
tokens_line=reading.split("\n")

#tokens_line.append("#")

gramer_stack=[]
gramer_stack.append("#")
gramer_stack.append("S")
terminnate=False
error=False
number_of_line=0
s_number=0
while(number_of_line<len(tokens_line)):

        s_number=0
            
        list_token=tokens_line[number_of_line].split(" ")

        while(s_number<len(list_token)):
            if(error==True):
                break
            token=list_token[s_number]
            if(M_function(gramer_stack[len(gramer_stack)-1],token)==1):
                gramer_stack.pop()
                s_number=s_number + 1

                terminate=False
            elif(M_function(gramer_stack[len(gramer_stack)-1],token)==2):
                gramer_stack.pop()
                terminate=True
                s_number=s_number+1 
                             
            elif(M_function(gramer_stack[len(gramer_stack)-1],token)==3):
                terminate=False
                txt=out_rule(gramer_stack[len(gramer_stack)-1],token)
                                
                if(txt != "NULL"):
                    separate=txt.split("$")
                    gramer_stack.pop()
                
                    separate.reverse()

                    for part in separate:
                        if(part!="@"):
                            gramer_stack.append(part)
                            
 
            else:
                s_number=s_number+1
                terminate=False
#                print("invalid syntax/your code dont match whit compiler syntax" )
                error=True
                break

        
        number_of_line=number_of_line+1        
if(gramer_stack[len(gramer_stack)-1]=="#" and number_of_line==len(tokens_line) ):
    terminate=True
    
if (terminate==True):
    print("yes/accept")

else:
    print("no/reject")
    print("your programe code reject by parser of compiler/enter correct one")
    
parser_file.close()
