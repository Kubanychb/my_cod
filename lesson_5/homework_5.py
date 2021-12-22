import re
class Text:
    def __init__(self, file_text, results_file_text, searcher):
        self.file_text = file_text
        self.results_file_text = results_file_text
        self.searcher = searcher

    def parsing(self):
        file_reader = open(self.file_text, mode="r")
        final_results = open(self.results_file_text, mode="w")
        class_file = file_reader.read()
        results_all = re.findall(self.searcher,class_file)

        for i in results_all:
            print(i)
            final_results.write(i + "\n")
        return (f"Total:{str(len(results_all))}")

file_1 = Text(file_text="MOCK_DATA", results_file_text="name_file",searcher=r"[A-Z].-\w+\s\w+|[A-Z]\w+\s[A-Z]\w+.\s|.+[A-Z]\w+\s")
print(file_1.parsing())

file_2 = Text(file_text="MOCK_DATA",results_file_text="mail_file",searcher=r"\w+@\w+.\w+")
print(file_2.parsing())

file_3 = Text(file_text="MOCK_DATA",results_file_text="extension", searcher=r"[A-Z]\w+[.]\w+\s|[A-Z][[.]\w+\s")
print(file_3.parsing())


file_4 = Text(file_text="MOCK_DATA",results_file_text="color_code",searcher=r"#\w+")
print(file_4.parsing())

