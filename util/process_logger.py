from multiprocessing import current_process


def log(level, message):
    current_process_name = current_process().name
    print('[{0} : {1}] {2}'.format(level, current_process_name, message))
