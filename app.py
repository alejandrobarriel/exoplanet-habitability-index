import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Exoplanet Habitability Lab",
    page_icon="Images/nasa.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# ESTILO GLOBAL
# =========================
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="collapsedControl"] {
        display: none;
    }

    .block-container {
        margin-top: 25px;
        max-width: 1450px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        padding-left: 2.2rem;
        padding-right: 2.2rem;
    }

    .main > div {
        padding-top: 0rem;
    }

    .app-badge {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(86,180,233,0.12);
        color: #EE57A2;
        border: 1px solid rgba(125,211,252,0.22);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        margin-bottom: 0.9rem;
    }

    .hero-card {
        background:
            radial-gradient(circle at top right, rgba(86,180,233,0.14), transparent 24%),
            linear-gradient(135deg, rgba(10,14,25,1) 0%, rgba(13,20,35,1) 100%);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 24px;
        padding: 1.6rem 1.7rem 1.35rem 1.7rem;
        margin-bottom: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.22);
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.04;
        letter-spacing: -0.03em;
        color: #f8fafc;
        margin-bottom: 0.55rem;
    }

    .hero-highlight {
        color: #56B4E9;
    }

    .hero-subtitle {
        font-size: 1.06rem;
        line-height: 1.65;
        color: #d6e0ea;
        max-width: 1000px;
        margin-bottom: 0.35rem;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.1;
        color: #f8fafc;
        margin-top: 0.35rem;
        margin-bottom: 0.4rem;
        letter-spacing: -0.02em;
    }

    .section-subtitle {
        font-size: 1rem;
        color: #c8d4df;
        margin-bottom: 1rem;
        line-height: 1.55;
    }

    .divider {
        height: 1px;
        background: linear-gradient(90deg, rgba(86,180,233,0.22), rgba(255,255,255,0.03));
        margin: 1.15rem 0 1.35rem 0;
        border-radius: 999px;
    }

    .metric-card {
        background: linear-gradient(180deg, rgba(27,33,47,0.96) 0%, rgba(16,20,30,0.96) 100%);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 20px;
        padding: 1.2rem 1rem;
        text-align: left;
        min-height: 122px;
        box-shadow: 0 10px 22px rgba(0,0,0,0.16);
    }

    .metric-label {
        font-size: 0.83rem;
        color: #97a8ba;
        margin-bottom: 0.4rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 700;
    }

    .metric-value {
        font-size: 2rem;
        color: #56B4E9;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 0.2rem;
    }

    .metric-value-small {
        font-size: 1.32rem;
        color: #56B4E9;
        font-weight: 800;
        line-height: 1.25;
        word-break: break-word;
    }

    .metric-help {
        font-size: 0.92rem;
        color: #e5edf5;
    }

    .mini-note {
        color: #9fb1c4;
        font-size: 0.92rem;
        margin-top: 0.35rem;
    }

    .panel-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 1rem 1rem 0.4rem 1rem;
        margin-bottom: 1rem;
    }

/* Radio horizontal de navegación */
/*
    div[role="radiogroup"] {
        gap: 0.5rem;
    }

    div[role="radiogroup"] > label {
        background: #56B4E9;
        border: 1px solid rgba(255,255,255,0.06);
        color: black !important;
        border-radius: 999px;
        padding: 0.55rem 0.95rem !important;

    }

   div[role="radiogroup"] > label:hover {
        background: #e91e8c !important;
        border-color: #e91e8c !important;
        color: white !important;
    }

    /* Ocultar bolita del radio */
    div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }
*/
    
    
    /* Botones de navegación */
    

    /* Inputs */
    .stNumberInput > div > div,
    .stTextInput > div > div,
    .stSelectbox > div > div,
    .stMultiSelect > div > div {
        border-radius: 14px !important;
    }

/*
    .stButton > button {
        border-radius: 14px !important;
        font-weight: 700 !important;
    }

    .stButton > button[kind="primary"] {
        background: #e91e8c !important;
        border-color: #e91e8c !important;
        color: white !important;
    }
*/

/* Botones de navegación: selector real de Streamlit */
    div[data-testid="stButton"] > button[data-testid="stBaseButton-secondary"] {
        background-color: rgba(86, 180, 233, 0.35) !important;
        background-image: none !important;
        border: 1px solid #56B4E9 !important;
        color: white !important;
        border-radius: 999px !important;
        min-height: 44px !important;
        font-weight: 700 !important;
        box-shadow: none !important;
    }

    div[data-testid="stButton"] > button[data-testid="stBaseButton-secondary"]:hover {
        background-color: #e91e8c !important;
        background-image: none !important;
        border-color: #e91e8c !important;
        color: white !important;
    }

    div[data-testid="stButton"] > button[data-testid="stBaseButton-secondary"]:focus,
    div[data-testid="stButton"] > button[data-testid="stBaseButton-secondary"]:active {
        background-color: rgba(86, 180, 233, 0.12) !important;
        background-image: none !important;
        border-color: #56B4E9 !important;
        color: #56B4E9 !important;
        box-shadow: none !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
    }

    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        border-radius: 12px 12px 0 0;
        font-weight: 700;
    }
    
    
    
