import logging
from ldap3 import Server, Connection, ALL

logger = logging.getLogger(__name__)

def exists_ad(username, password):
    ldap_server = 'ldap://10.0.1.253'  # Substitua pelo endereço do servidor LDAP
    ldap_port = 389  # Porta LDAP padrão
    ldap_user = f'{username}@honcord.local'  # Substitua pelo seu nome de usuário LDAP
    ldap_password = password

    server = Server(ldap_server, port=ldap_port, get_info=ALL)

    try:
        conn = Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)
        
        if conn.bind():
            logger.info(f"Usuário {username} autenticado com sucesso via LDAP.")
            return {'username': username}
        else:
            logger.error(f"Autenticação LDAP falhou para usuário {username}: {conn.result}")
            return None

    except Exception as e:
        logger.error(f"LDAP authentication failed for user {username}: {e}")
        return None
