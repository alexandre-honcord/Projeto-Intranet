from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from default.models.models_links import Tool, AppsTool
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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


def painelOrdemServico_view(request):
    tools = Tool.objects.all()
    apps = AppsTool.objects.all()
    user = request.user

    return render(request, 'ordemServico/painelOrdemServico.html', {
        'tools': tools,
        'apps': apps,
        'user': user
    })
@csrf_exempt
def processar_ordem_servico(request):
    if request.method == 'POST':
        # Extrair dados da requisição
        tipo = request.POST.get('tipo_ordem')           # Certifique-se de que os nomes correspondam
        categoria = request.POST.get('classificacao_ordem')  # Aqui também
        detalhes = request.POST.get('descricao_ordem')  # E aqui
        impacto = request.POST.get('dano_ordem')        # E aqui

        print(tipo, categoria, detalhes, impacto)  # Verifique se os dados estão sendo capturados corretamente
        response_data = {
            'tipo': tipo,
            'categoria': categoria,
            'detalhes': detalhes,
            'impacto': impacto,
            'status': 'sucesso',
            'mensagem': 'Dados recebidos com sucesso!',
        }
        print(response_data)

        return JsonResponse(response_data)
    
    return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido'}, status=405)