</style>
""", unsafe_allow_html=True)

# =========================
# CONSTANTES
# =========================
FAMILY_COLS = {
    "orbita": ["pl_orbper", "pl_orbsmax", "pl_orbeccen"],
    "planeta": ["pl_rade", "pl_bmasse", "pl_dens", "pl_eqt", "pl_insol"],
    "estrella": ["st_teff", "st_lum", "st_mass", "st_rad", "st_met", "st_logg", "st_age"]
}

DEFAULT_SENSITIVITY = {
    "winsor_threshold": 1.5,
    "p_low": 1,
    "p_high": 99,
    "weight_orbita": 1.0,
    "weight_planeta": 1.0,
    "weight_estrella": 1.0,
    "stability_top_n": 20
}

# =========================
# FUNCIONES DE DATOS
# =========================
@st.cache_data
def cargar_datos():
    try:
        return pd.read_csv("DataSets/exoplanetas_nasa.csv")
    except FileNotFoundError:
        st.error("❌ Error: No se encontró el archivo exoplanetas_nasa.csv")
        st.stop()


@st.cache_data
def procesar_datos(df_nasa):
    num_cols = [
        "pl_orbper", "pl_orbsmax", "pl_orbeccen", "pl_rade", "pl_bmasse",
        "pl_dens", "pl_eqt", "pl_insol", "st_teff", "st_lum", "st_mass",
        "st_rad", "st_met", "st_logg", "st_age"
    ]
    id_cols = ["objectid", "pl_name", "hostname"]

    df_reduced = df_nasa[id_cols + num_cols].copy()
    df_reduced["objectid"] = df_reduced["objectid"].astype(str)

    return df_reduced, num_cols


@st.cache_data
def imputar_datos(df_reduced, num_cols):
    df_imputed = df_reduced.copy()

    cols_type_A = [
        "pl_rade", "pl_bmasse", "pl_dens",
        "st_teff", "st_lum", "st_mass",
        "st_rad", "st_met", "st_logg", "st_age"
    ]

    for col in cols_type_A:
        if col in df_imputed.columns:
            median_value = df_imputed[col].median()
            df_imputed[col] = df_imputed[col].fillna(median_value)

    if "pl_orbeccen" in df_imputed.columns:
        df_imputed["pl_orbeccen"] = df_imputed["pl_orbeccen"].fillna(0)

    DAYS_PER_YEAR = 365.25

    mask_orbsmax = (
        df_imputed["pl_orbsmax"].isna() &
        df_imputed["pl_orbper"].notna() &
        df_imputed["st_mass"].notna()
    )

    P_years = df_imputed.loc[mask_orbsmax, "pl_orbper"] / DAYS_PER_YEAR

    df_imputed.loc[mask_orbsmax, "pl_orbsmax"] = (
        (P_years ** (2/3)) *
        (df_imputed.loc[mask_orbsmax, "st_mass"] ** (1/3))
    )

    mask_orbper = (
        df_imputed["pl_orbper"].isna() &
        df_imputed["pl_orbsmax"].notna() &
        df_imputed["st_mass"].notna()
    )

    P_years = (
        (df_imputed.loc[mask_orbper, "pl_orbsmax"] ** (3/2)) /
        (df_imputed.loc[mask_orbper, "st_mass"] ** (1/2))
    )

    df_imputed.loc[mask_orbper, "pl_orbper"] = P_years * DAYS_PER_YEAR

    RSUN_TO_AU = 0.00465047

    mask_eqt = (
        df_imputed["pl_eqt"].isna() &
        df_imputed["st_teff"].notna() &
        df_imputed["st_rad"].notna() &
        df_imputed["pl_orbsmax"].notna()
    )

    R_star_AU = df_imputed.loc[mask_eqt, "st_rad"] * RSUN_TO_AU

    df_imputed.loc[mask_eqt, "pl_eqt"] = (
        df_imputed.loc[mask_eqt, "st_teff"] *
        np.sqrt(R_star_AU / (2 * df_imputed.loc[mask_eqt, "pl_orbsmax"]))
    )

    mask_insol = (
        df_imputed["pl_insol"].isna() &
        df_imputed["st_lum"].notna() &
        df_imputed["pl_orbsmax"].notna()
    )

    df_imputed.loc[mask_insol, "pl_insol"] = (
        (10 ** df_imputed.loc[mask_insol, "st_lum"]) /
        (df_imputed.loc[mask_insol, "pl_orbsmax"] ** 2)
    )

    cols_problem = ["pl_orbper", "pl_orbsmax", "pl_eqt", "pl_insol"]
    df_work = df_imputed.dropna(subset=cols_problem)

    return df_work


def winsorizar_tukey(x, threshold=1.5):
    q1 = x.quantile(0.25)
    q3 = x.quantile(0.75)
    iqr = q3 - q1
    floor = q1 - threshold * iqr
    ceiling = q3 + threshold * iqr
    return x.clip(lower=floor, upper=ceiling)


@st.cache_data
def gestionar_outliers(df_work, cols, threshold=1.5):
    df_wins = df_work.copy()
    for col in cols:
        df_wins[col] = winsorizar_tukey(df_wins[col], threshold=threshold)
    return df_wins


@st.cache_data
def calcular_indices_habitabilidad(
    df_final,
    num_cols,
    reference_vector,
    p_low=1,
    p_high=99,
    family_weights=None,
    df_original=None,
    df_csv=None
):
    if family_weights is None:
        family_weights = {"orbita": 1.0, "planeta": 1.0, "estrella": 1.0}

    vector_referencia = pd.Series(reference_vector)[num_cols]
    p_low_q = df_final[num_cols].quantile(p_low / 100)
    p_high_q = df_final[num_cols].quantile(p_high / 100)
    rango_tipico = (p_high_q - p_low_q).clip(lower=1e-9)

    df_rankingExoplanetas = df_final.copy()
    csv_by_index = df_csv.copy() if df_csv is not None else None
    original_by_index = df_original.copy() if df_original is not None else None

    norm_cols = []
    for col in num_cols:
        x_ref = vector_referencia[col]
        rango = rango_tipico[col]
        csv_col = f"{col}_csv"
        imputado_col = f"{col}_imputado"
        raw_col = f"{col}_raw"
        norm_col = f"{col}_norm"

        if csv_by_index is not None and col in csv_by_index.columns:
            df_rankingExoplanetas[csv_col] = csv_by_index[col].reindex(df_rankingExoplanetas.index).values
        else:
            df_rankingExoplanetas[csv_col] = np.nan

        if original_by_index is not None and col in original_by_index.columns:
            df_rankingExoplanetas[imputado_col] = original_by_index[col].reindex(df_rankingExoplanetas.index).values
        else:
            df_rankingExoplanetas[imputado_col] = df_rankingExoplanetas[col]

        df_rankingExoplanetas[raw_col] = df_rankingExoplanetas[col]
        df_rankingExoplanetas[norm_col] = (df_rankingExoplanetas[col] - x_ref) / rango
        norm_cols.append(norm_col)

    weighted_terms = []
    for col in num_cols:
        norm_col = f"{col}_norm"
        if col in FAMILY_COLS["orbita"]:
            weight = family_weights.get("orbita", 1.0)
        elif col in FAMILY_COLS["planeta"]:
            weight = family_weights.get("planeta", 1.0)
        else:
            weight = family_weights.get("estrella", 1.0)
        weighted_terms.append(weight * (df_rankingExoplanetas[norm_col] ** 2))

    df_rankingExoplanetas["distancia_tierra"] = np.sqrt(np.sum(weighted_terms, axis=0))
    df_rankingExoplanetas["indice_habitabilidad"] = 1 / (1 + df_rankingExoplanetas["distancia_tierra"])
    df_rankingExoplanetas["orig_idx"] = df_rankingExoplanetas.index
    df_rankingExoplanetas = df_rankingExoplanetas.sort_values(
        "indice_habitabilidad",
        ascending=False
    ).reset_index(drop=True)
    df_rankingExoplanetas.insert(0, "ranking", range(1, len(df_rankingExoplanetas) + 1))

    return df_rankingExoplanetas


def calcular_indice_individual(valor_planeta, reference_vector, df_final, num_cols, p_low=1, p_high=99, family_weights=None):
    if family_weights is None:
        family_weights = {"orbita": 1.0, "planeta": 1.0, "estrella": 1.0}

    vector_ref = pd.Series(reference_vector)[num_cols]
    vector_planeta = pd.Series(valor_planeta)[num_cols]

    p_low_q = df_final[num_cols].quantile(p_low / 100)
    p_high_q = df_final[num_cols].quantile(p_high / 100)
    rango_tipico = (p_high_q - p_low_q).clip(lower=1e-9)

    diferencias = []
    for col in num_cols:
        dif_norm = (vector_planeta[col] - vector_ref[col]) / rango_tipico[col]
        if col in FAMILY_COLS["orbita"]:
            weight = family_weights.get("orbita", 1.0)
        elif col in FAMILY_COLS["planeta"]:
            weight = family_weights.get("planeta", 1.0)
        else:
            weight = family_weights.get("estrella", 1.0)
        diferencias.append(weight * (dif_norm ** 2))

    distancia = np.sqrt(sum(diferencias))
    indice = 1 / (1 + distancia)

    return distancia, indice


def apply_dynamic_filters(df_source, filters):
    df_filtrado = df_source.copy()
    for filtro in filters:
        campo = filtro["campo"]
        operador = filtro["operador"]
        valor = filtro["valor"]

        if campo not in df_filtrado.columns:
            continue
        if operador == "contiene":
            if valor:
                df_filtrado = df_filtrado[
                    df_filtrado[campo].astype(str).str.contains(str(valor), case=False, na=False)
                ]
        elif operador == "==":
            df_filtrado = df_filtrado[df_filtrado[campo] == valor]
        elif operador == ">":
            df_filtrado = df_filtrado[df_filtrado[campo] > valor]
        elif operador == ">=":
            df_filtrado = df_filtrado[df_filtrado[campo] >= valor]
        elif operador == "<":
            df_filtrado = df_filtrado[df_filtrado[campo] < valor]
        elif operador == "<=":
            df_filtrado = df_filtrado[df_filtrado[campo] <= valor]

    return df_filtrado


def render_dynamic_filters(
    df_source,
    filters_key,
    key_prefix,
    nombres_columnas_map,
    nombres_tecnicos_map,
    text_fields,
    numeric_fields,
    reset_on_clear=None
):
    if filters_key not in st.session_state:
        st.session_state[filters_key] = []

    filters = st.session_state[filters_key]

    for idx, filtro in enumerate(filters):
        campo_key = f"campo_{key_prefix}_{idx}"
        operador_key = f"operador_{key_prefix}_{idx}"
        valor_key = f"valor_{key_prefix}_{idx}"

        if campo_key in st.session_state:
            campo_seleccionado = st.session_state[campo_key]
            filtro["campo"] = nombres_tecnicos_map.get(campo_seleccionado, campo_seleccionado)

        if operador_key in st.session_state and filtro["campo"] not in text_fields:
            operadores = {
                "Igual a (=)": "==",
                "Mayor que (>)": ">",
                "Mayor o igual (≥)": ">=",
                "Menor que (<)": "<",
                "Menor o igual (≤)": "<="
            }
            filtro["operador"] = operadores.get(st.session_state[operador_key], filtro["operador"])

        if valor_key in st.session_state:
            filtro["valor"] = st.session_state[valor_key]

    col_titulo, col_agregar, col_limpiar = st.columns([4, 1.5, 1.5])
    with col_titulo:
        st.subheader("Filtros")
    with col_agregar:
        if st.button("Añadir filtro", key=f"add_{key_prefix}", use_container_width=True):
            filters.append({"campo": text_fields[0], "operador": "contiene", "valor": ""})
            st.rerun()
    with col_limpiar:
        if st.button("Limpiar", key=f"clear_{key_prefix}", use_container_width=True):
            if reset_on_clear:
                for state_key, state_value in reset_on_clear.items():
                    st.session_state[state_key] = state_value.copy() if isinstance(state_value, dict) else state_value
            st.session_state[filters_key] = []
            st.rerun()

    if len(filters) == 0:
        st.info("Añade filtros para explorar subconjuntos específicos del dataset.")
        return

    filtros_a_eliminar = []

    for idx, filtro in enumerate(filters):
        campo_actual = filtro["campo"]
        es_texto = campo_actual in text_fields
        if es_texto:
            resumen = f"{nombres_columnas_map.get(campo_actual, campo_actual)} contiene '{filtro['valor']}'"
        else:
            resumen = f"{nombres_columnas_map.get(campo_actual, campo_actual)} {filtro['operador']} {filtro['valor']}"

        with st.expander(resumen, expanded=True):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

            with col1:
                campos_disponibles = text_fields + numeric_fields
                campos_disponibles_natural = [nombres_columnas_map.get(col, col) for col in campos_disponibles]
                campo_actual_natural = nombres_columnas_map.get(campo_actual, campo_actual)
                campo_seleccionado = st.selectbox(
                    "Campo",
                    options=campos_disponibles_natural,
                    index=campos_disponibles_natural.index(campo_actual_natural) if campo_actual_natural in campos_disponibles_natural else 0,
                    key=f"campo_{key_prefix}_{idx}"
                )
                nuevo_campo = nombres_tecnicos_map.get(campo_seleccionado, campo_seleccionado)
                if campo_actual != nuevo_campo:
                    if nuevo_campo in text_fields:
                        filtro["valor"] = ""
                        filtro["operador"] = "contiene"
                    else:
                        serie = pd.to_numeric(df_source[nuevo_campo], errors="coerce")
                        filtro["valor"] = float(serie.median()) if serie.notna().any() else 0.0
                        filtro["operador"] = ">="
                filtro["campo"] = nuevo_campo

            campo_tecnico = filtro["campo"]
            es_campo_texto = campo_tecnico in text_fields

            with col2:
                if es_campo_texto:
                    st.text_input("Operador", value="contiene", disabled=True, key=f"operador_{key_prefix}_{idx}")
                    filtro["operador"] = "contiene"
                else:
                    operadores = {
                        "Igual a (=)": "==",
                        "Mayor que (>)": ">",
                        "Mayor o igual (≥)": ">=",
                        "Menor que (<)": "<",
                        "Menor o igual (≤)": "<="
                    }
                    operador_actual = [k for k, v in operadores.items() if v == filtro.get("operador", ">=")]
                    operador_actual = operador_actual[0] if operador_actual else "Mayor o igual (≥)"
                    operador_seleccionado = st.selectbox(
                        "Operador",
                        options=list(operadores.keys()),
                        index=list(operadores.keys()).index(operador_actual),
                        key=f"operador_{key_prefix}_{idx}"
                    )
                    filtro["operador"] = operadores[operador_seleccionado]

            with col3:
                if es_campo_texto:
                    valor = st.text_input(
                        "Valor",
                        value=str(filtro.get("valor", "")),
                        placeholder="Escribe para buscar",
                        key=f"valor_{key_prefix}_{idx}"
                    )
                    filtro["valor"] = valor
                else:
                    serie = pd.to_numeric(df_source[campo_tecnico], errors="coerce")
                    min_val = float(serie.min()) if serie.notna().any() else 0.0
                    max_val = float(serie.max()) if serie.notna().any() else 1.0
                    if min_val == max_val:
                        min_val -= 1.0
                        max_val += 1.0
                    try:
                        valor_actual = float(filtro.get("valor", min_val))
                    except (TypeError, ValueError):
                        valor_actual = min_val
                    valor_actual = min(max(valor_actual, min_val), max_val)
                    step = (max_val - min_val) / 1000 if max_val > min_val else 0.01
                    valor = st.number_input(
                        "Valor",
                        min_value=min_val,
                        max_value=max_val,
                        value=valor_actual,
                        step=float(step),
                        key=f"valor_{key_prefix}_{idx}",
                        format="%.4f"
                    )
                    filtro["valor"] = valor

            with col4:
                if st.button("✕", key=f"eliminar_{key_prefix}_{idx}", help="Eliminar este filtro"):
                    filtros_a_eliminar.append(idx)

    if filtros_a_eliminar:
        for idx in sorted(filtros_a_eliminar, reverse=True):
            filters.pop(idx)
        st.rerun()


def compute_topn_stability(df_current, df_baseline, top_n):
    top_n = min(top_n, len(df_current), len(df_baseline))
    if top_n <= 0:
        return 0.0, np.nan

    top_curr = set(df_current.head(top_n)["objectid"].astype(str))
    top_base = set(df_baseline.head(top_n)["objectid"].astype(str))
    overlap = len(top_curr.intersection(top_base)) / top_n * 100

    ranks_curr = df_current[["objectid", "ranking"]].rename(columns={"ranking": "ranking_curr"})
    ranks_base = df_baseline[["objectid", "ranking"]].rename(columns={"ranking": "ranking_base"})
    merged = ranks_curr.merge(ranks_base, on="objectid", how="inner")
    spearman = merged["ranking_curr"].corr(merged["ranking_base"], method="spearman")
    return overlap, spearman


# =========================
# FUNCIONES VISUALES
# =========================
def render_top_shell():
    st.markdown("""
    <div class='hero-card'>
        <div class='hero-title'>Exoplanet <span class='hero-highlight'>Habitability</span> Lab</div>
        <div class='hero-subtitle'>
            Herramienta interactiva para explorar el índice de habitabilidad de exoplanetas,
            modificar el vector de referencia terrestre y simular planetas propios dentro del mismo marco analítico.
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_page_header(title, subtitle):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


