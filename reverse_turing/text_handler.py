from pathlib import Path



class Text_handler:
    def __init__(self):
        script_location = Path(__file__).parent
        self.test_text_path = script_location / "dialog" / "testText.txt"
        self.test_file = open(self.test_text_path, 'r', encoding='utf-8')
        self.test_lines = self.test_file.readlines()
