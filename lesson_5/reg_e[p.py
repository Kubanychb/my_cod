import re


my_text = "Vasya 1964 vasya@gmail.com %1000$ " \
          "Adilet 1997 adilet@intel.com %3000$ " \
          "Aidana 2000 aidana@yandex.com %6987$ " \
          "Akylbek 1998 akilbek@gmail.com &6754$ " \
          "Aman 1999 aman@pixel.com *7654$ "
"""
\d = 0-9 Any digit 
\D = Any no digit
\w = [A - Z a - z ]
\W = non alphabet symbol 
\s = breakspace 
\S = Non breakspace 
"""

file_path = "class_mosk_data"
results_file_path = "results.txt"

file_reader = open(file_path, mode="r", encoding="Latin-1")
final_results = open(results_file_path, mode="w", encoding="Latin-1")

class_text = file_reader.read()


searcher = r"@\w+.\w+"
results_all = re.findall(searcher, class_text)

for item in results_all:
    print(item)
    final_results.write(item + "\n")
print(f"Total: {str(len(results_all))}")


