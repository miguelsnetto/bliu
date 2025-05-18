# Clau: Seu Assistente Inteligente para Compras Sustentáveis e Econômicas 🛍️ ☘️

## ✨ Visão Geral do Projeto

No mundo de hoje, tomar decisões de compra que equilibram **preço**, **qualidade** e **impacto ambiental/social** pode ser um verdadeiro desafio. É aqui que entra o **Clau**, um **agente de IA multi-agente** revolucionário que simplifica esse processo para você\!

Clau atua como seu consultor pessoal, explorando o mercado, analisando a sustentabilidade das empresas e avaliando o custo-benefício dos produtos para te guiar nas melhores escolhas. Ele foi projetado para te ajudar a consumir de forma mais consciente, sem abrir mão das suas necessidades e do seu orçamento.

![Agente Clau com uma muda de árvore e uma calculadora nas mãos](/clau.png)
-----

## 💡 O Problema que o Clau resolve

  * **Complexidade da Escolha:** Inúmeras opções de produtos e a dificuldade em compará-los seguindo seus critérios.
  * **Falta de Informação Transparente:** Dificuldade em acessar dados confiáveis sobre as práticas de sustentabilidade das empresas.
  * **Dilema Custo vs. Sustentabilidade:** Muitas vezes, produtos sustentáveis parecem mais caros, e é difícil encontrar o equilíbrio ideal.

Clau aborda esses pontos, fornecendo uma análise profunda e personalizada, permitindo que você tome decisões de compra mais informadas e alinhadas aos seus valores.

-----

## 🤖 Como Clau Funciona: Arquitetura Multi-Agente

O Clau é construído sobre uma arquitetura robusta de **agentes de IA especializados**, cada um com uma função única para garantir uma análise abrangente e precisa. Essa colaboração entre agentes é o que torna o Clau tão eficaz\!

### 1\. **Agente Explorador (Buscador de Produtos)**

  * **Propósito:** O primeiro passo\! Este agente utiliza o poder da busca do Google para encontrar uma ampla gama de produtos relacionados ao seu interesse.
  * **Funcionalidade:** Ele busca, filtra e organiza as opções de produtos disponíveis, priorizando aquelas com boas avaliações e disponibilidade ativa em lojas online. O objetivo é fornecer uma lista inicial rica e relevante.

### 2\. **Agente Especialista em Consumo Sustentável**

  * **Propósito:** Seu consultor de impacto ambiental e social. Este agente mergulha nas práticas de sustentabilidade das empresas por trás dos produtos.
  * **Funcionalidade:** Ele pesquisa informações sobre emissões, uso de recursos, condições de trabalho, ética corporativa e envolvimento social. Cada empresa/produto recebe uma **nota de sustentabilidade (0-10)** e um parecer detalhado, classificando as opções do mais para o menos sustentável.

### 3\. **Agente Especialista em Economia**

  * **Propósito:** O guru do custo-benefício\! Este agente foca na análise financeira dos produtos.
  * **Funcionalidade:** Ele pesquisa avaliações de usuários, compara preços e identifica os produtos que oferecem a melhor relação entre qualidade e preço. O resultado é um ranking claro, priorizando as opções mais vantajosas economicamente dentro do seu orçamento.

### 4\. **Agente Decisor**

  * **Propósito:** O cérebro da operação\! Este agente sintetiza todas as informações coletadas pelos agentes anteriores e gera a recomendação final.
  * **Funcionalidade:** Ele cruza os dados de sustentabilidade e economia, considerando seu orçamento, para apresentar uma tabela comparativa com nome do produto, preço, fabricante, pareceres ambiental/social, avaliação de preço e a **recomendação de compra final**. Ele inclusive fornece links para a homepage das empresas\!

-----

## 🌟 Recursos e Benefícios

  * **Decisão Holística:** Combina sustentabilidade e economia para uma escolha completa.
  * **Recomendações Personalizadas:** Leva em conta seu orçamento e prioridades.
  * **Transparência:** Justificativas claras para cada recomendação.
  * **Economia de Tempo:** Automação da pesquisa e análise de múltiplos critérios.
  * **Consumo Consciente:** Facilita a compra de produtos de empresas mais responsáveis.

-----

## 🛠️ Tecnologias Utilizadas

  * **Google ADK (Agent Development Kit):** O framework para a construção e orquestração dos agentes de IA.
  * **Python:** A linguagem de programação que impulsiona o projeto.
  * **Google Search Tool:** Essencial para a coleta de dados atualizados e relevantes.
  * **Bibliotecas Auxiliares:** `dotenv` (para gerenciar variáveis de ambiente), `datetime`, `textwrap`, `IPython.display`, `requests`, `warnings`.

-----

## 🚀 Como Rodar o Clau

### Pré-requisitos

  * Python 3.8+
  * Uma chave de API do Google Gemini.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```
2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # ou
    venv\Scripts\activate  # No Windows
    ```
