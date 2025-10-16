import sys
import re


class TextToPythonInterpreter:
    """Interpreteur pour le langage Text to Python"""
    
    def __init__(self):
        self.variables = {}
        self.condition_stack = []
        self.should_execute = True
        self.stopped = False
        self.else_executed = set()  # Track which conditions have had their else executed
        
    def parse_value(self, text):
        """Convertit un texte en valeur (int ou str)"""
        text = text.strip()
        if text.startswith("^^"):
            try:
                return int(text[2:])
            except ValueError:
                print(f"Erreur: '{text}' n'est pas un nombre valide")
                return 0
        elif text in self.variables:
            return self.variables[text]
        else:
            return text
    
    def get_indentation_level(self, line):
        """Compte le niveau d'indentation (nombre de __)"""
        count = 0
        while line.startswith("__"):
            count += 1
            line = line[2:]
        return count, line
    
    def evaluate_condition(self, line):
        """Evalue une condition (!si)"""
        line = line.strip()
        if not line.startswith("!si "):
            return None
            
        condition = line[4:]
        if " alors" in condition:
            condition = condition.replace(" alors", "")
        condition = condition.strip()
        
        # Detecter le type de comparaison
        if " est egale a " in condition:
            parts = condition.split(" est egale a ")
            if len(parts) == 2:
                val1 = self.parse_value(parts[0].strip())
                val2 = self.parse_value(parts[1].strip())
                return val1 == val2
        elif " est superieur a " in condition:
            parts = condition.split(" est superieur a ")
            if len(parts) == 2:
                val1 = self.parse_value(parts[0].strip())
                val2 = self.parse_value(parts[1].strip())
                try:
                    return val1 > val2
                except TypeError:
                    return False
        elif " est inferieur a " in condition:
            parts = condition.split(" est inferieur a ")
            if len(parts) == 2:
                val1 = self.parse_value(parts[0].strip())
                val2 = self.parse_value(parts[1].strip())
                try:
                    return val1 < val2
                except TypeError:
                    return False
        
        return False
    
    def execute_line(self, line, indent_level):
        """Execute une ligne de commande"""
        line = line.strip()
        
        if not line or line == "\n":
            return
        
        # Commande d'arret
        if line.startswith("!stop"):
            self.stopped = True
            return
        
        # Gestion des conditions
        if line.startswith("!si "):
            result = self.evaluate_condition(line)
            self.condition_stack.append({
                'level': indent_level, 
                'condition_result': result,  # Original condition result
                'in_else': False             # Are we in the else block?
            })
            return
        
        # Gestion du sinon (else)
        if line.startswith("!sinon"):
            if self.condition_stack and self.condition_stack[-1]['level'] == indent_level:
                # Mark that we're now in the else block
                self.condition_stack[-1]['in_else'] = True
            return
        
        # Verifier si on doit executer (selon les conditions)
        should_execute = True
        for cond in self.condition_stack:
            if cond['level'] >= indent_level:
                break
            
            # Logic: execute if (condition is true AND not in else) OR (condition is false AND in else)
            if cond['in_else']:
                # We're in an else block, so execute only if condition was false
                if cond['condition_result']:
                    should_execute = False
                    break
            else:
                # We're in an if block, so execute only if condition was true
                if not cond['condition_result']:
                    should_execute = False
                    break
        
        if not should_execute:
            return
        
        # Declaration de variable
        if line.startswith("/") and line.count("/") >= 2:
            parts = line.split("/")
            if len(parts) >= 3:
                var_name = parts[1]
                var_value = self.parse_value(parts[2])
                self.variables[var_name] = var_value
        
        # Affichage
        elif line.startswith("!afficher "):
            content = line[10:].strip()
            value = self.parse_value(content)
            print(value)
        
        # Operations arithmetiques
        elif line.startswith("!calculer "):
            expr = line[10:].strip()
            try:
                # Remplacer les variables par leurs valeurs
                for var_name, var_value in self.variables.items():
                    expr = expr.replace(var_name, str(var_value))
                # Evaluer l'expression
                result = eval(expr)
                print(result)
            except Exception as e:
                print(f"Erreur de calcul: {e}")
    
    def run_file(self, filename):
        """Execute un fichier Text to Python"""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Erreur: Le fichier '{filename}' n'existe pas")
            return
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier: {e}")
            return
        
        i = 0
        while i < len(lines):
            if self.stopped:
                break
            
            line = lines[i]
            
            # Obtenir le niveau d'indentation
            indent_level, clean_line = self.get_indentation_level(line)
            
            # Check if next non-empty line is !sinon at the same level
            is_before_sinon = False
            if i + 1 < len(lines):
                next_indent, next_clean = self.get_indentation_level(lines[i + 1])
                if next_clean.strip().startswith("!sinon") and next_indent == indent_level:
                    is_before_sinon = True
            
            # Nettoyer la pile de conditions selon l'indentation
            # On garde seulement les conditions qui sont a un niveau inferieur
            while self.condition_stack and self.condition_stack[-1]['level'] >= indent_level:
                # Don't pop if this is a !sinon and there's a condition at the same level
                if clean_line.strip().startswith("!sinon") and self.condition_stack and self.condition_stack[-1]['level'] == indent_level:
                    break
                # Don't pop if the next line is !sinon at same indent level
                if is_before_sinon and self.condition_stack[-1]['level'] == indent_level:
                    break
                self.condition_stack.pop()
            
            # Executer la ligne
            try:
                self.execute_line(clean_line, indent_level)
            except Exception as e:
                print(f"Erreur ligne {i+1}: {e}")
            
            i += 1


def main():
    """Point d'entree principal"""
    # Determiner le fichier a executer
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "./past-your-script-here.txt"
    
    # Creer et lancer l'interpreteur
    interpreter = TextToPythonInterpreter()
    interpreter.run_file(filename)


if __name__ == "__main__":
    main()