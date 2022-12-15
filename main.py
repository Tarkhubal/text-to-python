file = open("./past-your-script-here.txt", "r")
lines_lst = file.readlines()
vars_lst = []
if_test = True

def textType(text):
    if "^^" in text:
        return "int"


for loop in range(len(lines_lst)):
    actual_line = lines_lst[loop]
    # print(str(actual_line)) # debug
    
    if actual_line == "\n" or actual_line == "" or actual_line == " ":
        pass
    
    elif actual_line.startswith("/"):
        cut = actual_line.split("/")
        # print(str(cut)) # debug
        
        variable = cut[1]
        content = cut[2].split("\n")[0]
        content_type = textType(content)
        
        if content_type == "int":
            content = int(content.split("^^")[1])
        vars_lst += [variable, content]
        # print(str(vars_lst)) # debug
        
        del(variable, content, cut, content_type)
    
    elif "!afficher " in actual_line:
        # print(vars_lst) # debug
        print_content = actual_line.split("!afficher ")[1]
        print_content = print_content.split("\n")[0]
        # print("\"" + str(print_content) + "\"") # debug
        
        if if_test == False:
            pass
        elif print_content in vars_lst:
            print_content_index = vars_lst.index(print_content) + 1
            # print(str(True), print_content_index) # debug
            print(vars_lst[print_content_index])
            
            del(print_content_index)
        else:
            print(actual_line.split("!afficher ")[1])
        
        if_test = True
        
        del(print_content)
       
    elif actual_line.startswith("!si "):
        if_content = actual_line.split("!si ")
        if_content = if_content[1].split(" est ")
        
        if_compare1 = None
        if_compare2 = None
        
        # print("\"" + str(if_content) + "\"") # debug
        if if_content[0] in vars_lst:
            if_content_index = vars_lst.index(if_content[0]) + 1
            # print("\"" + str(if_content) + "\"", if_content_index) # debug
            if_compare1 = vars_lst[vars_lst.index(if_content[0]) + 1]
            # print("\"" + str(if_compare1) + "\"") # debug
            
            if "non egale a" in if_content[1]:
                if_compare2 = if_content[1].split("non egale a ")[1]
                if_compare2 = if_compare2.split(" alors\n")[0]
                
                if if_compare2 in vars_lst:
                    if_compare2 = vars_lst[vars_lst.index(if_compare2) + 1]
                # print("\"" + str(if_compare2) + "\"") # debug
                else:
                    if_compare2 = if_compare2.split("\n")[0]
                
                if if_compare1 != if_compare2:
                    if_test = True
                else:
                    if_test = False
            
            elif "egale a" in if_content[1]:
                if_compare2 = if_content[1].split("egale a ")[1]
                if_compare2 = if_compare2.split(" alors\n")[0]
                
                if if_compare2 in vars_lst:
                    if_compare2 = vars_lst[vars_lst.index(if_compare2) + 1]
                else:
                    if_compare2 = if_compare2.split("\n")[0]
                # print("\"" + str(if_compare2) + "\"") # debug
                
                if if_compare1 == if_compare2:
                    if_test = True
                    # print("True") # debug
                else:
                    if_test = False
                    # print("False") # debug
                
                # print("\"" + str(if_test) + "\"") # debug
            elif "superieur a" in if_content[1]:
                if_compare2 = if_content[1].split("superieur a ")[1]
                if_compare2 = if_compare2.split(" alors\n")[0]
                
                if if_compare2 in vars_lst:
                    if_compare2 = vars_lst[vars_lst.index(if_compare2) + 1]
                else:
                    if_compare2 = if_compare2.split("\n")[0]
                # print("\"" + str(if_compare2) + "\"") # debug
                
                if if_compare1 > if_compare2:
                    if_test = True
                else:
                    if_test = False
            
            elif "inferieur a" in if_content[1]:
                if_compare2 = if_content[1].split("inferieur a ")[1]
                if_compare2 = if_compare2.split(" alors\n")[0]
                
                if if_compare2 in vars_lst:
                    if_compare2 = vars_lst[vars_lst.index(if_compare2) + 1]
                else:
                    if_compare2 = if_compare2.split("\n")[0]
                
                if if_compare1 < if_compare2:
                    if_test = True
                else:
                    if_test = False

        else:
            if_compare1 = if_content[0]
        # print("\"" + str(if_compare1) + "\"", "\"" + str(if_compare2) + "\"") # debug
        
        del(if_compare1, if_compare2, if_content)