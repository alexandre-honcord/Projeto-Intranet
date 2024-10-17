# ramal/views.py
from django.shortcuts import render
import cx_Oracle # type: ignore
from default.models.models_links import Tool, AppsTool
from django.http import JsonResponse

def get_common_context():
    return {
        'tools': Tool.objects.all(),
        'apps': AppsTool.objects.all()
    }

def lista_ramais(request):
    # Configurar a conexão manual ao banco Oracle
    dsn_tns = cx_Oracle.makedsn('10.0.1.12', '1521', service_name='dbprod')  # Verifique a porta e service_name
    connection = cx_Oracle.connect(user='AUGUSTO', password='Mudar@123', dsn=dsn_tns)

    # Obter o termo de pesquisa e a coluna de ordenação
    query = request.GET.get('q', '')
    order_by = request.GET.get('order_by', 'nome')  # Usando 'nome' como padrão
    order_direction = request.GET.get('order_direction', 'asc')

    # Mapeamento de campos da tabela com os parâmetros
    column_mapping = {
        'nome': 'ds_usuario',
        'departamento': 'TASY.obter_desc_setor_atend(cd_setor_atendimento)',
        'ramal': 'nr_ramal'
    }

    # Garantir que a coluna de ordenação é válida
    if order_by not in column_mapping:
        order_by = 'nome'  # Redefinir para padrão se inválido
    
    # Verificar a direção de ordenação
    if order_direction not in ['asc', 'desc']:
        order_direction = 'asc'  # Redefinir para padrão se inválido

    # Construir a cláusula de ordenação
    order_clause = f"{column_mapping[order_by]} {order_direction}"

    # Query SQL com filtro de pesquisa e ordenação
    sql = f"""
        SELECT ds_usuario AS nome,
            TASY.obter_desc_setor_atend(cd_setor_atendimento) AS departamento,
            nr_ramal AS ramal
        FROM TASY.usuario
        WHERE ie_situacao = 'A'
        AND nr_ramal IS NOT NULL
    """
    
    # Adicionar condição de pesquisa na query, se houver termo
    if query:
        sql += " AND LOWER(ds_usuario) LIKE :search"
    
    # Adicionar a cláusula de ordenação
    sql += f" ORDER BY {order_clause}"

    # Executar a query
    cursor = connection.cursor()
    if query:
        cursor.execute(sql, search=f'%{query.lower()}%')
    else:
        cursor.execute(sql)

    # Buscar todos os resultados da query
    ramais = cursor.fetchall()

    # Fechar a conexão
    cursor.close()
    connection.close()

    # Passar os resultados para o template
    context = {
        'ramais': ramais,
        'query': query,
        'order_by': order_by,
        'order_direction': order_direction,
    }
    context.update(get_common_context())
    return render(request, 'lista_ramais.html', context)

def ajax_lista_ramais(request):
    # Obter o termo de pesquisa via AJAX
    query = request.GET.get('q', '')

    # Configurar a conexão manual ao banco Oracle
    dsn_tns = cx_Oracle.makedsn('10.0.1.12', '1521', service_name='dbprod')  # Verifique a porta e service_name
    connection = cx_Oracle.connect(user='AUGUSTO', password='Mudar@123', dsn=dsn_tns)

    # Query SQL com filtro de pesquisa
    sql = """
        SELECT ds_usuario AS nome,
               TASY.obter_desc_setor_atend(cd_setor_atendimento) AS departamento,
               nr_ramal AS ramal
        FROM TASY.usuario
        WHERE ie_situacao = 'A'
          AND nr_ramal IS NOT NULL
    """

    # Adicionar condição de pesquisa na query, se houver termo
    if query:
        sql += " AND LOWER(ds_usuario) LIKE :search ORDER BY ds_usuario ASC"
        cursor = connection.cursor()
        cursor.execute(sql, search=f'%{query.lower()}%')
    else:
        sql += " ORDER BY ds_usuario ASC"
        cursor = connection.cursor()
        cursor.execute(sql)

    # Buscar todos os resultados da query
    ramais = cursor.fetchall()

    # Fechar a conexão
    cursor.close()
    connection.close()

    # Retornar os dados como JSON
    return JsonResponse({'ramais': ramais})
