# -*- coding: utf-8 -*-

# Commented out IPython magic to ensure Python compatibility.
#@title PD Validator: Jeffreys Test (EBA Compliant)
#@markdown Inserisci i dati e clicca Play. 

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
import pandas as pd

# ---
# %config InlineBackend.figure_format = 'retina'
plt.rcParams['figure.facecolor'] = 'white'

# --- INPUT DATI ---
nome_modello = "Portafoglio Mutui Retail" #@param {type:"string"}
defaults = 13453 #@param {type:"integer"}
goods = 345000 #@param {type:"integer"}
PD_modello = 0.038 #@param {type:"number"}
alpha_significativita = 0.05 #@param {type:"slider", min:0.01, max:0.1, step:0.01}

def run_professional_validation(def_obs, goo_obs, pd_mod, alpha, label):
    # 1. Calcoli Statistici
    n = def_obs + goo_obs
    if n == 0: return print("Errore: Portafoglio vuoto")

    td_obs = def_obs / n
    a, b = def_obs + 0.5, goo_obs + 0.5 # Jeffreys Prior

    p_value = beta.cdf(pd_mod, a, b)
    critical_pd = beta.ppf(alpha, a, b)

    # 2. Logica EBA
    if p_value > 0.05:
        status, color, emoji = "VERDE (Adeguato)", "#2ecc71", "🟢"
    elif 0.01 < p_value <= 0.05:
        status, color, emoji = "GIALLO (Monitoraggio)", "#f1c40f", "🟡"
    else:
        status, color, emoji = "ROSSO (Ricalibrazione)", "#e74c3c", "🔴"

    # 3. Output Testuale Professionale
    print(f"\n{emoji} ESITO VALIDAZIONE: {status}")
    print("-" * 50)
    data = {
        "Metrica": ["Segmento", "N. Controparti", "Default", "Default Rate (TD)", "PD Modello", "p-value", "Soglia Critica"],
        "Valore": [label, f"{n:,}", f"{def_obs:,}", f"{td_obs:.4%}", f"{pd_mod:.4%}", f"{p_value:.4f}", f"{critical_pd:.4%}"]
    }
    print(pd.DataFrame(data).to_string(index=False))
    print("-" * 50)

    # 4.
    std_dev = np.sqrt((a * b) / ((a + b)**2 * (a + b + 1)))
    x = np.linspace(max(0, td_obs - 4*std_dev), min(1, td_obs + 4*std_dev), 1000)
    pdf = beta.pdf(x, a, b)

    fig, ax = plt.subplots(figsize=(11, 6))

    #
    ax.plot(x, pdf, color='#2c3e50', lw=2.5, label='Distribuzione Beta (Jeffreys Prior)')
    ax.fill_between(x, 0, pdf, color='#34495e', alpha=0.1)

    #
    x_crit = np.linspace(x.min(), critical_pd, 100)
    ax.fill_between(x_crit, beta.pdf(x_crit, a, b), color='#e74c3c', alpha=0.4, label=f'Zona di Sottostima (p < {alpha})')

    #
    ax.axvline(td_obs, color='black', lw=1.5, label=f'TD Osservato ({td_obs:.2%})')
    ax.axvline(pd_mod, color=color, linestyle='--', lw=3, label=f'PD Modello ({pd_mod:.2%})')

    #
    ax.set_title(f"Backtesting PD - {label}", fontsize=15, fontweight='bold', pad=20)
    ax.set_xlabel("Probability of Default (PD)", fontsize=11)
    ax.set_ylabel("Densità di Probabilità", fontsize=11)
    ax.legend(loc='upper right', frameon=True, shadow=True, fontsize=9)
    ax.grid(True, linestyle=':', alpha=0.6)

    #
    ax.set_ylim(bottom=0)
    ax.set_xlim(x.min(), x.max())

    # Esito
    ax.text(0.02, 0.93, f"STATUS: {status}", transform=ax.transAxes,
            fontsize=11, fontweight='bold', color='white',
            bbox=dict(facecolor=color, alpha=0.8, edgecolor='none', boxstyle='round,pad=0.5'))

    plt.tight_layout()

    # Salvataggio file
    filename = f"validazione_{label.replace(' ', '_')}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"✅ Grafico salvato come: {filename}")

# Esecuzione
run_professional_validation(defaults, goods, PD_modello, alpha_significativita, nome_modello)
