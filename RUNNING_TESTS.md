## Running Tests

To ensure the correctness of the implementation, unit tests have been provided. These tests can be executed using the `unittest` framework in Python.

### Running Tests from the Command Line

1. Open a terminal or command prompt.
2. Navigate to the root directory of the project where `test.py` is located.
3. Run the following command to discover and run all tests:

    ```sh
    python -m unittest discover
    ```

The unit tests cover various scenarios including:

- Scanning a single item.
- Scanning multiple items without any offers.
- Scanning multiple items with applicable offers.
- Calculating the total price for a mixture of items with and without offers.

### Example Test Output

Running the tests should provide output similar to the following:

```sh
$ python -m unittest discover
...
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK