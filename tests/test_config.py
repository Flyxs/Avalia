# tests/test_config.py
import os
from aval_mds_utils.config import load_env, is_ai_enabled

def test_load_env_returns_dict():
    env = load_env()
    assert isinstance(env, dict)
    assert "GH_TOKEN" in env
    assert "OPENAI_API_KEY" in env

def test_is_ai_enabled_false_by_default(tmp_path, monkeypatch):
    # garante que sem OPENAI_API_KEY e sem DISABLE_AI -> False
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("DISABLE_AI", raising=False)
    env = load_env()
    assert is_ai_enabled(env) is False
