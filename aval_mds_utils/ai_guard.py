# aval_mds_utils/ai_guard.py
from typing import Any, Dict
import logging
from .config import load_env, is_ai_enabled

logger = logging.getLogger(__name__)

def get_ai_client() -> Dict[str, Any]:
    """
    Retorna um objeto "cliente" mínimo: se não houver OPENAI_API_KEY, retorna um cliente de mock.
    A vantagem é que o resto do código pode chamar generate_text(...) com segurança.
    """
    env = load_env()
    enabled = is_ai_enabled(env)
    if not enabled:
        logger.warning("OpenAI not configured or disabled: running in mock mode.")
        return {"type": "mock", "key": None}
    # Se houver chave, ainda assim não chamamos a API aqui (para evitar dependências/segredos em testes).
    # O cliente retornado indica que a chave existe — o código que consumir pode decidir como proceder.
    return {"type": "real", "key": env.get("OPENAI_API_KEY")}

def generate_text(prompt: str, client: Dict[str, Any]) -> str:
    """
    Gera texto via OpenAI se client['type']=="real". Em modo mock, retorna string simulada.
    Este comportamento permite rodar o projeto sem a OpenAI.
    """
    if client.get("type") == "mock":
        # resposta de teste/controlada
        return f"[MOCK] resposta para: {prompt}"
    # Em ambiente real, aqui vocês podem integrar com openai.OpenAI(...) ou outra lib.
    # Para não criar dependência direta neste PR, apenas devolvemos uma placeholder.
    key = client.get("key")
    if not key:
        return f"[MOCK] resposta (sem chave) para: {prompt}"
    # Se quiserem, troquem a linha abaixo pela chamada real à API usando a key.
    return f"[REAL-PLACEHOLDER] (OpenAI key presente) resposta para: {prompt}"
