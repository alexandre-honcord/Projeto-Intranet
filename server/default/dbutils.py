import cx_Oracle
from django.conf import settings

def connect_to_db():
    # Extrai as configurações do banco de dados Oracle a partir do settings
    oracle_db = settings.DATABASES['oracle']
    
    dsn_tns = cx_Oracle.makedsn(
        host=oracle_db['HOST'],
        port=oracle_db['PORT'],
        service_name=oracle_db['NAME']
    )
    
    connection = cx_Oracle.connect(
        user=oracle_db['USER'],
        password=oracle_db['PASSWORD'],
        dsn=dsn_tns
    )
    
    return connection

def get_status_counts(solicitante_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = """
    SELECT 
        ie_status_ordem as status,
        COUNT(*) as quantidade
    FROM 
        TASY.MAN_ORDEM_SERVICO
    WHERE
        cd_pessoa_solicitante = :solicitante
    GROUP BY 
        ie_status_ordem
    """
    cursor.execute(query, {'solicitante': solicitante_id})
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()

    counts = {'abertas': 0, 'em_processo': 0, 'encerradas': 0}
    for status, quantidade in resultados:
        status = int(status)
        if status == 1:
            counts['abertas'] = quantidade
        elif status == 2:
            counts['em_processo'] = quantidade
        elif status == 3:
            counts['encerradas'] = quantidade
    return counts

def get_os_details(solicitante_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = """
    SELECT
        nr_sequencia as sequencia,
        dt_ordem_servico as dataAbertura,
        ds_dano_breve as descricao,
        ds_dano as dano,
        TASY.OBTER_VALOR_DOMINIO(1149, ie_classificacao) as classificacao,
        dt_fim_real as dataFim,
        ie_status_ordem as status,
        TRIM(REGEXP_SUBSTR(TASY.OBTER_DESC_GRUPO_PLANEJ(NR_GRUPO_PLANEJ), '[^ ]+$')) as grupo
    FROM 
        TASY.MAN_ORDEM_SERVICO
    WHERE
        cd_pessoa_solicitante = :solicitante
    ORDER BY 
        dt_ordem_servico DESC
    """
    cursor.execute(query, {'solicitante': solicitante_id})
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def insert_ordem_servico(grupo_trabalho, solicitante_id, usuario, categoria, descricao, dano, grupo_planejamento):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    insert_query = """
        INSERT INTO TASY.MAN_ORDEM_SERVICO (
            nr_sequencia,
            dt_ordem_servico,
            dt_atualizacao,
            ie_status_ordem,
            nr_grupo_trabalho,
            cd_pessoa_solicitante,
            nm_usuario,
            nr_seq_localizacao,
            ie_classificacao,
            ie_prioridade,
            ie_parado,
            ds_dano_breve,
            ds_dano,
            ie_tipo_ordem,
            nr_grupo_planej,
            nr_seq_estagio
        ) VALUES (
            (SELECT COALESCE(MAX(nr_sequencia), 0) + 1 FROM TASY.MAN_ORDEM_SERVICO),
            SYSDATE,
            SYSDATE,
            1,
            :grupo_trabalho,
            :solicitante,
            :usuario,
            (
                SELECT NVL(
                    (SELECT MAX(Y.NR_SEQUENCIA) 
                    FROM TASY.MAN_LOCALIZACAO Y 
                    WHERE Y.CD_SETOR = X.CD_SETOR_ATENDIMENTO AND Y.IE_SITUACAO='A'),
                    49
                ) AS nr_seq_localizacao
                FROM TASY.USUARIO X
                WHERE X.IE_SITUACAO = 'A'
                AND X.CD_PESSOA_FISICA = :solicitante
            ),
            :classificacao,
            'M',
            'N',
            :descricao,
            :dano,
            9,
            :grupo_planejamento,
            21
        )
    """

    parametros = {
        'grupo_trabalho': grupo_trabalho,
        'solicitante': solicitante_id,
        'usuario': usuario,
        'classificacao': categoria,
        'descricao': descricao,
        'dano': dano,
        'grupo_planejamento': grupo_planejamento,
    }
    
    try:
        cursor.execute(insert_query, parametros)
        connection.commit()
        return {'status': 'sucesso', 'mensagem': 'Ordem de serviço criada com sucesso!'}
    except cx_Oracle.DatabaseError as e:
        connection.rollback()
        error, = e.args
        return {'status': 'erro', 'mensagem': 'Erro ao criar ordem de serviço: ' + error.message}
    finally:
        cursor.close()
        connection.close()
