# use get_total_memory and compare it against result from psutils
# run it only if the it is windows os.name == "nt"
import os
def test_internal_windows_total_memory():
    if os.name == "nt":
        from tabpfn.utils import get_total_memory_windows
        import psutil
        utils_result = get_total_memory_windows()
        psutil_result = psutil.virtual_memory().total / 1e9
        assert utils_result == psutil_result

def test_internal_windows_total_memory_multithreaded():
    # collect results from multiple threads
    if os.name == "nt":
        from tabpfn.utils import get_total_memory_windows
        import psutil
        import threading
        results = []
        def get_memory():
            results.append(get_total_memory_windows())
        threads = []
        for _ in range(10):
            t = threading.Thread(target=get_memory)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        psutil_result = psutil.virtual_memory().total / 1e9
        assert all([result == psutil_result for result in results])