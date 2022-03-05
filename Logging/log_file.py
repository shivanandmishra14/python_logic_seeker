import logging
# from test_Cases.test_login import *
# from test_Cases.test_home_page import *
# from test_Cases.test_signup import *
# from test_Cases.test_contact import *
from test_Cases.test_validate_home_footer import *

logging.basicConfig(filename="..//Logging//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s')
# level=logging.DEBUG

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.ERROR)


logger.debug("Debug Detail")
logger.info("Info Detail")
logger.warning("Warning Detail")
logger.error("Error Detail")
logger.critical("Critical Detail")

# SDET_QA Automation Techie Selenium with Python Tutorial 29-Logging | Generate log file
# cat test.log
# tail -f test.log
