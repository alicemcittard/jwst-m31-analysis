from astroquery.mast import Observations
import pandas as pd

print ("Cercando dati JWST di M31 aka Andromeda...")

obs= Observations.query_object ("M31", radius="0.31 deg")
obs_df=obs.to_pandas()

jwst=obs_df[obs_df["obs_collection"]== "JWST"]

print(f"Trovate {len(jwst)} osservazioni JWST di M31")
print (jwst [["obs_id", "filters", "t_exptime"]].head(10))

print(f"\nTotale osservazioni JWST di M31: {len(jwst)}")
print(f"Strumenti usati: {jwst['instrument_name'].unique()}")

jwst.to_csv ("m31__jwst_observations.csv", index=False)
print ("Dati salvati in m31__jwst_observations.csv")


import matplotlib.pyplot as plt

# Grafico: distribuzione dei tempi di esposizione
plt.figure(figsize=(10, 6))
plt.hist(jwst['t_exptime'].dropna(), bins=20, color='steelblue', edgecolor='black')
plt.title('Distribuzione Tempi di Esposizione JWST - M31 (Andromeda)')
plt.xlabel('Tempo di Esposizione (secondi)')
plt.ylabel('Numero di Osservazioni')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('m31_esposizione.png')
plt.show()
print("Grafico salvato!")