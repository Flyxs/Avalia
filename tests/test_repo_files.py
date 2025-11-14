# tests/test_repo_files.py
import os

def test_env_example_exists():
    assert os.path.isfile(".env.example"), ".env.example must exist in repo root"

def test_requirements_txt_exists():
    assert os.path.isfile("requirements.txt"), "requirements.txt must exist"
