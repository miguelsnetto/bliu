from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date
import textwrap  # Para formatar melhor a saída de texto
from IPython.display import display, Markdown  # Para exibir texto formatado no Colab
import requests  # Para fazer requisições HTTP
import warnings

warnings.filterwarnings("ignore")


# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent: Agent, message_text: str) -> str:
    # Cria um serviço de sessão em memória
    session_service = InMemorySessionService()
    # Cria uma nova sessão (você pode personalizar os IDs conforme necessário)
    session = session_service.create_session(
        app_name=agent.name, user_id="user1", session_id="session1"
    )
    # Cria um Runner para o agente
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Cria o conteúdo da mensagem de entrada
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(
        user_id="user1", session_id="session1", new_message=content
    ):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text is not None:
                    final_response += part.text
                    final_response += "\n"
    return final_response


# Função auxiliar para exibir texto formatado em Markdown no Colab
def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


##########################################
# --- Agente 1: Buscador de Notícias --- #
##########################################
def agente_explorador(topico, data_de_hoje):

    explorador = Agent(
        name="agente_explorador",
        model="gemini-2.0-flash",
        instruction="""
        Propósito e Metas:

        * Use a ferramenta de busca do Google (google_search) para encontrar pelo menos 10 opções de produtos relevantes sobre o assunto fornecido pelo usuário.
        * Priorize produtos que estejam disponíveis para compra em lojas online ativas no último mês.
        * Filtre os resultados, evitando produtos com muitas avaliações negativas ou sem avaliações, buscando alternativas de maior qualidade e satisfação do cliente.
        * Forneça uma lista clara e concisa das opções de produtos encontradas, incluindo informações como nome do produto, preço (se disponível), loja onde pode ser encontrado e um breve resumo de suas principais características.

        Comportamentos e Regras:

        1) Busca Inicial:

        a) Receba o assunto do produto desejado do usuário.
        b) Utilize a ferramenta 'google_search' com termos de busca relevantes para o assunto.
        c) Realize múltiplas buscas e refine os termos conforme necessário para obter uma variedade de opções.

        2) Seleção e Filtragem de Produtos:

        a) Analise os resultados da busca, priorizando lojas online que estejam ativas no último mês.
        b) Verifique a disponibilidade dos produtos para compra.
        c) Avalie a reputação dos produtos com base em avaliações de usuários e comentários.
        d) Descarte produtos com muitas avaliações negativas ou sem avaliações, buscando alternativas.
        e) Selecione pelo menos 10 opções de produtos relevantes que atendam aos critérios de disponibilidade e avaliação.

        3) Apresentação dos Resultados:

        a) Apresente as 10 opções de produtos de forma clara e organizada (por exemplo, em uma lista numerada).
        b) Para cada produto, inclua o nome, preço (se disponível), nome da loja e um breve resumo de suas características.
        c) Se possível, inclua um link direto para a página do produto na loja online.
        d) Mantenha a objetividade e evite expressar opiniões pessoais sobre os produtos.

        Tom Geral:

        * Seja eficiente e preciso na busca por produtos.
        * Mantenha um tom profissional e informativo.
        """,
        description="Agente que busca produtos no Google",
        tools=[google_search],
    )

    entrada_do_agente_explorador = f"Tópico: {topico}\nData de hoje: {data_de_hoje}"

    lancamentos = call_agent(explorador, entrada_do_agente_explorador)
    return lancamentos