def render_kpis(df_final, df_rankingExoplanetas):
    planeta_top = df_rankingExoplanetas.iloc[0]["pl_name"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Registros válidos</div>
            <div class="metric-value">{len(df_final)}</div>
            <div class="metric-help">Exoplanetas disponibles</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Sistemas estelares</div>
            <div class="metric-value">{df_final['hostname'].nunique()}</div>
            <div class="metric-help">Estrellas únicas</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Índice medio</div>
            <div class="metric-value">{round(df_rankingExoplanetas['indice_habitabilidad'].mean(), 3)}</div>
            <div class="metric-help">Promedio del ranking</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Primer puesto</div>
            <div class="metric-value-small">{planeta_top}</div>
            <div class="metric-help">Máxima similitud relativa</div>
        </div>
        """, unsafe_allow_html=True)


# =========================
# CARGA Y CÁLCULO
# =========================
df_nasa = cargar_datos()
df_reduced, num_cols = procesar_datos(df_nasa)
df_work = imputar_datos(df_reduced, num_cols)

default_earth_values = {
    "pl_orbper": 365.25,
    "pl_orbsmax": 1.0,
    "pl_orbeccen": 0.0167,
    "pl_rade": 1.0,
    "pl_bmasse": 1.0,
    "pl_dens": 5.51,
    "pl_eqt": 255.0,
    "pl_insol": 1.0,
    "st_teff": 5778.0,
    "st_lum": 0.0,
    "st_mass": 1.0,
    "st_rad": 1.0,
    "st_met": 0.0,
    "st_logg": 4.44,
    "st_age": 4.6
}

if "earth_values" not in st.session_state:
    st.session_state.earth_values = default_earth_values.copy()

if "sensitivity_params" not in st.session_state:
    st.session_state.sensitivity_params = DEFAULT_SENSITIVITY.copy()

if "sensitivity_draft" not in st.session_state:
    st.session_state.sensitivity_draft = st.session_state.sensitivity_params.copy()

sensitivity = st.session_state.sensitivity_params

family_weights = {
    "orbita": float(sensitivity["weight_orbita"]),
    "planeta": float(sensitivity["weight_planeta"]),
    "estrella": float(sensitivity["weight_estrella"])
}

df_final = gestionar_outliers(
    df_work,
    num_cols,
    threshold=float(sensitivity["winsor_threshold"])
)

df_final_baseline = gestionar_outliers(
    df_work,
    num_cols,
    threshold=float(DEFAULT_SENSITIVITY["winsor_threshold"])
)

df_rankingExoplanetas = calcular_indices_habitabilidad(
    df_final,
    num_cols,
    st.session_state.earth_values,
    p_low=int(sensitivity["p_low"]),
    p_high=int(sensitivity["p_high"]),
    family_weights=family_weights,
    df_original=df_work,
    df_csv=df_reduced
)

df_ranking_baseline = calcular_indices_habitabilidad(
    df_final_baseline,
    num_cols,
    st.session_state.earth_values,
    p_low=int(DEFAULT_SENSITIVITY["p_low"]),
    p_high=int(DEFAULT_SENSITIVITY["p_high"]),
    family_weights={
        "orbita": DEFAULT_SENSITIVITY["weight_orbita"],
        "planeta": DEFAULT_SENSITIVITY["weight_planeta"],
        "estrella": DEFAULT_SENSITIVITY["weight_estrella"]
    },
    df_original=df_work,
    df_csv=df_reduced
)

nombres_columnas = {
    "objectid": "ID NASA",
    "pl_name": "Nombre del Planeta",
    "hostname": "Estrella",
    "pl_orbper": "Periodo Orbital (días)",
    "pl_orbsmax": "Distancia Orbital (AU)",
    "pl_orbeccen": "Excentricidad Orbital",
    "pl_rade": "Radio del Planeta (R⊕)",
    "pl_bmasse": "Masa del Planeta (M⊕)",
    "pl_dens": "Densidad del Planeta (g/cm³)",
    "pl_eqt": "Temperatura de Equilibrio (K)",
    "pl_insol": "Radiación Recibida",
    "st_teff": "Temperatura Estelar (K)",
    "st_lum": "Luminosidad Estelar (log)",
    "st_mass": "Masa Estelar (M☉)",
    "st_rad": "Radio Estelar (R☉)",
    "st_met": "Metalicidad Estelar [Fe/H]",
    "st_logg": "Gravedad Superficial Estelar (log g)",
    "st_age": "Edad Estelar (Gyr)"
}

nombres_tecnicos = {v: k for k, v in nombres_columnas.items()}

nombres_columnas_ranking = {
    **nombres_columnas,
    "ranking": "Orden",
    "indice_habitabilidad": "Índice de Habitabilidad",
    "distancia_tierra": "Distancia a la Tierra (normalizada)"
}

nombres_tecnicos_ranking = {v: k for k, v in nombres_columnas_ranking.items()}

# =========================
# SHELL SUPERIOR
# =========================
render_top_shell()

PAGES = [
    "Inicio",
    "Ranking",
    "Vector Tierra",
    "Simulador",
    "Correlaciones",
    "Temperatura",
    "Estrellas"
]


# pagina = st.radio(
#   "Navegación principal",
#    PAGES,
#    horizontal=True,
#   label_visibility="collapsed"
#)

if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"

cols = st.columns(len(PAGES))
for i, page in enumerate(PAGES):
    with cols[i]:
        if st.button(page, key=f"nav_{i}", use_container_width=True):
            st.session_state.pagina = page

pagina = st.session_state.pagina

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# =========================
# PÁGINAS
# =========================
if pagina == "Inicio":
    render_page_header(
        "Dataset de exoplanetas",
        "Exploración tabular del dataset procesado, con filtros dinámicos y estadísticas descriptivas."
    )
    render_kpis(df_final, df_rankingExoplanetas)
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    if "filtros" not in st.session_state:
        st.session_state.filtros = []

    df_filtrado = apply_dynamic_filters(df_final, st.session_state.filtros)

    if len(df_filtrado) > 0:
        tab1, tab2 = st.tabs(["Vista de datos", "Estadísticas"])

        with tab1:
            render_dynamic_filters(
                df_source=df_final,
                filters_key="filtros",
                key_prefix="dataset",
                nombres_columnas_map=nombres_columnas,
                nombres_tecnicos_map=nombres_tecnicos,
                text_fields=["pl_name", "hostname"],
                numeric_fields=num_cols
            )

            df_filtrado = apply_dynamic_filters(df_final, st.session_state.filtros)
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

            df_mostrar = df_filtrado.copy().rename(columns=nombres_columnas)

            column_config = {
                nombres_columnas["pl_name"]: st.column_config.TextColumn(
                    nombres_columnas["pl_name"],
                    width="medium",
                    pinned=True
                )
            }

            st.dataframe(
                df_mostrar,
                use_container_width=True,
                height=650,
                column_config=column_config,
                hide_index=True
            )

            st.caption(
                f"Mostrando {len(df_filtrado)} de {len(df_final)} exoplanetas · "
                f"{df_filtrado['hostname'].nunique()} estrellas únicas"
            )

        with tab2:
            vars_stats = num_cols

            if vars_stats:
                df_stats = df_filtrado[vars_stats].describe().T
                df_stats.index = df_stats.index.map(lambda x: nombres_columnas.get(x, x))

                st.dataframe(df_stats, use_container_width=True, hide_index=False)
                st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

                num_vars = min(len(vars_stats), 12)

                if num_vars > 0:
                    okabe_ito_colors = [
                        "#E69F00", "#56B4E9", "#009E73",
                        "#F0E442", "#0072B2", "#D55E00", "#CC79A7"
                    ]

                    cols_per_row = 3
                    num_rows = (num_vars + cols_per_row - 1) // cols_per_row

                    fig, axes = plt.subplots(num_rows, cols_per_row, figsize=(15, 4 * num_rows))
                    axes = axes.flatten() if num_vars > 1 else [axes]

                    for idx, var in enumerate(vars_stats[:12]):
                        ax = axes[idx]
                        color = okabe_ito_colors[idx % len(okabe_ito_colors)]
                        df_filtrado[var].hist(bins=30, ax=ax, color=color, edgecolor="black", alpha=0.7)
                        ax.set_title(nombres_columnas.get(var, var), fontweight="bold", fontsize=10)
                        ax.set_xlabel("")
                        ax.set_ylabel("Frecuencia", fontsize=9)

                    for idx in range(num_vars, len(axes)):
                        axes[idx].axis("off")

                    plt.tight_layout()
                    st.pyplot(fig)
    else:
        st.warning("No se encontraron resultados. Ajusta los filtros.")

elif pagina == "Ranking":
    render_page_header(
        "Índice de habitabilidad",
        "Ranking interactivo basado en similitud relativa con el vector de referencia terrestre y sensibilidad configurable."
    )
    render_kpis(df_final, df_rankingExoplanetas)
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    if "filtros_ranking" not in st.session_state:
        st.session_state.filtros_ranking = []
    if "sensitivity_draft" not in st.session_state:
        st.session_state.sensitivity_draft = st.session_state.sensitivity_params.copy()

    with st.expander("Ajustes de sensibilidad del índice", expanded=False):
        draft = st.session_state.sensitivity_draft
        col1, col2, col3 = st.columns(3)

        with col1:
            draft["winsor_threshold"] = st.slider("Winsor (Tukey IQR)", 0.5, 3.0, float(draft["winsor_threshold"]), 0.1)
            draft["weight_orbita"] = st.slider("Peso órbita", 0.0, 3.0, float(draft["weight_orbita"]), 0.1)

        with col2:
            draft["p_low"] = st.slider("Percentil inferior", 0, 20, int(draft["p_low"]), 1)
            draft["weight_planeta"] = st.slider("Peso planeta", 0.0, 3.0, float(draft["weight_planeta"]), 0.1)

        with col3:
            min_p_high = int(draft["p_low"]) + 1
            draft["p_high"] = st.slider("Percentil superior", min_p_high, 100, max(int(draft["p_high"]), min_p_high), 1)
            draft["weight_estrella"] = st.slider("Peso estrella", 0.0, 3.0, float(draft["weight_estrella"]), 0.1)

        draft["stability_top_n"] = st.slider("Top-N para estabilidad", 5, 200, int(draft["stability_top_n"]), 5)

        c_apply, c_reset = st.columns([1, 1])
        with c_apply:
            if st.button("Actualizar índice", use_container_width=True, type="primary"):
                st.session_state.sensitivity_params = st.session_state.sensitivity_draft.copy()
                st.rerun()
        with c_reset:
            if st.button("Restaurar valores por defecto", use_container_width=True):
                st.session_state.sensitivity_params = DEFAULT_SENSITIVITY.copy()
                st.session_state.sensitivity_draft = DEFAULT_SENSITIVITY.copy()
                st.rerun()

        overlap_pct, spearman = compute_topn_stability(
            df_rankingExoplanetas,
            df_ranking_baseline,
            int(st.session_state.sensitivity_params["stability_top_n"])
        )
        m1, m2 = st.columns(2)
        with m1:
            st.metric("Solapamiento Top-N vs base", f"{overlap_pct:.1f}%")
        with m2:
            spearman_txt = "N/A" if pd.isna(spearman) else f"{spearman:.3f}"
            st.metric("Spearman ranking vs base", spearman_txt)

    df_filtrado = apply_dynamic_filters(df_rankingExoplanetas, st.session_state.filtros_ranking)

    if len(df_filtrado) > 0:
        tab1, tab2, tab3, tab4 = st.tabs([
            "Ranking",
            "Análisis del índice",
            "Distribución",
            "Relaciones"
        ])

        with tab1:
            render_dynamic_filters(
                df_source=df_rankingExoplanetas,
                filters_key="filtros_ranking",
                key_prefix="ranking",
                nombres_columnas_map=nombres_columnas_ranking,
                nombres_tecnicos_map=nombres_tecnicos_ranking,
                text_fields=["pl_name", "hostname"],
                numeric_fields=["ranking", "indice_habitabilidad", "distancia_tierra"] + num_cols,
                reset_on_clear={
                    "sensitivity_params": DEFAULT_SENSITIVITY.copy(),
                    "sensitivity_draft": DEFAULT_SENSITIVITY.copy()
                }
            )

            df_filtrado = apply_dynamic_filters(df_rankingExoplanetas, st.session_state.filtros_ranking)
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

            columnas_principales = ["ranking", "pl_name", "hostname", "indice_habitabilidad", "distancia_tierra"]
            df_mostrar = df_filtrado[columnas_principales].copy().rename(columns=nombres_columnas_ranking)

            column_config = {
                nombres_columnas_ranking["ranking"]: st.column_config.NumberColumn(
                    nombres_columnas_ranking["ranking"],
                    width="small",
                    pinned=True
                )
            }

            st.dataframe(
                df_mostrar,
                use_container_width=True,
                height=650,
                column_config=column_config,
                hide_index=True
            )

            st.caption(
                f"Mostrando {len(df_filtrado)} de {len(df_rankingExoplanetas)} exoplanetas · "
                f"Índice medio del subconjunto: {df_filtrado['indice_habitabilidad'].mean():.4f}"
            )

            with st.expander("Detalle de variables", expanded=False):
                planeta_sel = st.selectbox("Planeta", options=df_filtrado["pl_name"].tolist(), key="trace_planet")
                vars_sel = st.multiselect("Variables", options=num_cols, default=num_cols[:5], key="trace_vars")

                if vars_sel:
                    fila = df_rankingExoplanetas.loc[df_rankingExoplanetas["pl_name"] == planeta_sel].iloc[0]
                    df_trace = pd.DataFrame({
                        "Variable": [nombres_columnas.get(c, c) for c in vars_sel],
                        "valor_csv": [fila[f"{c}_csv"] for c in vars_sel],
                        "valor_imputado": [fila[f"{c}_imputado"] for c in vars_sel],
                        "valor_raw": [fila[f"{c}_raw"] for c in vars_sel],
                        "valor_norm": [fila[f"{c}_norm"] for c in vars_sel]
                    })
                    st.dataframe(df_trace, use_container_width=True, hide_index=True)

        with tab2:
            fig, axes = plt.subplots(1, 2, figsize=(16, 6))

            axes[0].plot(df_filtrado["ranking"], df_filtrado["indice_habitabilidad"], linewidth=1.6, color="#56B4E9")
            axes[0].set_xlabel("Posición en el ranking")
            axes[0].set_ylabel("Índice")
            axes[0].set_title("Decaimiento del índice a lo largo del ranking")
            axes[0].grid(alpha=0.3)
            axes[0].axhline(df_filtrado["indice_habitabilidad"].median(), linestyle="--", linewidth=1.5, color="red")

            top_100 = df_filtrado.head(100)
            axes[1].plot(top_100["ranking"], top_100["indice_habitabilidad"], linewidth=2, marker="o", markersize=3, color="#56B4E9")
            axes[1].set_xlabel("Posición")
            axes[1].set_ylabel("Índice")
            axes[1].set_title("Detalle del top 100")
            axes[1].grid(alpha=0.3)

            plt.tight_layout()
            st.pyplot(fig)

        with tab3:
            fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))
            indice = df_filtrado["indice_habitabilidad"]

            sns.histplot(indice, bins=40, kde=True, ax=axes2[0], color="#56B4E9", edgecolor="black", alpha=0.7)
            axes2[0].set_title("Distribución del índice")
            axes2[0].set_xlabel("Índice")
            axes2[0].set_ylabel("Frecuencia")
            axes2[0].grid(alpha=0.3)

            sns.boxplot(x=indice, ax=axes2[1], color="#7dd3fc")
            axes2[1].set_title("Boxplot del índice")
            axes2[1].set_xlabel("Índice")
            axes2[1].grid(alpha=0.3, axis="x")

            plt.tight_layout()
            st.pyplot(fig2)

        with tab4:
            fig3, axes3 = plt.subplots(2, 2, figsize=(14, 10))

            axes3[0, 0].scatter(df_filtrado["pl_rade"], df_filtrado["indice_habitabilidad"], alpha=0.6, s=20, color="#e91e8c")
            axes3[0, 0].set_xlabel("Radio planetario")
            axes3[0, 0].set_ylabel("Índice")
            axes3[0, 0].set_title("Índice vs radio planetario")
            axes3[0, 0].grid(alpha=0.3)

            axes3[0, 1].scatter(df_filtrado["pl_insol"], df_filtrado["indice_habitabilidad"], alpha=0.6, s=20, color="#009E73")
            axes3[0, 1].set_xlabel("Radiación recibida")
            axes3[0, 1].set_ylabel("Índice")
            axes3[0, 1].set_title("Índice vs radiación")
            axes3[0, 1].grid(alpha=0.3)

            axes3[1, 0].scatter(df_filtrado["st_teff"], df_filtrado["indice_habitabilidad"], alpha=0.6, s=20, color="#E69F00")
            axes3[1, 0].set_xlabel("Temperatura estelar")
            axes3[1, 0].set_ylabel("Índice")
            axes3[1, 0].set_title("Índice vs temperatura estelar")
            axes3[1, 0].grid(alpha=0.3)

            axes3[1, 1].scatter(df_filtrado["pl_eqt"], df_filtrado["indice_habitabilidad"], alpha=0.6, s=20, color="#56B4E9")
            axes3[1, 1].set_xlabel("Temperatura de equilibrio")
            axes3[1, 1].set_ylabel("Índice")
            axes3[1, 1].set_title("Índice vs temperatura de equilibrio")
            axes3[1, 1].grid(alpha=0.3)

            plt.tight_layout()
            st.pyplot(fig3)

    else:
        st.warning("No se encontraron resultados. Ajusta los filtros.")

elif pagina == "Vector Tierra":
    render_page_header(
        "Vector de referencia terrestre",
        "Ajuste manual del vector de referencia empleado en el cálculo del índice de habitabilidad."
    )

    col_reset, col_info = st.columns([1, 1])

    with col_reset:
        if st.button("Restaurar valores de la Tierra", use_container_width=True):
            st.session_state.earth_values = default_earth_values.copy()
            st.rerun()

    with col_info:
        st.info("El ranking se recalcula automáticamente al cambiar el vector de referencia")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.subheader("Parámetros orbitales")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.session_state.earth_values["pl_orbper"] = st.number_input("Periodo orbital (días)", value=float(st.session_state.earth_values["pl_orbper"]), min_value=0.0, format="%.2f")
    with col2:
        st.session_state.earth_values["pl_orbsmax"] = st.number_input("Distancia orbital (AU)", value=float(st.session_state.earth_values["pl_orbsmax"]), min_value=0.0, format="%.4f")
    with col3:
        st.session_state.earth_values["pl_orbeccen"] = st.number_input("Excentricidad orbital", value=float(st.session_state.earth_values["pl_orbeccen"]), min_value=0.0, max_value=1.0, format="%.4f")

    st.subheader("Parámetros planetarios")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.session_state.earth_values["pl_rade"] = st.number_input("Radio del planeta (R⊕)", value=float(st.session_state.earth_values["pl_rade"]), min_value=0.0, format="%.4f")
    with col2:
        st.session_state.earth_values["pl_bmasse"] = st.number_input("Masa del planeta (M⊕)", value=float(st.session_state.earth_values["pl_bmasse"]), min_value=0.0, format="%.4f")
    with col3:
        st.session_state.earth_values["pl_dens"] = st.number_input("Densidad (g/cm³)", value=float(st.session_state.earth_values["pl_dens"]), min_value=0.0, format="%.2f")

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.earth_values["pl_eqt"] = st.number_input("Temperatura de equilibrio (K)", value=float(st.session_state.earth_values["pl_eqt"]), min_value=0.0, format="%.1f")
    with col2:
        st.session_state.earth_values["pl_insol"] = st.number_input("Radiación recibida", value=float(st.session_state.earth_values["pl_insol"]), min_value=0.0, format="%.4f")

    st.subheader("Parámetros estelares")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.session_state.earth_values["st_teff"] = st.number_input("Temperatura estelar (K)", value=float(st.session_state.earth_values["st_teff"]), min_value=0.0, format="%.1f")
    with col2:
        st.session_state.earth_values["st_mass"] = st.number_input("Masa estelar (M☉)", value=float(st.session_state.earth_values["st_mass"]), min_value=0.0, format="%.4f")
    with col3:
        st.session_state.earth_values["st_rad"] = st.number_input("Radio estelar (R☉)", value=float(st.session_state.earth_values["st_rad"]), min_value=0.0, format="%.4f")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.earth_values["st_lum"] = st.number_input("Luminosidad estelar (log)", value=float(st.session_state.earth_values["st_lum"]), format="%.4f")
    with col2:
        st.session_state.earth_values["st_met"] = st.number_input("Metalicidad estelar [Fe/H]", value=float(st.session_state.earth_values["st_met"]), format="%.4f")
    with col3:
        st.session_state.earth_values["st_logg"] = st.number_input("Gravedad superficial (log g)", value=float(st.session_state.earth_values["st_logg"]), min_value=0.0, format="%.2f")

    st.session_state.earth_values["st_age"] = st.number_input("Edad estelar (Gyr)", value=float(st.session_state.earth_values["st_age"]), min_value=0.0, format="%.2f")

elif pagina == "Simulador":
    render_page_header(
        "Simulador de planeta",
        "Construye un planeta hipotético, calcula su índice de habitabilidad y compáralo con el ranking observado."
    )

    st.subheader("Parámetros orbitales")
    col1, col2, col3 = st.columns(3)

    with col1:
        pl_orbper = st.number_input("Periodo orbital (días)", value=365.25, min_value=0.1, format="%.2f")
    with col2:
        pl_orbsmax = st.number_input("Distancia orbital (AU)", value=1.0, min_value=0.01, format="%.4f")
    with col3:
        pl_orbeccen = st.number_input("Excentricidad orbital", value=0.0167, min_value=0.0, max_value=0.99, format="%.4f")

    st.subheader("Parámetros del planeta")
    col1, col2, col3 = st.columns(3)

    with col1:
        pl_rade = st.number_input("Radio del planeta (R⊕)", value=1.0, min_value=0.1, format="%.3f")
    with col2:
        pl_bmasse = st.number_input("Masa del planeta (M⊕)", value=1.0, min_value=0.01, format="%.3f")
    with col3:
        pl_dens = st.number_input("Densidad (g/cm³)", value=5.51, min_value=0.1, format="%.2f")

    col1, col2 = st.columns(2)
    with col1:
        pl_eqt = st.number_input("Temperatura de equilibrio (K)", value=255.0, min_value=0.0, format="%.1f")
    with col2:
        pl_insol = st.number_input("Radiación recibida", value=1.0, min_value=0.01, format="%.3f")

    st.subheader("Parámetros de la estrella")
    col1, col2, col3 = st.columns(3)

    with col1:
        st_teff = st.number_input("Temperatura estelar (K)", value=5778.0, min_value=1000.0, format="%.1f")
    with col2:
        st_mass = st.number_input("Masa estelar (M☉)", value=1.0, min_value=0.1, format="%.3f")
    with col3:
        st_rad = st.number_input("Radio estelar (R☉)", value=1.0, min_value=0.1, format="%.3f")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st_lum = st.number_input("Luminosidad estelar (log)", value=0.0, format="%.3f")
    with col2:
        st_met = st.number_input("Metalicidad [Fe/H]", value=0.0, format="%.3f")
    with col3:
        st_logg = st.number_input("Gravedad superficial (log g)", value=4.44, min_value=0.0, format="%.2f")
    with col4:
        st_age = st.number_input("Edad estelar (Gyr)", value=4.6, min_value=0.0, format="%.2f")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    if st.button("Calcular índice de habitabilidad", type="primary", use_container_width=True):
        valor_planeta = {
            "pl_orbper": pl_orbper,
            "pl_orbsmax": pl_orbsmax,
            "pl_orbeccen": pl_orbeccen,
            "pl_rade": pl_rade,
            "pl_bmasse": pl_bmasse,
            "pl_dens": pl_dens,
            "pl_eqt": pl_eqt,
            "pl_insol": pl_insol,
            "st_teff": st_teff,
            "st_lum": st_lum,
            "st_mass": st_mass,
            "st_rad": st_rad,
            "st_met": st_met,
            "st_logg": st_logg,
            "st_age": st_age
        }

        distancia, indice = calcular_indice_individual(
            valor_planeta,
            st.session_state.earth_values,
            df_final,
            num_cols,
            p_low=int(st.session_state.sensitivity_params["p_low"]),
            p_high=int(st.session_state.sensitivity_params["p_high"]),
            family_weights={
                "orbita": float(st.session_state.sensitivity_params["weight_orbita"]),
                "planeta": float(st.session_state.sensitivity_params["weight_planeta"]),
                "estrella": float(st.session_state.sensitivity_params["weight_estrella"])
            }
        )

        mejores = (df_rankingExoplanetas["indice_habitabilidad"] > indice).sum()
        posicion = mejores + 1

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Índice de habitabilidad", f"{indice:.6f}")
        with col2:
            st.metric("Distancia al vector de referencia", f"{distancia:.4f}")
        with col3:
            st.metric("Posición estimada", f"#{posicion} / {len(df_rankingExoplanetas)}")

        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.hist(df_rankingExoplanetas["indice_habitabilidad"], bins=50, edgecolor="black", alpha=0.7)
        ax.axvline(indice, linestyle="--", linewidth=3, color="red", label=f"Tu planeta: {indice:.6f}")
        ax.set_xlabel("Índice de habitabilidad")
        ax.set_ylabel("Frecuencia")
        ax.set_title("Distribución de índices frente a tu planeta")
        ax.legend()
        ax.grid(alpha=0.3)
        st.pyplot(fig)

elif pagina == "Correlaciones":
    render_page_header(
        "Exploración bivariante y correlacional",
        "Selección libre de variables para analizar relaciones, distribuciones y matriz de correlación."
    )

    col1, col2 = st.columns(2)
    with col1:
        var_x = st.selectbox("Variable X", num_cols, index=0)
    with col2:
        var_y = st.selectbox("Variable Y", num_cols, index=1)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Scatter",
        "Distribuciones",
        "Resumen estadístico",
        "Correlación"
    ])

    with tab1:
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df_final[var_x], df_final[var_y], alpha=0.6, c=df_final["pl_eqt"], cmap="coolwarm", s=50)
        ax.set_xlabel(var_x)
        ax.set_ylabel(var_y)
        ax.set_title(f"{var_x} vs {var_y}")
        plt.colorbar(scatter, label="Temperatura equilibrio", ax=ax)
        st.pyplot(fig)

    with tab2:
        c1, c2 = st.columns(2)

        with c1:
            fig, ax = plt.subplots(figsize=(8, 5))
            df_final[var_x].hist(bins=50, ax=ax, edgecolor="black")
            ax.set_title(f"Distribución de {var_x}")
            ax.set_xlabel(var_x)
            ax.set_ylabel("Frecuencia")
            st.pyplot(fig)

        with c2:
            fig, ax = plt.subplots(figsize=(8, 5))
            df_final[var_y].hist(bins=50, ax=ax, edgecolor="black")
            ax.set_title(f"Distribución de {var_y}")
            ax.set_xlabel(var_y)
            ax.set_ylabel("Frecuencia")
            st.pyplot(fig)

    with tab3:
        c1, c2 = st.columns(2)

        with c1:
            st.write(f"**Estadísticas de {var_x}**")
            st.write(df_final[var_x].describe())

        with c2:
            st.write(f"**Estadísticas de {var_y}**")
            st.write(df_final[var_y].describe())

        st.write(f"**Correlación:** {df_final[[var_x, var_y]].corr().iloc[0, 1]:.3f}")

    with tab4:
        variables_sel = st.multiselect(
            "Variables para la matriz de correlación",
            num_cols,
            default=num_cols[:8],
            key="corr_vars"
        )

        if len(variables_sel) >= 2:
            fig, ax = plt.subplots(figsize=(12, 10))
            corr_matrix = df_final[variables_sel].corr()
            sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0, square=True, linewidths=1, ax=ax)
            ax.set_title("Matriz de correlación")
            st.pyplot(fig)
        else:
            st.warning("Selecciona al menos 2 variables.")

elif pagina == "Temperatura":
    render_page_header(
        "Análisis térmico",
        "Exploración de temperaturas de equilibrio y rango térmico seleccionado."
    )

    temp_range = st.slider(
        "Selecciona rango de temperatura (K)",
        int(df_final["pl_eqt"].min()),
        int(df_final["pl_eqt"].max()),
        (200, 400)
    )

    df_temp = df_final[
        (df_final["pl_eqt"] >= temp_range[0]) &
        (df_final["pl_eqt"] <= temp_range[1])
    ]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Exoplanetas en rango", len(df_temp))
    with col2:
        st.metric("Temperatura media", f"{df_temp['pl_eqt'].mean():.1f} K")
    with col3:
        st.metric("Desviación estándar", f"{df_temp['pl_eqt'].std():.1f} K")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df_final["pl_eqt"], bins=50,  color="#4fc3f7", edgecolor="black", alpha=0.7)
        ax.axvline(273, linestyle="--", linewidth=2, color="#00e5ff", label="Congelación H₂O (273K)")
        ax.axvline(373, linestyle="--", linewidth=2, color="red", label="Ebullición H₂O (373K)")
        ax.axvspan(temp_range[0], temp_range[1], alpha=0.2, color="pink", label="Rango seleccionado")
        ax.set_xlabel("Temperatura de equilibrio (K)")
        ax.set_ylabel("Frecuencia")
        ax.set_title("Distribución térmica")
        ax.legend()
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df_final["pl_rade"], df_final["pl_eqt"], alpha=0.6, c=df_final["pl_bmasse"], cmap="cool", s=50)
        ax.set_xlabel("Radio del planeta")
        ax.set_ylabel("Temperatura de equilibrio (K)")
        ax.set_title("Temperatura vs radio planetario")
        ax.axhline(273, linestyle="--", alpha=0.5, color="blue")
        ax.axhline(373, linestyle="--", alpha=0.5, color="red")
        plt.colorbar(scatter, label="Masa (M⊕)", ax=ax)
        st.pyplot(fig)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.dataframe(
        df_temp[["pl_name", "hostname", "pl_eqt", "pl_rade", "pl_bmasse", "pl_orbsmax"]].sort_values("pl_eqt"),
        use_container_width=True
    )

elif pagina == "Estrellas":
    render_page_header(
        "Características estelares",
        "Análisis visual de masa, radio, temperatura, luminosidad y edad de las estrellas anfitrionas."
    )

    c1, c2 = st.columns(2)

    with c1:
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df_final["st_mass"], df_final["st_rad"], alpha=0.6, c=df_final["st_teff"], cmap="hot", s=50)
        ax.set_xlabel("Masa estelar")
        ax.set_ylabel("Radio estelar")
        ax.set_title("Relación masa-radio estelar")
        plt.colorbar(scatter, label="Temperatura estelar (K)", ax=ax)
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df_final["st_teff"], df_final["st_lum"], alpha=0.6, c=df_final["st_age"], cmap="viridis", s=50)
        ax.set_xlabel("Temperatura estelar (K)")
        ax.set_ylabel("Luminosidad (log)")
        ax.set_title("Temperatura vs luminosidad")
        plt.colorbar(scatter, label="Edad estelar (Gyr)", ax=ax)
        st.pyplot(fig)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df_final["st_mass"], bins=40, edgecolor="black", alpha=0.7, color="gold")
        ax.axvline(1.0, linestyle="--", linewidth=2, color="red", label="Masa solar")
        ax.set_xlabel("Masa estelar (M☉)")
        ax.set_ylabel("Frecuencia")
        ax.legend()
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df_final["st_teff"], bins=40, edgecolor="black", alpha=0.7, color="orangered")
        ax.axvline(5778, linestyle="--", linewidth=2, color="yellow", label="Temp. solar")
        ax.set_xlabel("Temperatura (K)")
        ax.set_ylabel("Frecuencia")
        ax.legend()
        st.pyplot(fig)

    with c3:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df_final["st_age"], bins=40, edgecolor="black", alpha=0.7, color="steelblue")
        ax.axvline(4.6, linestyle="--", linewidth=2, color="orange", label="Edad solar")
        ax.set_xlabel("Edad (Gyr)")
        ax.set_ylabel("Frecuencia")
        ax.legend()
        st.pyplot(fig)

st.markdown("""
    <div style='
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        border-top: 1px solid rgba(233, 30, 140, 0.15);
        color: rgba(255,255,255,0.4);
        font-size: 0.82rem;
        letter-spacing: 0.3px;
    '>
        Datos: <a href="https://exoplanetarchive.ipac.caltech.edu/" target="_blank"
            style="color: #4fc3f7; text-decoration: none;">NASA Exoplanet Archive</a>
        &nbsp;·&nbsp;
        Desarrollado por <span style="color: #e91e8c; font-weight: 600;">Alejandro Barriel</span>
        &nbsp;·&nbsp;
        <a href="https://alejandrobarriel.com" target="_blank"
            style="color: #4fc3f7; text-decoration: none;">alejandrobarriel.com</a>
    </div>
""", unsafe_allow_html=True)