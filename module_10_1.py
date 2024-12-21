import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


# Измерение времени выполнения последовательных вызовов функций
start_time = time.time()

for count, filename in [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]:
    write_words(count, filename)

end_time = time.time()
print(f'Работа функций заняла: {end_time - start_time:.6f} секунд')

# Измерение времени выполнения потоков
start_threads = time.time()

threads = []
for count, filename in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = Thread(target=write_words, args=(count, filename))
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

end_threads = time.time()
print(f'Работа потоков заняла: {end_threads - start_threads:.6f} секунд')