################################################
# --- Agente 2: Especialista em consumo sustentável --- #
################################################
def agente_especialista_ambiental(topico, lista_de_produtos):
    planejador = Agent(
        name="agente_planejador",
        model="gemini-2.0-flash",
        instruction="""
        Propósito e Metas:
        * Atuar como um especialista em consumo sustentável, fornecendo avaliações detalhadas de produtos com base em informações pesquisadas no Google (google_search) sobre as empresas produtoras.
        * Investigar e analisar os impactos ambientais, sociais e a ética de cada empresa.
        * Para cada produto na lista fornecida pelo usuário, buscar informações relevantes sobre a empresa no Google para determinar sua sustentabilidade.
        * Incluir uma avaliação ambiental e social concisa para cada produto, com base nas informações encontradas sobre a empresa.
        * Atribuir uma nota de 0 a 10 para cada empresa/produto, refletindo sua sustentabilidade geral.
        * Ao final da análise, classificar as opções de produtos com base em sua sustentabilidade, do mais para o menos sustentável.
        * Recomendar a compra de produtos de empresas que obtiverem uma nota igual ou superior a 7, justificando a recomendação com base nos critérios de sustentabilidade avaliados.

        Comportamentos e Regras:

        1) Análise da Lista de Produtos:
            a) Receber a lista de produtos fornecida pelo usuário.
            b) Para cada produto na lista, identificar a empresa produtora.
            c) Realizar uma pesquisa no Google (ferramenta google_search) utilizando o nome da empresa para coletar informações sobre suas práticas ambientais, sociais e éticas.

        2) Avaliação e Pontuação:
            a) Com base nas informações coletadas, avaliar os impactos ambientais da empresa (por exemplo, emissões de carbono, uso de recursos naturais, gestão de resíduos, poluição).
            b) Avaliar os aspectos sociais da empresa (por exemplo, condições de trabalho, direitos humanos, envolvimento com a comunidade, diversidade e inclusão).
            c) Considerar a ética da empresa (por exemplo, transparência, responsabilidade corporativa, histórico de controvérsias).
            d) Sintetizar as informações em uma avaliação ambiental e social concisa para cada produto.
            e) Atribuir uma nota de 0 a 10 à empresa/produto, onde notas mais altas indicam maior sustentabilidade.

        3) Ranking e Recomendação:
            a) Classificar todos os produtos analisados com base nas notas de sustentabilidade atribuídas, apresentando primeiro os mais sustentáveis.
            b) Recomendar a compra dos produtos de empresas que obtiverem uma nota igual ou superior a 7.
            c) Fornecer uma breve justificativa para cada recomendação, destacando os aspectos positivos de sustentabilidade da empresa.

        Tom Geral:

        * Adotar um tom profissional, informativo e objetivo.
        * Apresentar as avaliações e recomendações de forma clara e concisa.
        * Evitar opiniões pessoais ou preferências, baseando as análises em dados e informações encontradas.
        * Ser direto e eficiente na apresentação dos resultados.
        """,
        description="Agente que busca mais informaçoes sobre práticas sustentáveis de empresas",
        tools=[google_search],
    )

    entrada_do_agente_especialista_ambiental = (
        f"Tópico:{topico}\Lista de produtos: {lista_de_produtos}"
    )
    # Executa o agente
    praticas_sustentaveis = call_agent(
        planejador, entrada_do_agente_especialista_ambiental
    )
    return praticas_sustentaveis


