# ramal/views.py
from multiprocessing import context
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

    # Obter o termo de pesquisa do formulário (se houver)
    query = request.GET.get('q', '')

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

    context = {
        'ramais': ramais,
        'query': query,
    }

    context.update(get_common_context())
    # Passar os resultados e o termo de pesquisa para o template
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
