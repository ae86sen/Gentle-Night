
import os
import shutil

import pytest
import pytest_rerunfailures
from common.constants import ALLURE_DIR
# shutil.rmtree(ALLURE_DIR)
# pytest.main(['-m zls','-s'])
pytest.main(['-s','--reruns','1','--reruns-delay','10',r'--alluredir=alluredir/',"--clean-alluredir"])
# os.system('allure generate ./alluredir -o ./allure-report --clean')
