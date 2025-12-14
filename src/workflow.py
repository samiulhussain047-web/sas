import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger("SparxWorkflow")
logging.basicConfig(level=logging.INFO)


class SparxWorkflow:
    def __init__(self):
        self.driver = None

    def open_browser(self):
        options = Options()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        logger.info("Browser opened")

    def wait_for_manual_login(self):
        print("\n==============================")
        print("MANUAL LOGIN MODE")
        print("1. Log in to Sparx")
        print("2. Open the homework page")
        print("3. Make sure questions are visible")
        print("==============================\n")
        input("When ready, press ENTER to continue...")

    def run(self):
        try:
            self.open_browser()
            self.wait_for_manual_login()

            logger.info("Manual phase completed. Workflow ready.")
            print("\nBot is now idle. You can add logic here later.\n")

            # Keep browser open
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            logger.info("Stopped by user")

        except Exception as e:
            logger.exception(f"Workflow error: {e}")


def run_workflow():
    workflow = SparxWorkflow()
    workflow.run()
