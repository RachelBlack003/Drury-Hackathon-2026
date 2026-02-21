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