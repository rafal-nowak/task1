from datetime import datetime


class TestLogger:
    MAIN_TEST_LOG_FILE = "./test_results/test_summary.txt"
    DETAIL_TEST_LOG_FILE = "./test_results/test_details.txt"

    def __init__(self):
        self.results = dict()

    def log_single_test_result(self, test_name, passed):
        self.results[test_name] = passed

    def save_results(self):
        self.save_summary_result(TestLogger.MAIN_TEST_LOG_FILE)
        self.save_detailed_results(TestLogger.DETAIL_TEST_LOG_FILE)

    def save_summary_result(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            overall_test_result = not False in self.results.values()
            file.write(f"TASK COMPLETED: {overall_test_result}\n")
            passed_tests_count = sum(map((True).__eq__, self.results.values()))
            file.write(f"PASSED TESTS: {passed_tests_count} OF {len(self.results)}\n")

    def save_detailed_results(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            for key, value in self.results.items():
                file.write(f"{datetime.now()};{key};{value}\n")


if __name__ == '__main__':
    logger = TestLogger()
    logger.log_single_test_result("test1", True)
    # logger.log_single_test_result("test2", False)
    logger.log_single_test_result("test3", True)
    # logger.log_single_test_result("test4", False)
    logger.save_results()
