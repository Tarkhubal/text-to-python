file = open("./tests/past-your-script-here.txt", "r")
lines_lst = file.readlines()

vars_lst = []
if_tab_lst = [True]
first_line = True
line_tab = 0
if_compare1 = None
if_compare2 = None

def textType(text):
    if "^^" in text:
        return int(text.split("^^")[1])
    else:
        return str(text)

for loop in range(len(lines_lst)):
    actual_line = lines_lst[loop]
    
    # print("[before] if tab lst =", if_tab_lst) # debug
    # print("actual line =", actual_line) # debug
    
    if actual_line.startswith("__"):
        is_tab = True
        nb_tabs = actual_line.count("__")
    else:
        nb_tabs = 0
    
    if first_line == True:
        if_tab_lst = []
    if nb_tabs == 0:
        if_tab_lst = []
    
    if "__" in actual_line:
        actual_line = actual_line.split("__")[nb_tabs]
    
    if actual_line == "\n" or actual_line == "" or actual_line == " " or actual_line == "\t":
        pass
    
    if if_tab_lst == [] and nb_tabs > 0:
        pass
    
    elif actual_line.startswith("!si"):
        if_content = actual_line.split("!si ")[1]
        
        if "est egale a" in if_content:
            if_content = if_content.split(" est egale a ")
            if_compare1 = textType(if_content[0])
            if_compare2 = textType(if_content[1].split(" alors\n")[0])
            
            if if_compare1 == if_compare2:
                if_tab_lst += [True]
            else:
                if nb_tabs == 0:
                    if_tab_lst = []
                elif len(if_tab_lst) > 1:
                    if_tab_lst = [True for x in range(len(if_tab_lst)-1)]
                else:
                    if_tab_lst = []
        
        elif "est superieur a" in if_content:
            if_content = if_content.split(" est superieur a ")
            if_compare1 = textType(if_content[0])
            if_compare2 = textType(if_content[1].split(" alors\n")[0])
            
            if if_compare1 > if_compare2:
                if_tab_lst += [True]
            else:
                if nb_tabs == 0:
                    if_tab_lst = []
                elif len(if_tab_lst) > 1:
                    if_tab_lst = [True for x in range(len(if_tab_lst)-1)]
                else:
                    if_tab_lst = []
        
        elif "est inferieur a" in if_content:
            if_content = if_content.split(" est inferieur a ")
            if_compare1 = textType(if_content[0])
            if_compare2 = textType(if_content[1].split(" alors\n")[0])
            
            if if_compare1 < if_compare2:
                if_tab_lst += [True]
            else:
                if nb_tabs == 0:
                    if_tab_lst = []
                elif len(if_tab_lst) > 1:
                    if_tab_lst = [True for x in range(len(if_tab_lst)-1)]
                else:
                    if_tab_lst = []
            
        
        # print("if1 =", if_compare1, "(" + str(type(if_compare1)) + ")", "if2 =", if_compare2, "(" + str(type(if_compare2)) + ")") # debug
        
            
    elif if_tab_lst == [] and nb_tabs > 0:
        # print('pass') # debug
        pass
    
    else:
        if actual_line.startswith("/"):
            cut = actual_line.split("/")
            # print(str(cut)) # debug
            
            variable = cut[1]
            content = textType(cut[2].split("\n")[0])
            
            vars_lst += [variable, content]
        
        elif "!afficher " in actual_line:
            # print(vars_lst) # debug
            print_content = actual_line.split("!afficher ")[1]
            print_content = print_content.split("\n")[0]
            # print("\"" + str(print_content) + "\"") # debug
            
            if print_content in vars_lst:
                print_content_index = vars_lst.index(print_content) + 1
                # print(str(True), print_content_index) # debug
                print(vars_lst[print_content_index])
                
                del(print_content_index)
            else:
                print(actual_line.split("!afficher ")[1], end='')
            
            del(print_content)

    if first_line == True:
        first_line = False
    
    # print("[after] if tab lst =", if_tab_lst)