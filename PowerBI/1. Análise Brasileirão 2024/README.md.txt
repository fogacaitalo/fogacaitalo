# 📊 Análise do Campeonato Brasileiro 2024 com Power BI ⚽

Olá! 👋 Bem-vindo(a) a este projeto de análise visual dos dados do Campeonato Brasileiro de Futebol Série A de 2024. O objetivo é explorar o desempenho dos times, com foco em resultados, gols e a classificação geral, utilizando o Power BI para criar um painel interativo.

## ✨ Painel Interativo Online

Você pode explorar o painel interativo diretamente no seu navegador através deste link:
[**Visualizar Painel do Brasileirão 2024 no Power BI**](https://app.powerbi.com/view?r=eyJrIjoiZjU3YzI5MTQtZjE4YS00MmVhLThkZDUtMWFhZWE4Mjc3MjQwIiwidCI6IjE2OGQ0MTM3LWQ2ZjYtNDVmOC1hYWE3LWQxYTcwMjMzMDk1ZSIsImMiOjR9)

## 🎯 Objetivo do Projeto

* Coletar e preparar dados da temporada 2024 do Brasileirão Série A.
* Desenvolver um painel no Power BI que apresente de forma clara:
    * A tabela de classificação completa.
    * Desempenho de ataque e defesa dos times.
    * Comparativo de desempenho jogando em casa versus fora.
* Demonstrar o processo de tratamento de dados e criação de visualizações para análise esportiva.

## 💾 Fonte dos Dados

Os dados foram obtidos do site `football-data.co.uk` (arquivo `BRA.csv`), que consolida resultados de diversas temporadas. Para esta análise, filtramos apenas os jogos da temporada de 2024.

## 🛠️ Ferramentas Utilizadas

* **Python (com a biblioteca Pandas):** Para a carga inicial do CSV completo, filtragem da temporada 2024 e uma limpeza básica inicial.
* **Power BI Desktop:** Para as principais transformações de dados (via Power Query), criação de medidas DAX e desenvolvimento do painel de visualização interativo.

## ⚙️ Principais Etapas do Projeto

1.  **Carga e Preparação Inicial (Python/Pandas):**
    * Carregamento do arquivo CSV histórico (`BRA.csv`).
    * Conversão da coluna de datas para o formato datetime.
    * Filtragem para selecionar apenas os jogos da temporada 2024.
    * Limpeza básica de colunas e geração de um CSV intermediário para importação no Power BI.

2.  **Transformação de Dados no Power Query (Power BI):**
    * Importação do CSV preparado.
    * Verificação e ajuste dos tipos de dados.
    * Criação da tabela `Jogos_Times` (formato longo): Duplicação da consulta original para criar visões separadas para "Jogos em Casa" e "Jogos Fora", renomeação de colunas, adição da coluna `Local` ("Casa"/"Fora") e criação de uma coluna condicional `Pontos`.
    * União (Append) das tabelas de "Jogos em Casa" e "Jogos Fora".

3.  **Criação de Medidas DAX (Power BI):**
    * `Total Pontos = SUM(Jogos_Times[Pontos])`
    * `Gols Feitos = SUM(Jogos_Times[GolsFeitos])`
    * `Gols Sofridos = SUM(Jogos_Times[GolsSofridos])`
    * `Saldo Gols = [Gols Feitos] - [Gols Sofridos]`
    * `Jogos = COUNTROWS(Jogos_Times)`
    * `Vitorias = CALCULATE(COUNTROWS(Jogos_Times), Jogos_Times[Pontos] = 3)`
    * `Empates = CALCULATE(COUNTROWS(Jogos_Times), Jogos_Times[Pontos] = 1)`
    * `Derrotas = CALCULATE(COUNTROWS(Jogos_Times), Jogos_Times[Pontos] = 0)`
    * `Posição = RANKX(ALLSELECTED(Jogos_Times[Time]), CALCULATE([Total Pontos]*10000 + [Saldo Gols]*100 + [Gols Feitos]), , DESC, DENSE)`

4.  **Desenvolvimento do Painel no Power BI:**
    * Criação da tabela de classificação interativa.
    * Aplicação de formatação condicional para destacar posições (Libertadores, Sul-Americana, Rebaixamento).
    * Desenvolvimento de gráficos para comparar gols feitos/sofridos e desempenho casa/fora.

##  dashboards O que Você Encontrará no Painel

* Uma **tabela de classificação** completa e dinâmica do Brasileirão 2024.
* **Formatação visual** que facilita a identificação dos times em diferentes faixas da tabela.
* **Gráficos comparativos** do desempenho ofensivo e defensivo das equipes.
* Uma análise do **desempenho dos times jogando em seus domínios versus como visitantes**.
* *(Você pode adicionar aqui outros visuais importantes que criou)*

## 👀 Como Explorar Mais

* 🖼️ **Screenshots:** Algumas imagens do painel também estão disponíveis na pasta `imagens_dashboard` deste repositório (você precisará criar esta pasta e adicionar as imagens).
* 📊 **Arquivo Power BI:** O arquivo `.pbix` (`Analise_Brasileirao_2024.pbix`) deste projeto também está incluído no repositório. Você pode baixá-lo e abri-lo com o Power BI Desktop para explorar a construção do painel, as transformações e os dados.

## 💡 Desafios e Aprendizados

Durante este projeto, o principal desafio foi encontrar uma fonte de dados gratuita que incluísse estatísticas de jogo mais detalhadas, como escanteios. Isso levou à decisão de focar na análise de resultados e gols, que, por si só, já permitem a extração de insights valiosos sobre o campeonato.

## 🚀 Próximos Passos (Possíveis Melhorias)

* Adicionar uma coluna "Rodada" para permitir análises de evolução temporal.
* Explorar a criação de mais visuais, como um gráfico de aproveitamento de pontos.
* Investigar (como uma Fase 2) fontes de dados mais detalhadas para incluir estatísticas como chutes, posse de bola e escanteios.

---

Fique à vontade para explorar o painel online, os arquivos ou entrar em contato se tiver dúvidas ou sugestões!