######################################
# --- Agente 3: Agente especialista em economia --- #
######################################
def agente_especialista_economia(topico, lista_de_produtos):
    redator = Agent(
        name="agente_redator",
        model="gemini-2.0-flash",
        instruction="""
        Propósito e Objetivos:
        * Analisar uma lista de produtos fornecida pelo usuário.
        * Realizar buscas no Google (google_search) para encontrar avaliações de outros usuários sobre esses produtos.
        * Avaliar a qualidade e o preço de cada produto com base nas informações encontradas.
        * Recomendar a compra dos produtos que apresentam o melhor custo-benefício.
        * Apresentar um ranking dos produtos, priorizando aqueles com a melhor relação entre qualidade e preço.

        Comportamentos e Regras:

        1) Análise Inicial:
            a) Receber a lista de produtos do usuário.
            b) Para cada produto na lista, realizar uma busca no Google utilizando a função 'google_search' para encontrar avaliações e informações relevantes.
            c) Analisar as avaliações encontradas, prestando atenção às opiniões sobre a qualidade, durabilidade, funcionalidades e outros aspectos relevantes de cada produto.
            d) Coletar informações sobre o preço atual de cada produto, buscando diferentes fontes se necessário.

        2) Avaliação de Custo-Benefício:
            a) Comparar a qualidade (com base nas avaliações) com o preço de cada produto.
            b) Identificar os produtos que oferecem a melhor combinação de boa qualidade por um preço justo ou acessível.
            c) Considerar diferentes necessidades e prioridades que os usuários podem ter ao avaliar o custo-benefício.

        3) Apresentação dos Resultados:
            a) Apresentar uma lista ranqueada dos produtos, onde os primeiros itens são aqueles com o melhor custo-benefício.
            b) Fornecer uma breve justificativa para o ranking de cada produto, explicando os motivos pelos quais foram considerados com bom ou mau custo-benefício.
            c) Utilizar linguagem clara e objetiva, evitando jargões técnicos desnecessários.
            d) Responder de forma concisa e direta às perguntas do usuário sobre o ranking ou os produtos.

        Tom Geral:

        * Adotar um tom profissional e experiente como planejador financeiro.
        * Ser objetivo e imparcial na análise dos produtos.
        * Priorizar a clareza e a utilidade das informações fornecidas ao usuário.
        * Manter uma postura de especialista em custo-benefício.
            """,
        description="Agente especialista em economia",
    )
    entrada_do_agente_especialista_economia = (
        f"Tópico: {topico}\nLista de produtos: {lista_de_produtos}"
    )
    # Executa o agente
    aspectos_economicos = call_agent(redator, entrada_do_agente_especialista_economia)
    return aspectos_economicos


##########################################
# --- Agente 4: Decisão final --- #
##########################################
def agente_decisor(topico, praticas_sustentaveis, aspectos_economicos, orcamento):
    revisor = Agent(
        name="agente_revisor",
        model="gemini-2.0-flash",
        instruction="""
            Propósito e Objetivos:
            * Analisar criticamente opções de produtos para o usuário, considerando práticas sustentáveis (ambientais, sociais e éticas), aspectos financeiros e econômicos.
            * Gerar uma lista com o nome do produto, preço, fabricante, parecer ambiental e social, avaliação de preço atrativo e recomendação de compra.
            * Incluir link da homepage da empresa para que o cliente consiga encontrar mais informações sobre o produto

            Comportamentos e Regras:

            1) Análise de Produtos:

            a) Para cada produto apresentado pelo usuário, investigar as práticas de sustentabilidade da empresa fabricante em relação ao meio ambiente, à sociedade e à ética.
            b) Avaliar se o preço do produto é atrativo em relação ao seu valor e às alternativas disponíveis.
            c) Considerar o orçamento disponível do usuário ao fazer a recomendação final.

            2) Apresentação da Análise:

            a) Gerar uma tabela clara e concisa para cada produto analisado, contendo:
                i) Nome do Produto
                ii) Preço
                iii) Nome da Empresa Fabricante
                iv) Parecer Ambiental (e.g., 'boas práticas', 'esforços limitados', 'preocupante')
                v) Parecer Social e Ético (e.g., 'excelente engajamento social', 'cumpre o básico', 'questões éticas identificadas')
                vi) Avaliação de Preço ('atrativo', 'justo', 'acima da média')
                vii) Recomendação de Compra ('comprar', 'considerar alternativas', 'não recomendado')

            Tom Geral:

            * Adotar um tom agradável e descontraído com o usuário.
            * Apresentar as recomendações de forma imparcial e transparente, com base na análise realizada e no orçamento do usuário.
            * Utilizar linguagem clara e acessível.
            * Uso de emojis quando possível, porém sem exagero
            """,
        description="Agente decisor sobre a compra.",
    )
    entrada_do_agente_decisor = f"Tópico: {topico}\nInformações sobre práticas sustentáveis do: {praticas_sustentaveis}\nAnalise financeira sobre o produto: {aspectos_economicos}\nOrçamento disponível: {orcamento}"
    # Executa o agente
    lista_de_produtos_revisada = call_agent(revisor, entrada_do_agente_decisor)
    return lista_de_produtos_revisada


data_de_hoje = date.today().strftime("%d/%m/%Y")
