import multiprocessing
import sys

def search_keyword_in_file(keyword, filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if keyword in line:
                print(f"Ключевое слово '{keyword}' найдено в файле {filename}")
                break

def main(keyword, file_list):
    processes = []
    for file in file_list:
        p = multiprocessing.Process(target=search_keyword_in_file, args=(keyword, file))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Задайте ключевые слова и имя файла через командную строку: python multiproccessing.py <ключевое_слово> <файл1> ")
    else:
        try:
            keyword = sys.argv[1]
            files = sys.argv[2:]
            main(keyword, files)
        except Exception as e:
            print(f"Произошла ошибка: {e}")