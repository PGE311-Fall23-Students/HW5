# Required packages
import unittest
import nbconvert

# Assignment-specific packages
import numpy as np
import pandas as pd
# Convert the assignment Jupyter notebooks into something we can import
with open("HW5.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("HW5.py", "w") as f:
    f.write(python_file)

# Import the converted file. Best to import only the variables you want to test
from HW5 import monthly_payment, sine_approximate, lettergrade, square_root, v

# Here is where you will write your tests
class TestSolution(unittest.TestCase):
    # You can fill this out if you are testing functions/classes, or want private tests
    # The name must be setUp(self)

    def setUp(self):
        pass

    # All tests need to start with "test_..."
    def test_q1(self):
        # Numpy has an extensive test suite.
        # It's best to use allclose instead of equal to avoid problems with machine precision
        np.testing.assert_allclose(monthly_payment(40000, 5.3, 36), 1204.2310458682666, rtol=1e-5)
        return


    def test_q2(self):
        # It also works if testing an array
        # You can write the solution yourself as follows. But students will be able to see your solution

        np.testing.assert_allclose(sine_approximate(0.9,8), 0.783326909627483, rtol=1e-5)
        return
        
    def test_q3(self):
        # It also works if testing an array
        # You can write the solution yourself as follows. But students will be able to see your solution
        
        np.testing.assert_string_equal(lettergrade(90), 'A')
        return

        
    def test_q4(self):
        # Instead, it's better to hardcode the solution if possible
        
        np.testing.assert_allclose(square_root(56, 1e-6), 7.4833147735478995, rtol=1e-5)
        return
        
    def test_q5(self):
        # Instead, it's better to hardcode the solution if possible
        t = np.linspace(-5,50)
        np.testing.assert_allclose(v(t[26]), 1674.2823823406907, rtol=1e-5)
        return
        


if __name__ == "__main__":
    tester = unittest.main(verbosity=2, exit=False)

    # Count number of total tests
    total_tests = tester.result.testsRun

    # Number of failed, errors, and skipped tests
    num_failures = len(tester.result.failures)
    num_errors = len(tester.result.errors)
    num_skipped = len(tester.result.skipped)

    # Final student score
    student_score = total_tests - (num_failures + num_errors + num_skipped)
    print(f"Score: {student_score}/{total_tests}")

    # Write student score to Pandas dataframe
    score_df = pd.DataFrame(
        {
            "Total Tests": total_tests,
            "Number of Test Failures": num_failures,
            "Number of Test Errors": num_errors,
            "Number of Skipped Tests": num_skipped,
            "Student Score": student_score,
        }, index=[0])

    # Write dataframe to csv
    score_df.to_csv("student_score.csv", index=False)
