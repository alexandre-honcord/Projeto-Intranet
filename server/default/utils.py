import logging
from ldap3 import Server, Connection, ALL
import cx_Oracle
import base64

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
    
def buscar_foto_usuario(username):
    # Configurar a conexão manual ao banco Oracle
    dsn_tns = cx_Oracle.makedsn('10.0.1.12', '1521', service_name='dbprod')  # Verifique a porta e service_name
    connection = cx_Oracle.connect(user='AUGUSTO', password='Mudar@123', dsn=dsn_tns)
    cursor = connection.cursor()
    
    # Consulta para buscar o código hexadecimal da foto
    cursor.execute('SELECT im_pessoa_fisica FROM TASY.PESSOA_FISICA_FOTO WHERE nm_usuario = :username', [username])
    
    row = cursor.fetchone()
    if row:
        foto_binaria = row[0]  # Os dados já são binários
        
        # Codificar a imagem em base64
        foto_base64 = base64.b64encode(foto_binaria).decode('utf-8')
        
        cursor.close()
        connection.close()
        
        return foto_base64
    else:
        cursor.close()
        connection.close()
        return None
