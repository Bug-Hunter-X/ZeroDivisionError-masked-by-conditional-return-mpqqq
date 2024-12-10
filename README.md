# ZeroDivisionError masked by conditional return

This example demonstrates a subtle bug in Python where a `ZeroDivisionError` is masked by a conditional return statement that seems to handle the problematic case, but fails to do so properly. The error is not immediately apparent and can be hard to debug.

The `bug.py` file contains the buggy code. The `bugSolution.py` file contains the corrected version of the function that explicitly addresses the possibility of zero values, preventing the error.