import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def test_calculator_root_directory(self):
        """Test listing files in calculator root directory"""
        result = get_files_info("calculator", ".")
        lines = result.split("\n")

        expected_content = [
            ("tests.py", "is_dir=False"),
            ("main.py", "is_dir=False"),
            ("pkg", "is_dir=True"),
        ]

        self.assertEqual(len(lines), len(expected_content))
        for line, (filename, dir_status) in zip(lines, expected_content):
            self.assertIn(f"- {filename}: file_size=", line)
            self.assertIn(dir_status, line)
            self.assertRegex(line, r"^- .+: file_size=\d+ bytes, is_dir=(True|False)$")

    def test_calculator_pkg_directory(self):
        """Test listing files in calculator/pkg directory"""
        result = get_files_info("calculator", "pkg")
        lines = result.split("\n")

        expected_content = [
            ("render.py", "is_dir=False"),
            ("calculator.py", "is_dir=False"),
        ]

        self.assertEqual(len(lines), len(expected_content))
        for line, (filename, dir_status) in zip(lines, expected_content):
            self.assertIn(f"- {filename}: file_size=", line)
            self.assertIn(dir_status, line)
            self.assertRegex(line, r"^- .+: file_size=\d+ bytes, is_dir=(True|False)$")

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
