import re

file_text = "MOCK_DATA"
results_file_text = "name_file"
file_reader = open(file_text, mode="r")
final_results = open(results_file_text, mode="w")


class_file = file_reader.read()
searcher = r"[A-Z]\w+\s[A-Z]\w+\s|[A-Z]\w+\s.+|[A-Z]\w+\s"
results_all = re.findall(searcher, class_file)

for i in results_all:
    print(i)
    final_results.write(i + "\n")
print(f"Total: {str(len(results_all))}")


results_file_text_1 = "mail_file"
file_reader_1 = open(file_text, mode="r")
final_results_1 = open(results_file_text_1, mode="w")
class_file_1 = file_reader_1.read()
searcher_1 = r"\w+@\w+.\w+"
results_all_1 = re.findall(searcher_1,class_file_1)

for j in results_all_1:
    # print(j)
    final_results_1.write(j + "\n")
# print(f"Total: {str(len(results_all_1))}")

results_file_text_2 = "extension"
file_reader_2 = open(file_text, mode="r")
final_results_2 = open(results_file_text_2, mode="w")
class_file_2 = file_reader_2.read()
searcher_2 = r"[A-Z]+.[a-z]+"
results_all_2 = re.findall(searcher_2, class_file_2)

for l in results_all_2:
    # print(l)
    final_results_2.write(l + "\n")
# print(f"Total: {str(len(results_all_2))}")

results_file_text_3 = "color_code"
file_reader_3 = open(file_text, mode="r")
final_results_3 = open(results_file_text_3, mode="w")
class_file_3 = file_reader_3.read()
searcher_3 = r"#\w+"
results_all_3 = re.findall(searcher_3, class_file_3)

for k in results_all_3:
    # print(k)
    final_results_3.write(k + "\n")
# print(f"Total:{str(len(results_all_3))}")


