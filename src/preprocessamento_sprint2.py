"""
Pré-processamento e engenharia de atributos — Sprint 2 (MVP Analítico)

Consolida os dados reais coletados na Sprint 1 (ver docs/levantamento-datasets.md e
notebooks/01_eda_infopen_sap.ipynb) em duas tabelas de features prontas para modelagem:

  1. features_serie_temporal.csv — série anual (nacional + SP) com atributos de lag e
     taxa de crescimento, usada para o baseline de projeção de população/ocupação.
  2. features_unidades.csv — snapshot real de unidades prisionais de SP com atributos
     derivados (taxa de ocupação, log da capacidade, one-hot do tipo de unidade) e o
     rótulo binário "critico" (taxa_ocupacao >= 1.5), usado para o baseline de
     classificação de unidades críticas.

Nenhum dado é simulado: todos os valores de entrada vêm das fontes documentadas em
docs/levantamento-datasets.md (INFOPEN/DEPEN via artigo peer-reviewed, SAP-SP oficial).

Uso:
    python src/features/preprocessamento_sprint2.py
"""

import logging
from pathlib import Path

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

PROCESSED_DIR = Path("data/processed")
LIMIAR_CRITICO = 1.5


# ---------------------------------------------------------------------------
# 1. Dados reais de entrada (mesmos valores usados no notebook 01_eda_infopen_sap.ipynb)
# ---------------------------------------------------------------------------

def carregar_serie_nacional() -> pd.DataFrame:
    """Série nacional 2007-2019 (INFOPEN/DEPEN via Cadernos de Saúde Pública, 2023)."""
    return pd.DataFrame([
        {"ano": 2007, "populacao": 366359, "ppl_por_vaga": 1.5},
        {"ano": 2008, "populacao": 394488, "ppl_por_vaga": 1.5},
        {"ano": 2009, "populacao": 417112, "ppl_por_vaga": 1.5},
        {"ano": 2010, "populacao": 445705, "ppl_por_vaga": 1.6},
        {"ano": 2011, "populacao": 471254, "ppl_por_vaga": 1.6},
        {"ano": 2012, "populacao": 548003, "ppl_por_vaga": 1.8},
        {"ano": 2013, "populacao": 537790, "ppl_por_vaga": 1.7},
        {"ano": 2014, "populacao": 584758, "ppl_por_vaga": 1.6},
        {"ano": 2015, "populacao": 663385, "ppl_por_vaga": 1.8},
        {"ano": 2016, "populacao": 702385, "ppl_por_vaga": 1.6},
        {"ano": 2017, "populacao": 704576, "ppl_por_vaga": 1.6},
        {"ano": 2018, "populacao": 725332, "ppl_por_vaga": 1.6},
        {"ano": 2019, "populacao": 748009, "ppl_por_vaga": 1.7},
    ]).assign(serie="nacional")


def carregar_serie_sp() -> pd.DataFrame:
    """Série histórica da SAP-SP (2022-2026), publicada em www1.sap.sp.gov.br."""
    return pd.DataFrame([
        {"ano": 2022, "populacao": 195194, "ppl_por_vaga": np.nan},
        {"ano": 2023, "populacao": 197071, "ppl_por_vaga": np.nan},
        {"ano": 2024, "populacao": 205210, "ppl_por_vaga": np.nan},
        {"ano": 2025, "populacao": 221252, "ppl_por_vaga": np.nan},
    ]).assign(serie="sp")


