def unsafe_file_execution(file_path):
    with open(file_path, "exec") as file:
        content = file.read()

        return content


def dummy_thread_sleep():
    import time

    time.sleep(5)
