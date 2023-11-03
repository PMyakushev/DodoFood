import multiprocessing
import subprocess

def run_program(file_name):
    subprocess.call(['python', file_name])

if __name__ == '__main__':
    # Создание пула процессов
    pool = multiprocessing.Pool(6)

    # Запуск трех файлов
    pool.map(run_program, ['ParsingPageStoreOne.py', 'ParsingPageStoreTwo.py', 'ParsingPageStoreThree.py', 'ParsingPageStoreSix.py', 'ParsingPageStoreFive.py', 'ParsingPageStoreFour.py'])
    # pool.map(run_program, ['ParsingPageStoreOne.py', 'ParsingPageStoreTwo.py', 'ParsingPageStoreThree.py'])
    # Ожидание завершения всех процессов
    pool.close()
    pool.join()