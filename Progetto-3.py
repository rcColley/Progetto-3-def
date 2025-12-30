import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random 

nome = "Mario Rossi"
eta = 34
saldo_conto = 2500.75
vip = True

destinazioni = ["Roma", "Parigi", "New York", "Tokyo", "Cairo"]

prezzi_destinazioni = {
    "Roma": 450,
    "Parigi": 600,
    "New York": 1200,
    "Tokyo": 1500,
    "Cairo": 700
}
#------------------------------------------------------

class Cliente:
    def __init__(self, nome, eta, vip=False):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def info(self):
        print(f"Cliente: {self.nome}, Età: {self.eta}, VIP: {self.vip}")

class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata


class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

    def importo_finale(self):
        if self.cliente.vip:
            return self.viaggio.prezzo * 0.9
        return self.viaggio.prezzo

    def dettagli(self):
        print("---- Dettagli Prenotazione ----")
        self.cliente.info()
        print(f"Destinazione: {self.viaggio.destinazione}")
        print(f"Durata: {self.viaggio.durata} giorni")
        print(f"Prezzo finale: €{self.importo_finale():.2f}")

#------------------------------------------------------

prezzi = np.random.uniform(200, 4000, 100)

media = np.mean(prezzi)
minimo = np.min(prezzi)
massimo = np.max(prezzi)
dev_std = np.std(prezzi)
percentuale_sopra_media = np.sum(prezzi > media) / len(prezzi) * 100

print("Prezzo medio:", media)
print("Min:", minimo, "Max:", massimo)
print("Deviazione standard:", dev_std)
print("Prenotazioni sopra la media:", percentuale_sopra_media, "%")

#------------------------------------------------------

np.random.seed(42)

df = pd.DataFrame({
    "Cliente": np.random.choice(["Riccardo", "Luca", "Anna", "Giulia", "Marco"], 100),
    "Destinazione": np.random.choice(destinazioni, 100),
    "Prezzo": np.random.uniform(200, 4000, 100),
    "Giorno_Partenza": np.random.randint(1, 31, 100),
    "Durata": np.random.randint(3, 15, 100)
})

df["Incasso"] = df["Prezzo"]

# Analisi
incasso_totale = df["Incasso"].sum()
incasso_medio_dest = df.groupby("Destinazione")["Incasso"].mean()
top3_dest = df["Destinazione"].value_counts().head(3)

print("Incasso totale:", incasso_totale)
print("Incasso medio per destinazione:\n", incasso_medio_dest)
print("Top 3 destinazioni:\n", top3_dest)
#------------------------------------------------------

incasso_per_destinazione = df.groupby("Destinazione")["Incasso"].sum()

plt.figure()
plt.bar(incasso_per_destinazione.index, incasso_per_destinazione.values)
plt.title("Incasso per Destinazione")
plt.xlabel("Destinazione")
plt.ylabel("Incasso (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

incasso_giornaliero = df.groupby("Giorno_Partenza")["Incasso"].sum()

plt.figure()
plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker="o")
plt.title("Andamento Giornaliero degli Incassi")
plt.xlabel("Giorno di Partenza")
plt.ylabel("Incasso (€)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure()
plt.pie(
    incasso_per_destinazione.values,
    labels=incasso_per_destinazione.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Percentuale di Vendite per Destinazione")
plt.tight_layout()
plt.show()
#------------------------------------------------------

categorie = {
    "Roma": "Europa",
    "Parigi": "Europa",
    "New York": "America",
    "Tokyo": "Asia",
    "Cairo": "Africa"
}

df["Categoria"] = df["Destinazione"].map(categorie)

incasso_categoria = df.groupby("Categoria")["Incasso"].sum()
durata_media_categoria = df.groupby("Categoria")["Durata"].mean()

print("Incasso per categoria:\n", incasso_categoria)
print("Durata media per categoria:\n", durata_media_categoria)

# Salvataggio CSV
df.to_csv("prenotazioni_analizzate.csv", index=False)
#------------------------------------------------------

def top_n_clienti(df, n):
    return df["Cliente"].value_counts().head(n)

print(top_n_clienti(df, 3))

fig, ax1 = plt.subplots()

# Grafico a barre (incasso medio)
ax1.bar(
    incasso_categoria.index,
    incasso_categoria.values
)
ax1.set_xlabel("Categoria")
ax1.set_ylabel("Incasso Medio (€)")
ax1.set_title("Incasso Medio e Durata Media per Categoria")

# Secondo asse y per la linea
ax2 = ax1.twinx()
ax2.plot(
    durata_media_categoria.index,
    durata_media_categoria.values,
    marker="o"
)
ax2.set_ylabel("Durata Media (giorni)")

plt.tight_layout()
plt.show()