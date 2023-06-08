import sys

ishile = False
RED = "\033[91m"
GREEN = "\033[32m"
WHITE = "\033[0m"

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    try:
        with open(file_name, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(RED + "not founded file:", file_name + WHITE)
        sys.exit(5)
    except Exception as e:
        print(RED + "An error occurred:", e, WHITE)
        sys.exit(1)
    res = []
    if "print(" in code or "input(" in code:
        res.append("using System;")
    res += ["namespace csp{", "    class prog{", "        static void Main(){"]
    for line in code.splitlines():
        if "print(" in line:
            line = line.replace('",', ' " +')
            line = line.replace("',", " ' +")
            line = line.replace('f"', '$"')
            line = line.replace("f'", "$'")
            line = line.replace("print", "            Console.WriteLine", 1) + ";"
        elif "while " in line:
            line = line.replace("True", "true")
            line = line.replace(":", "")
            line = line.replace("while ", "", 1)
            line = "(" + line + ") { "
            line = "        while " + line

        elif line.endswith("endwhile") == True:
            line = "}"
        elif line.endswith("endif") == True:
            line = "}"

        elif "if " in line:
            line = line.replace("if ", "", 1)
            line = line.replace(":", "")
            line = line.replace("and", "&&")
            line = line.replace("or", "||")
            line = "(" + line + ")"
            line = "if " + line + "{"


        elif "input(" in line:
            saveline = line
            totwo = saveline.find('"')
            tone = saveline.rfind('"')
            saveline = saveline.replace(saveline[:totwo - 1], '', 1)
            saveline = saveline.replace(saveline[tone:], '', 1)
            saveline = saveline.replace('f"', '$"')
            saveline = saveline.replace("f'", "$'")
            saveline = saveline.replace("(", "")
            saveline = saveline.replace(")", "")
            if saveline == "":
                saveline = '""'
            saveline = saveline.replace('f"', '@"')
            saveline = saveline.replace("f'", "@'")
            saveline = saveline.replace('",', ' " +')
            saveline = saveline.replace("', ", " ' +")
            saveline = "            Console.Write(" + '"" + ' + saveline + ")" + "; "
            line = line + ";"
            find = line.find('"')
            line = line[:find - 1]
            line = line.replace('"', "", 1)
            line = line.replace('(', "", 1)
            line = line.replace(')', "", 1)
            line = line.replace("'", "", 1)
            line = line.replace('input', "Console.ReadLine()", 1)
            if "=" in line:
                isvar = 1
            else:
                isvar = 0
            line = line.replace(saveline, "", 1)
            line = line.replace('', "", 1)
            if isvar == 1:
                line = saveline + "string " + line + ";"
            else:
                line = saveline + line + ";"
        else:
            if "=" in line:
                if '"' in line or "'" in line:
                    line = line.replace("'", '"')
                    line = "        string " + line + ";"
                elif "." in line:
                    line = "        double " + line + ";"
                else:
                    line = "        int " + line + ";"
        res.append(line)
    type = file_name.rfind(".")
    file_name = file_name.replace(file_name[type:], "", 1)
    res += ["        }", "    }", "}"]
    with open(file_name + ".cs", "w") as f:
        f.write("\n".join(res))
    print(GREEN + "successfully compiled" + WHITE)
else:
    print(RED + "csp need get 1 argument the (FILE)" + WHITE)
