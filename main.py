file = open("./past-your-script-here.txt", "r")
lines_lst = file.readlines()
vars_lst = []

for loop in range(len(lines_lst)):
    actual_line = lines_lst[loop]
    # print(str(actual_line)) # debug
    if actual_line == "\n" or actual_line == "" or actual_line == " ":
        pass
    elif "!afficher " in actual_line:
        print_content = actual_line.split("!afficher ")[1]
        
        if print_content in vars_lst:
            print_content_index = vars_lst.index(print_content) + 1
            # print(print_content_index) # debug
            print(vars_lst[print_content_index])
        else:
            print(actual_line.split("!afficher ")[1])
    elif "/" in actual_line:
        cut = actual_line.split("/")
        variable = cut[0]
        content = cut[1].split("\n")[0]
        
        vars_lst += [variable, content]
        
        # print(str(vars_lst)) # debug
    elif "!si" in actual_line:
        if_content = actual_line.split("!si ")
        if_content = if_content[1].split(" est ")
        
        if_compare1 = None
        if_compare2 = None
        
        print(if_content) # debug
        if if_content[0] in vars_lst:
            if_content_index = vars_lst.index(if_content[0]) + 1
            print(if_content, if_content_index) # debug
            if_compare1 = vars_lst[vars_lst.index(if_content[0]) + 1]
        else:
            if_compare1 = if_content[0]
        print(if_compare1) # debug