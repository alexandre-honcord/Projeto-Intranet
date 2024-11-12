import logging
from ldap3 import Server, Connection, ALL
import cx_Oracle
import base64
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def exists_ad(username, password):
    ldap_server = 'ldap://10.0.1.253'
    ldap_port = 389 
    ldap_user = f'{username}@honcord.local'
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
    
def buscar_dados_usuario(username):
    dsn_tns = cx_Oracle.makedsn('10.0.1.12', '1521', service_name='dbprod')
    connection = cx_Oracle.connect(user='AUGUSTO', password='Mudar@123', dsn=dsn_tns)
    cursor = connection.cursor()

    query = """
        SELECT cd_pessoa_fisica as IDtasy, TASY.OBTER_NOME_PF(cd_pessoa_fisica) as name, im_pessoa_fisica as foto
        FROM TASY.PESSOA_FISICA_FOTO
        WHERE nm_usuario = :username
    """
    
    cursor.execute(query, username=username)
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        idtasy, name, foto = result
        foto_base64 = base64.b64encode(foto).decode('utf-8') if foto else None
        return {'IDtasy': idtasy, 'name': name, 'foto': foto_base64}
    return None


from datetime import datetime, timedelta

def format_duration(dataAbertura, dataFim=None):
    dataFim = dataFim or datetime.now()
    duracao = dataFim - dataAbertura

    if duracao < timedelta(days=1):
        horas_totais = int(duracao.total_seconds() // 3600)
        minutos = int((duracao.total_seconds() % 3600) // 60)

        if horas_totais > 0:
            return f"{horas_totais}h {minutos}min"
        elif minutos > 0:
            return f"{minutos}min"
        else:
            return "< 1 minuto"
    else:
        return f"{duracao.days} dias"

def categorize_os_details(resultados_os):
    os_abertas = []
    os_em_processo = []
    os_encerradas = []

    for sequencia, dataAbertura, descricao, dano, classificacao, dataFim, status, grupo in resultados_os:
        status = int(status)
        duracao_formatada = format_duration(dataAbertura, dataFim)
        
        os_data = {
            'sequencia': sequencia,
            'dataAbertura': dataAbertura,
            'descricao': descricao,
            'dano': dano,
            'classificacao': classificacao,
            'dataFim': dataFim,
            'duracao': duracao_formatada,
            'grupo': grupo
        }

        if status == 1:
            os_abertas.append(os_data)
        elif status == 2:
            os_em_processo.append(os_data)
        elif status == 3:
            os_encerradas.append(os_data)

    return os_abertas, os_em_processo, os_encerradas

def map_grupo_trabalho(grupo_planejamento):
    grupo_trabalho = {
        27: 19,
        21: 11,
        30: 74
    }
    return grupo_trabalho.get(grupo_planejamento, None)

def parse_request_data(request):
    try:
        grupo_planejamento = int(request.POST.get('ordem', 0))
        grupo_trabalho = request.POST.get('tipo_ordem')
        categoria = request.POST.get('classificacao_ordem')
        detalhes = request.POST.get('descricao_ordem')
        impacto = request.POST.get('dano_ordem')

        mapped_grupo_trabalho = map_grupo_trabalho(grupo_planejamento)
        if mapped_grupo_trabalho:
            grupo_trabalho = mapped_grupo_trabalho

        grupo_trabalho = int(grupo_trabalho)
        return grupo_planejamento, grupo_trabalho, categoria, detalhes, impacto
    except ValueError:
        return None, None, None, None, None
