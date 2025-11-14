# aval_mds_utils/config.py
import os
from typing import Dict

def load_env() -> Dict[str, str]:
    """
    Carrega variáveis de ambiente relevantes do projeto e retorna um dicionário.
    Não lança se as variáveis estiverem ausentes — apenas retorna valores vazios.
    """
    return {
        "GH_TOKEN": os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_API_KEY") or "",
        "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY") or os.environ.get("OPENAI_KEY") or "",
        "DISABLE_AI": os.environ.get("DISABLE_AI", "0"),
    }

def is_ai_enabled(env: Dict[str, str]) -> bool:
    """
    Decide se a análise AI deve rodar.
    Retorna False se DISABLE_AI estiver ativado ou não houver OPENAI_API_KEY.
    """
    if str(env.get("DISABLE_AI", "0")).lower() in ("1", "true", "yes"):
        return False
    if not env.get("OPENAI_API_KEY"):
        return False
    return True