def carregar_unidades_sp() -> pd.DataFrame:
    """Snapshot real de unidades prisionais de SP (data-base 23/jun), fonte SAP-SP."""
    return pd.DataFrame([
        {"unidade": 'Álvaro de Carvalho - Penit. I "Valentim Alves da Silva"', "tipo": "Penitenciária", "capacidade": 873, "populacao": 1610},
        {"unidade": "Álvaro de Carvalho - APP", "tipo": "APP", "capacidade": 222, "populacao": 281},
        {"unidade": "CDP Álvaro de Carvalho", "tipo": "CDP", "capacidade": 821, "populacao": 1568},
        {"unidade": "Andradina - Penitenciária", "tipo": "Penitenciária", "capacidade": 1291, "populacao": 2197},
        {"unidade": "Araraquara - Penit. Dr. Sebastião Martins Silveira", "tipo": "Penitenciária", "capacidade": 1312, "populacao": 2255},
        {"unidade": "Araraquara - PRSA", "tipo": "PRSA", "capacidade": 248, "populacao": 293},
        {"unidade": "Presidente Bernardes - Penitenciária", "tipo": "Penitenciária", "capacidade": 1247, "populacao": 2368},
        {"unidade": "Presidente Bernardes - APP", "tipo": "APP", "capacidade": 204, "populacao": 257},
        {"unidade": "Presidente Prudente - Penitenciária", "tipo": "Penitenciária", "capacidade": 693, "populacao": 1297},
        {"unidade": "Presidente Prudente - PRSA", "tipo": "PRSA", "capacidade": 267, "populacao": 340},
    ])


# ---------------------------------------------------------------------------
# 2. Engenharia de atributos — série temporal
# ---------------------------------------------------------------------------

def construir_features_serie_temporal() -> pd.DataFrame:
    df = pd.concat([carregar_serie_nacional(), carregar_serie_sp()], ignore_index=True)
    df = df.sort_values(["serie", "ano"]).reset_index(drop=True)

    # Lag features e taxa de crescimento ano a ano, calculadas por série
    df["populacao_lag1"] = df.groupby("serie")["populacao"].shift(1)
    df["crescimento_absoluto"] = df["populacao"] - df["populacao_lag1"]
    df["crescimento_pct"] = df.groupby("serie")["populacao"].pct_change() * 100

    # Média móvel de 3 anos (usada como baseline "moving average")
    df["media_movel_3anos"] = (
        df.groupby("serie")["populacao"]
        .transform(lambda s: s.shift(1).rolling(window=3, min_periods=1).mean())
    )

    return df


# ---------------------------------------------------------------------------
# 3. Engenharia de atributos — unidades prisionais
# ---------------------------------------------------------------------------

def construir_features_unidades() -> pd.DataFrame:
    df = carregar_unidades_sp().copy()

    df["taxa_ocupacao"] = df["populacao"] / df["capacidade"]
    df["log_capacidade"] = np.log(df["capacidade"])
    df["critico"] = (df["taxa_ocupacao"] >= LIMIAR_CRITICO).astype(int)

    # One-hot encoding do tipo de unidade (atributo categórico)
    tipo_dummies = pd.get_dummies(df["tipo"], prefix="tipo")
    df = pd.concat([df, tipo_dummies], axis=1)

    return df


# ---------------------------------------------------------------------------
# Execução
# ---------------------------------------------------------------------------

def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    features_serie = construir_features_serie_temporal()
    caminho_serie = PROCESSED_DIR / "features_serie_temporal.csv"
    features_serie.to_csv(caminho_serie, index=False)
    logger.info("Salvo: %s (%d linhas)", caminho_serie, len(features_serie))

    features_unidades = construir_features_unidades()
    caminho_unidades = PROCESSED_DIR / "features_unidades.csv"
    features_unidades.to_csv(caminho_unidades, index=False)
    logger.info("Salvo: %s (%d linhas)", caminho_unidades, len(features_unidades))
    logger.info(
        "Distribuição do rótulo 'critico': %d críticas / %d não críticas (de %d unidades)",
        features_unidades["critico"].sum(),
        len(features_unidades) - features_unidades["critico"].sum(),
        len(features_unidades),
    )
    logger.info(
        "ATENÇÃO: amostra pequena (N=%d unidades, %d pontos de série temporal) — "
        "resultados desta sprint são um MVP analítico, não um modelo final. "
        "Ver limitações documentadas no artigo científico (Seção 8).",
        len(features_unidades), len(features_serie),
    )


if __name__ == "__main__":
    main()
