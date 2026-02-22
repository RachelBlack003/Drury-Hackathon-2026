from pathlib import Path



class Question_Text_handler:
    def __init__(self, filepath):
        script_location = Path(__file__).parent
        introduction_path = script_location / "dialog" / filepath / "introduction.txt"
        pass_path = script_location / "dialog" / filepath / "pass.txt"
        fail_path = script_location / "dialog" / filepath / "fail.txt"

        self.introduction_file = open(introduction_path, 'r', encoding='utf-8')
        self.pass_file = open(pass_path, 'r', encoding='utf-8')
        self.fail_file = open(fail_path, 'r', encoding='utf-8')

        self.introduction_lines = self.introduction_file.readlines()
        self.pass_lines = self.pass_file.readlines()
        self.fail_lines = self.fail_file.readlines()
        if len(self.introduction_lines) > 0:
            self.current_text = [self.introduction_lines, 0]
        else:
            self.current_text = [["---NO TEXT PRESENT---"],0]
        #Spacebar will be used to go to the next dialog option. If the box is
        #active, then it will do it. Otherwise, it won't.
        self.active = True

    
    def next(self):
        if self.active:
            if self.current_text[1] + 1 < len(self.current_text[0]):
                self.current_text[1] += 1
                return self.get_text(), True
            else:
                self.active = False
                return None, False
            
    def win(self):
        if len(self.pass_lines) > 0:
            self.current_text = [self.pass_lines, 0]
        else:
            self.current_text = [["---NO TEXT PRESENT---"],0]
        self.active = True
        return self.get_text()

    def lose(self):
        if len(self.fail_lines) > 0:
            self.current_text = [self.fail_lines, 0]
        else:
            self.current_text = [["---NO TEXT PRESENT---"],0]
        self.active = True
        return self.get_text()
    
    def get_text(self):
        return self.current_text[0][self.current_text[1]]
    
    def is_active(self):
        return self.active

    

class Indroduction_Text_handler:
    def __init__(self):
        script_location = Path(__file__).parent
        self.test_text_path = script_location / "dialog" / "testText.txt"
        self.test_file = open(self.test_text_path, 'r', encoding='utf-8')
        self.test_lines = self.test_file.readlines()

class Ending_Text_handler:
    def __init__(self):
        script_location = Path(__file__).parent
        self.test_text_path = script_location / "dialog" / "testText.txt"
        self.test_file = open(self.test_text_path, 'r', encoding='utf-8')
        self.test_lines = self.test_file.readlines()