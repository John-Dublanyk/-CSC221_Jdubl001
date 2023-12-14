from broken_final import min_max_sum_fixed, primes_sieve
import pytest

def test_min_max_sum_fixed():
    assert min_max_sum_fixed(1, 2, 3) == (1, 3, 6)
    assert min_max_sum_fixed(10, 20, 30) == (10, 30, 60)

def test_primes_sieve():
    assert primes_sieve(10) == [2, 3, 5, 7]
    assert primes_sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

"""
____________________________________________________________________________________ ERROR collecting test_broken.py ____________________________________________________________________________________
..\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\_pytest\python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
..\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\_pytest\pathlib.py:567: in import_path
    importlib.import_module(module_name)
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1050: in _gcd_import
    ???
<frozen importlib._bootstrap>:1027: in _find_and_load
    ???
<frozen importlib._bootstrap>:1006: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:688: in _load_unlocked
    ???
..\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\_pytest\assertion\rewrite.py:178: in exec_module
    exec(co, module.__dict__)
test_broken.py:1: in <module>
    from broken_final import min_max_sum_fixed, primes_sieve
E     File "C:\Users\johnn\Downloads\broken_final.py", line 12
E       return [x for x i primes if x]
E                     ^^^
E   SyntaxError: invalid syntax. Perhaps you forgot a comma?
======================================================================================== short test summary info ========================================================================================
ERROR test_broken.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
======================================================
"""