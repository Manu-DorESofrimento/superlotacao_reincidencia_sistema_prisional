# Painel de Projeção de Capacidade Prisional e Reincidência (PCPR)

Projeto de dados abertos para projetar a ocupação de unidades prisionais e estimar risco agregado de reincidência, com o objetivo de apoiar decisões de gestão do sistema penitenciário — não de substituí-las.

## O que é o projeto

Unidades prisionais estaduais no Brasil frequentemente operam acima da capacidade declarada, e a gestão raramente tem visibilidade antecipada sobre a pressão futura de ocupação por unidade. Este projeto combina:

1. **Modelo de projeção de fluxo carcerário** — estima a ocupação futura de cada unidade prisional (6–12 meses) a partir do histórico de entradas e saídas.
2. **Modelo de risco de reincidência agregado** — segmenta a população carcerária por risco de retorno ao sistema em até 24 meses após a saída, em nível de perfil/unidade (nunca individual).

Os dois modelos alimentam um painel único de apoio à decisão para gestores públicos.

## Por que importa

Superlotação carcerária está associada a piores condições de saúde, maior reincidência e maior custo de gestão do sistema. Antecipar picos de ocupação com meses de antecedência permite planejar transferências, mutirões carcerários e alocação de programas de ressocialização de forma proativa em vez de reativa.

## Estrutura do repositório

```
superlotacao_reincidencia_sistema_prisional/
├── README.md
├── canvas.pdf                              Canvas do projeto
├── backlog.md                              Backlog priorizado (histórias de usuário e casos de uso)
├── kanban.md                               Kanban do projeto, com estimativas ágeis
│
├── docs/
│   ├── artigo-cientifico-superlotacao-reincidencia.pdf   Artigo científico
│   └── levantamento-datasets.md                          Levantamento dos datasets usados
│
├── data/
│   └── processed/
│       ├── features_serie_temporal.csv     Dados tratados da série temporal (nacional + SP)
│       └── features_unidades.csv           Dados tratados das unidades prisionais (SAP-SP)
│
├── notebooks/
│   ├── 01_eda_infopen_sap.ipynb            Análise exploratória (Sprint 1)
│   └── 02_treinamento_modelos_baseline.ipynb   Treinamento dos modelos baseline (Sprint 2)
│
├── models/
│   ├── modelo_projecao_populacao_v1.joblib     Modelo de projeção de população/ocupação
│   └── modelo_unidade_critica_v1.joblib        Modelo de classificação de unidade crítica
│
└── src/
    └── features/
        └── preprocessamento_sprint2.py      Script de pré-processamento e feature engineering
```

O `canvas.pdf` dá uma visão geral do projeto. O `backlog.md` e o `kanban.md` mostram o planejamento das sprints. Em `docs/` está o levantamento dos datasets usados e o artigo científico com a fundamentação teórica, a metodologia e os resultados dos modelos. Os notebooks em `notebooks/` mostram a análise exploratória e o treinamento dos modelos passo a passo, e em `models/` ficam os modelos já treinados, salvos em `.joblib`.
