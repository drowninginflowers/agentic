import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


class TestGetFilesInfo(unittest.TestCase):
    def test_get_file_content(self):
        print(get_file_content("calculator", "main.py"))
        print(get_file_content("calculator", "pkg/calculator.py"))
        print(get_file_content("calculator", "/bin/cat"))
        print(get_file_content("calculator", "pkg/does_not_exist.py"))

    def test_absolute_path_outside_directory(self):
        """Test that absolute paths outside the base directory are rejected"""
        expected_result = (
            'Error: Cannot list "/bin" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, expected_result)

    def test_relative_path_outside_directory(self):
        """Test that relative paths outside the base directory are rejected"""
        expected_result = (
            'Error: Cannot list "../" as it is outside the permitted working directory'
        )
        result = get_files_info("calculator", "../")
        self.assertEqual(result, expected_result)

    def test_nonexistent_base_directory(self):
        """Test behavior with non-existent base directory"""
        result = get_files_info("nonexistent_directory", ".")
        self.assertTrue(
            result.startswith('Error: "nonexistent_directory" is not a directory')
        )

    def test_nonexistent_relative_path(self):
        """Test behavior with non-existent relative path"""
        result = get_files_info("calculator", "nonexistent_subdir")
        self.assertTrue(
            result.startswith('Error: "nonexistent_subdir" is not a directory')
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