3.  **Instale as dependências:**
    ```bash
    %pip install -q google-genai google-adk python-dotenv
    ```

### Configuração da API Key

1.  Crie um arquivo `.env` na raiz do projeto.
2.  Adicione sua chave de API do Google Gemini a ele:
    ```
    GOOGLE_API_KEY='SUA_API_KEY_AQUI'
    ```

### Execução

1.  Abra o notebook `agente.ipynb` em um ambiente como Google Colab ou Jupyter Notebook.
2.  Execute todas as células. Quando solicitado, digite o produto que deseja pesquisar e o orçamento disponível.

-----

## 🎯 Exemplo de Uso

Vamos ver o Clau em ação ao pesquisar por "Tênis de Corrida" com um orçamento de "R$600":

**Input:**

```
O que você gostaria de comprar hoje? Tênis de Corrida 600
Quanto você tem disponível para compra? R$600
```

**Resultado Final (Agente Decisor):**

> Olá\! 😊 Analisando suas opções de tênis com foco em sustentabilidade, custo-benefício e seu orçamento de R$600, preparei uma tabela com as melhores recomendações pra você\!
>
> | Produto                | Preço (R$) | Fabricante | Parecer Ambiental 🌿 | Parecer Social e Ético 🤝 | Avaliação de Preço 💰 | Recomendação de Compra ✅ | Link da Empresa                                                        |
> | ---------------------- | ---------- | ---------- | --------------------- | ------------------------- | ----------------------- | ------------------------ | --------------------------------------------------------------------- |
> | ASICS Gel-Pulse 15     | \<400       | ASICS      | Informações Limitadas  | Informações Limitadas     | Atrativo                | Comprar                  | [ASICS](https://www.asics.com.br/)                                    |
> | Mizuno Wave Rider 27   | 430        | Mizuno     | Crescendo             | Cumpre o Básico          | Justo                   | Comprar                  | [Mizuno](https://www.mizuno.com.br/)                                  |
> | Olympikus Corre 4      | 500        | Olympikus  | Boas Práticas        | Excelente Engajamento     | Justo                   | Comprar                  | [Olympikus](https://www.olympikus.com.br/)                              |
> | Fila Float Maxxi 2     | 500-550    | Fila       | Cumpre o Básico        | Cumpre o Básico          | Justo                   | Comprar                  | [Fila](https://www.fila.com.br/)                                      |
> | ASICS Dynablast 4     | \<600       | ASICS      | Informações Limitadas  | Informações Limitadas     | Justo                   | Comprar                  | [ASICS](https://www.asics.com.br/)                                    |
> | Adidas Supernova Rise  | \<600\* | Adidas     | Boas Práticas        | Cumpre o Básico          | Atrativo (se \<R$600)   | Considerar Alternativas | [Adidas](https://www.adidas.com.br/)                                   |
> | New Balance 880v13/v14 | 600        | New Balance| Boas Práticas        | Cumpre o Básico          | Justo                   | Considerar Alternativas | [New Balance](https://www.newbalance.com.br/)                           |
>
>   * **Observações:**
>
>       * **ASICS Gel-Pulse 15**: Ideal para iniciantes e quem busca economia.
>       * **Mizuno Wave Rider 27**: Ótima durabilidade para treinos diários.
>       * **Olympikus Corre 4**: Versátil para diferentes distâncias.
>       * **Fila Float Maxxi 2**: Bom amortecimento para iniciantes e pessoas com sobrepeso
>       * **ASICS Dynablast 4**: Para quem busca conforto e responsividade.
>       * **Adidas Supernova Rise**: Se encontrar abaixo de R$600, pode valer a pena pelo amortecimento.
>       * **New Balance 880v13/v14**: Conforto e bom ajuste para treinos diários.
>
> Espero que ajude na sua escolha\! 😉 Se tiver mais dúvidas, é só perguntar\! 😊

-----

## 📈 Próximos Passos e Melhorias Futuras

Estamos sempre buscando aprimorar o Clau\! Algumas ideias para o futuro incluem:

  * **Integração com APIs de E-commerce:** Para obter preços em tempo real e links diretos de compra mais precisos.
  * **Métricas de Sustentabilidade Aprofundadas:** Pesquisar certificações, relatórios de impacto e pegada de carbono.
  * **Personalização de Preferências:** Permitir que o usuário defina o peso de cada critério (sustentabilidade vs. economia).
  * **Interface de Usuário (UI):** Desenvolver uma interface mais intuitiva para interação com o Clau.
  * **Análise de Avaliações em Maior Escala:** Utilizar processamento de linguagem natural (PNL) avançado para extrair insights mais ricos de milhares de avaliações.

-----

## 🤝 Contribua\!

Sua contribuição é muito bem-vinda\! Se você tem ideias, sugestões ou quer colaborar com o desenvolvimento do Clau, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
