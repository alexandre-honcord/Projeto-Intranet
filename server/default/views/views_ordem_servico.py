from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from default.models.models_links import Tool, AppsTool
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from default.models.models_tasy import User
import cx_Oracle

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
@login_required
def processar_ordem_servico(request):
    if request.method == 'POST':
        # Extrair dados da requisição
        grupo_planejamento = request.POST.get('ordem')
        grupo_trabalho = request.POST.get('tipo_ordem')
        categoria = request.POST.get('classificacao_ordem')
        detalhes = request.POST.get('descricao_ordem')
        impacto = request.POST.get('dano_ordem')

        # Converter grupo_planejamento para inteiro, se possível
        grupo_planejamento = int(grupo_planejamento)

        if grupo_planejamento != 22:
            if grupo_planejamento == 27:
                grupo_trabalho = 19
            elif grupo_planejamento == 21:
                grupo_trabalho = 11
            elif grupo_planejamento == 30:
                grupo_trabalho = 74

        # Obter IDtasy do usuário logado
        solicitante_id = str(request.user.IDtasy)
        usuario = request.user.username

        try:
            grupo_trabalho = int(grupo_trabalho)
            grupo_planejamento = int(grupo_planejamento)
        except ValueError as e:
            print("Erro de conversão para número:", str(e))
            return JsonResponse({'status': 'erro', 'mensagem': 'Erro nos dados numéricos'}, status=400)

        # Configuração da conexão com o Oracle
        dsn_tns = cx_Oracle.makedsn('10.0.1.20', '1521', service_name='dbtest')
        connection = cx_Oracle.connect(user='tasy', password='honbdt_exhemo', dsn=dsn_tns)

        try:
            # Criar um cursor para executar comandos SQL
            cursor = connection.cursor()

            # Montar a query de inserção
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
                    49,
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

            # Definir valores dos parâmetros para a query
            parametros = {
                'grupo_trabalho': grupo_trabalho,
                'solicitante': solicitante_id,
                'usuario': usuario,
                'classificacao': categoria,
                'descricao': detalhes,
                'dano': impacto,
                'grupo_planejamento': grupo_planejamento,
            }

            # Imprimir parâmetros para verificação
            # print("Parâmetros para inserção no banco:")
            # for key, value in parametros.items():
            #     print(f"{key}: {value}")


            # Executar a inserção
            cursor.execute(insert_query, parametros)

            # Confirmar transação
            connection.commit()

            # Preparar resposta de sucesso
            response_data = {
                'status': 'sucesso',
                'mensagem': 'Ordem de serviço criada com sucesso!',
                'redirect_url': '/painel/OrdemServico'
            }

        except cx_Oracle.DatabaseError as e:
            # Capturar e imprimir erro específico do Oracle no console
            error, = e.args
            print("Erro ORA:", error.message)

            # Fazer rollback e retornar mensagem de erro
            connection.rollback()
            response_data = {
                'status': 'erro',
                'mensagem': 'Erro ao criar ordem de serviço: ' + error.message,
            }

        finally:
            # Fechar cursor e conexão
            cursor.close()
            connection.close()

        return JsonResponse(response_data)

    return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido'}, status=405)