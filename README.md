# Maintenance Prédictive des Moteurs Turbofan

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![Streamlit App](https://img.shields.io/badge/voir-app--web-green?logo=streamlit)](https://projet-maintenance-predictive.streamlit.app/)
> *"Si vous voulez trouver les secrets de l'univers, pensez en termes d'énergie, de fréquence, d'information et de vibration."* - Nikola Tesla

## À Propos de Ce Projet

J'ai toujours été fasciné par l'idée que les machines "parlent" avant de tomber en panne. Ce projet explore comment prédire les défaillances de moteurs turbofan en analysant leurs signaux vitaux - un peu comme un médecin qui écoute le cœur d'un patient.

L'inspiration vient du framework de Tesla sur les 4 dimensions fondamentales de l'énergie. J'ai appliqué cette vision à l'analyse de données industrielles, et les résultats sont plutôt encourageants !

## Démo en Ligne

Vous pouvez tester l'application Streamlit ici 👉 [Projet Maintenance Prédictive - Application Web](https://projet-maintenance-predictive.streamlit.app/)
## Ce que j'ai Obtenu

Les performances sont honnêtement meilleures que ce que j'espérais au début :

| Métrique | Résultat | Mon Interprétation |
|----------|----------|-------------------|
| **Précision (R²)** | ~90% | Le modèle comprend bien les patterns |
| **Erreur Moyenne** | 15 cycles | On peut anticiper les pannes 2 semaines avant |
| **Données** | 9,559 échantillons | 50 moteurs virtuels analysés |

## L'Approche "Tesla" que j'ai Testée

### Les 4 Dimensions que j'ai Analysées

| Dimension | Capteur | Importance | Pourquoi c'est Logique |
|-----------|---------|------------|----------------------|
| **ÉNERGIE** | Température | ~75% | Plus un moteur chauffe, plus il est en fin de vie |
| **FORCE** | Pression | ~18% | La pression baisse quand les composants s'usent |
| **VIBRATION** | Vibrations | ~4% | Les vibrations augmentent avec l'usure |
| **INFORMATION** | Efficacité | ~3% | Performance globale du système |

Ce qui m'a surpris, c'est que la température domine vraiment la prédiction. Tesla avait raison : l'énergie est au cœur de tout !

## Comment Utiliser Ce Code

### Installation
```bash
# Cloner le projet
git clone https://github.com/votre-nom/maintenance-predictive-tesla
cd maintenance-predictive-tesla

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'analyse complète
python main.py
```

### Structure des Fichiers
```
├── main.py                    # Le script principal (tout est dedans)
├── requirements.txt           # Les librairies nécessaires
├── data/
│   └── turbofan_data.csv     # Dataset généré automatiquement
├── models/
│   ├── random_forest_model.pkl    # Modèle entraîné
│   └── model_metrics.json         # Métriques sauvegardées
└── visualizations/
    ├── analysis_overview.png       # Vue d'ensemble des données
    └── prediction_analysis.png     # Résultats du modèle
```

## Ce que Ça Génère Automatiquement

Quand vous lancez `python main.py`, le script :

1. **Crée des données réalistes** de 50 moteurs avec leurs cycles de dégradation
2. **Analyse les patterns** et montre les corrélations
3. **Entraîne le modèle** Random Forest et évalue ses performances
4. **Génère 2 graphiques** pour visualiser les résultats

### Les Graphiques Produits

**analysis_overview.png** - Une vue 2x2 qui montre :
- Distribution des durées de vie des moteurs
- Comment la température évolue pour quelques moteurs
- La relation entre température et durée de vie restante
- Matrice de corrélations entre tous les capteurs

**prediction_analysis.png** - Validation du modèle :
- Prédictions vs réalité (idéalement alignées sur la diagonale)
- Distribution des erreurs de prédiction

## Résultats Techniques

### Performance du Modèle
```python
# Métriques typiques que j'obtiens
{
    'R²_training': 0.95,     # Très bon ajustement
    'R²_test': 0.90,        # Bonne généralisation
    'MAE_training': 8.5,    # Erreur d'entraînement
    'MAE_test': 15.2,       # Erreur de test
}
```

### Importance des Variables
La température représente environ 75% de l'importance, ce qui confirme l'hypothèse Tesla sur la dominance énergétique.

```python
# Distribution typique que j'observe
{
    'temperature': 0.76,    # Prédicteur principal
    'pressure': 0.18,      # Contribution significative  
    'vibration': 0.04,     # Signal complémentaire
    'efficiency': 0.02     # État global
}
```

## Comment j'ai Généré les Données

Plutôt que d'utiliser des données complètement aléatoires, j'ai modélisé la physique de la dégradation :

```python
def generate_sensor_data(degradation_level):
    # Plus le moteur est usé, plus il chauffe
    temperature = 500 + degradation_level * 200 + bruit
    
    # Les vibrations augmentent avec l'usure
    vibration = 0.5 + degradation_level * 1.5 + bruit
    
    # La pression baisse quand ça se dégrade
    pressure = 40 - degradation_level * 15 + bruit
    
    # L'efficacité diminue progressivement
    efficiency = 0.9 - degradation_level * 0.2 + bruit
```

J'ai aussi ajouté des contraintes physiques réalistes (température min 300°C, pression min 10 bar, etc.).

## Applications Concrètes

Ce type d'analyse pourrait être utilisé pour :

- **Aéronautique** : Prédire la maintenance des moteurs d'avion
- **Centrales électriques** : Optimiser la maintenance des turbines à gaz  
- **Industrie** : Surveillance de compresseurs et ventilateurs
- **Marine** : Maintenance prédictive des systèmes de propulsion

L'idée est d'éviter les pannes coûteuses (200k€ en moyenne) en planifiant la maintenance préventive (50k€).

## Limites et Améliorations Possibles

### Ce qui Pourrait Être Mieux

1. **Données synthétiques** : J'aimerais tester sur de vraies données (comme le dataset NASA C-MAPSS)
2. **Un seul algorithme** : Random Forest fonctionne bien, mais XGBoost pourrait faire mieux
3. **Pas de séries temporelles** : Les LSTM pourraient capturer des patterns temporels plus complexes

### Prochaines Étapes

Si j'avais plus de temps, j'aimerais :
- Comparer avec XGBoost et des réseaux de neurones
- Intégrer de vraies données industrielles
- Créer une petite interface web pour tester le modèle
- Ajouter plus de features (historique, conditions environnementales)

## L'Inspiration Tesla

Ce qui m'a marqué dans l'approche de Tesla, c'est l'idée que tout dans l'univers peut être analysé selon 4 dimensions énergétiques. En appliquant ce framework aux machines industrielles, on retrouve effectivement ces patterns.

La température (énergie) domine vraiment les prédictions, exactement comme Tesla l'aurait prédit. C'est fascinant de voir comment des principes physiques fondamentaux se retrouvent dans les algorithmes de machine learning !

## Reproductibilité

Le code est entièrement reproductible. Le seed est fixé pour les nombres aléatoires, donc vous devriez obtenir des résultats très similaires à chaque exécution.

```bash
# Pour reproduire exactement mes résultats
python main.py
```

Tous les fichiers sont générés automatiquement, pas besoin de préparation manuelle.

## Environnement Technique

```python
# Ce dont vous avez besoin
dependencies = {
    'python': '3.9+',
    'pandas': '1.5.0+',
    'numpy': '1.24.0+', 
    'scikit-learn': '1.2.0+',
    'matplotlib': '3.6.0+',
    'seaborn': '0.12.0+',
    'joblib': '1.2.0+'
}
```

## Contact

N'hésitez pas à me contacter si vous avez des questions ou des suggestions d'amélioration !

📧 **Email** : [habachrida1@gmail.com](mailto:habachrida1@gmail.com)  
💼 **LinkedIn** : [Rida Habach](https://www.linkedin.com/in/rida-habach-352769171/)

Je suis actuellement **à la recherche d'opportunités** en tant qu'**Ingénieur Data Science** ou **ML Engineer**. Ce projet fait partie de mon portfolio pour démontrer mes compétences en machine learning appliqué à des problématiques industrielles concrètes.

Je suis passionné par l'application de la physique et des mathématiques aux données, et j'aimerais contribuer à des projets qui ont un impact réel sur l'optimisation industrielle et la maintenance prédictive.

💡 Toujours ouvert aux discussions sur le machine learning, l'analyse de données, et les défis techniques interessants !

## Remerciements

- **Nikola Tesla** pour l'inspiration conceptuelle
- **La communauté open source** pour tous les outils utilisés
- **NASA** pour les datasets de référence qui m'ont inspiré la modélisation

---

*"La maintenance prédictive n'est finalement qu'une façon d'écouter ce que les machines essaient de nous dire."*

## License

MIT License - vous pouvez utiliser ce code librement, modifier, redistribuer. Juste gardez la mention d'origine !
