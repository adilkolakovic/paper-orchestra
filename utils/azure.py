import os
from functools import lru_cache

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


@lru_cache(maxsize=1)
def _get_secret_client() -> SecretClient:
    vault_url = os.getenv("KEYVAULT_URL") or (
        "https://kv-portal-new.vault.azure.net/"
    )
    return SecretClient(
        vault_url=vault_url,
        credential=DefaultAzureCredential(),
    )


def get_secret(name: str) -> str:
    value = _get_secret_client().get_secret(name).value
    if not value:
        raise ValueError(f"Key Vault secret '{name}' is empty.")
    return value
