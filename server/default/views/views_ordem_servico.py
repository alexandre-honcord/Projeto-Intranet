from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from default.models.models_links import Tool, AppsTool
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import cx_Oracle
from ..utils import categorize_os_details, parse_request_data
from ..dbutils import get_status_counts, get_os_details, insert_ordem_servico

@login_required
def ordemServico_view(request):
    tools = Tool.objects.all()
    apps = AppsTool.objects.all()
    user = request.user

    return render(request, 'ordemServico/ordemServico.html', {
        'tools': tools,
        'apps': apps,
        'user': user
    })

@login_required
def painelOrdemServico_view(request):
    solicitante_id = str(request.user.IDtasy)

    try:
        status_counts = get_status_counts(solicitante_id)
        quantidade_abertas = status_counts['abertas']
        quantidade_em_processo = status_counts['em_processo']
        quantidade_encerradas = status_counts['encerradas']

        resultados_os = get_os_details(solicitante_id)
        os_abertas, os_em_processo, os_encerradas = categorize_os_details(resultados_os)

    except cx_Oracle.DatabaseError as e:
        print("Erro ORA:", e)
        quantidade_abertas = quantidade_em_processo = quantidade_encerradas = 0
        os_abertas = os_em_processo = os_encerradas = []

    tools = Tool.objects.all()
    apps = AppsTool.objects.all()
    user = request.user

    context = {
        'tools': tools,
        'apps': apps,
        'user': user,
        'quantidade_abertas': quantidade_abertas,
        'quantidade_em_processo': quantidade_em_processo,
        'quantidade_encerradas': quantidade_encerradas,
        'os_abertas': os_abertas,
        'os_em_processo': os_em_processo,
        'os_encerradas': os_encerradas,
    }

    return render(request, 'ordemServico/painelOrdemServico.html', context)

@csrf_exempt
@login_required
def processar_ordem_servico(request):
    if request.method == 'POST':
        grupo_planejamento, grupo_trabalho, categoria, detalhes, impacto = parse_request_data(request)

        if grupo_trabalho is None:
            return JsonResponse({'status': 'erro', 'mensagem': 'Erro nos dados numéricos'}, status=400)

        solicitante_id = str(request.user.IDtasy)
        usuario = request.user.username

        response_data = insert_ordem_servico(
            grupo_trabalho=grupo_trabalho,
            solicitante_id=solicitante_id,
            usuario=usuario,
            categoria=categoria,
            descricao=detalhes,
            dano=impacto,
            grupo_planejamento=grupo_planejamento,
        )

        return JsonResponse(response_data)

    return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido'}, status=405)