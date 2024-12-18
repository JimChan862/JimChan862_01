import os

import pytest

if __name__ == '__main__':
    pytest.main(['-sv','test_py4.py','--alluredir','./reslut','--clean-alluredir'])
    os.system('allure generate ./reslut -o ./reports --clean')