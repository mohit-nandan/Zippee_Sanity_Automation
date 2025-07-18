import os
import subprocess
import datetime
import sys
import shutil
import webbrowser
import time

# --- Configuration Paths ---
# Get the root directory of the project (where this script is located)
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Directory for raw Allure results (JSON/XML files)
# This directory will be cleaned before each run to ensure fresh results.
ALLURE_RESULTS_DIR = os.path.join(ROOT_DIR, "reports", "allure-results")

# Base directory where all generated HTML reports will be stored.
# Each test run will create a new, uniquely timestamped subfolder within this base.
HTML_REPORTS_BASE_DIR = os.path.join(ROOT_DIR, "reports", "html-reports")

# Generate a unique timestamp for the current test run.
# This ensures each generated HTML report gets its own distinct folder.
TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define the specific directory for the HTML report of this current run.
CURRENT_HTML_REPORT_DIR = os.path.join(HTML_REPORTS_BASE_DIR, f"report_{TIMESTAMP}")

# --- Pre-run Setup & Cleanup ---
print("--- Test Run Setup ---")

# Clean the raw Allure results directory. This is a failsafe;
# --clean-alluredir in pytest_cmd also handles this.
if os.path.exists(ALLURE_RESULTS_DIR):
    print(f"Cleaning previous raw Allure results from: {ALLURE_RESULTS_DIR}")
    shutil.rmtree(ALLURE_RESULTS_DIR)
# Create the directory to store new raw Allure results.
os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)

# Ensure the base directory for storing all historical HTML reports exists.
os.makedirs(HTML_REPORTS_BASE_DIR, exist_ok=True)

# --- Run Pytest Tests ---
pytest_cmd = [
    sys.executable,        # Uses the Python executable from the active environment
    "-m", "pytest",        # Runs pytest as a module
    "tests/",              # Tells pytest where your test files are located
    f"--alluredir={ALLURE_RESULTS_DIR}", # Specifies where Allure raw results should be saved
    "--clean-alluredir"    # Ensures the allure results directory is empty before starting tests
]
print(f"\n▶️ Running tests:\n{' '.join(pytest_cmd)}\n")

try:
    # Execute the pytest command.
    # 'check=True' will raise a CalledProcessError if pytest returns a non-zero exit code (i.e., if tests fail).
    subprocess.run(pytest_cmd, check=True)
    print("\n✅ Pytest tests executed successfully (all passed or some failed as expected).")
except subprocess.CalledProcessError as e:
    # This block is executed if any test fails, or if pytest itself encounters an error.
    print(f"❌ Pytest command failed with error: {e}")
    print("Some tests might have failed. Proceeding to generate report with available results.")
    # If you want the script to stop immediately if tests fail, uncomment the line below:
    # sys.exit(1)

# --- Generate Allure HTML Report ---
# Give a small delay to ensure all test result files are completely written to disk.
time.sleep(1)

# Construct the command for allure generate as a single string.
# Using shell=True for 'allure' commands as it appears more reliable in your environment.
generate_cmd_str = f"allure generate \"{ALLURE_RESULTS_DIR}\" -o \"{CURRENT_HTML_REPORT_DIR}\" --clean"
print(f"\n📊 Generating HTML report in: {CURRENT_HTML_REPORT_DIR}\n")

try:
    # Execute the allure generate command using shell=True
    subprocess.run(generate_cmd_str, shell=True, check=True)
    print("\n✅ Allure HTML report generated successfully.")
except subprocess.CalledProcessError as e:
    print(f"\n❌ Allure report generation failed with error: {e}")
    sys.exit(1) # Exit if Allure generation command fails.
except Exception as e: # Catch any other unexpected errors during shell execution
    print(f"\n❌ An unexpected error occurred during Allure report generation: {e}")
    print("Please ensure 'allure' is correctly installed and accessible via your system's shell.")
    sys.exit(1)

# --- Open Report in Browser ---
index_path = os.path.join(CURRENT_HTML_REPORT_DIR, "index.html")
if os.path.exists(index_path):
    print(f"\n🌐 Attempting to open Allure report in default browser: {index_path}")
    webbrowser.open(index_path)
    print("Note: Browser security settings might prevent direct local HTML files")
    print("from fully loading. If the report shows 'Loading...', please use:")
    print(f"  cd \"{CURRENT_HTML_REPORT_DIR}\"")
    print(f"  allure serve .")
else:
    print(f"\n⚠️ Warning: index.html not found at {index_path}. Report might not have generated correctly.")

print("\n--- Test Run Complete ---")