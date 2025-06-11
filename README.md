# Pricing de Produits Structurés

## 📖 Présentation du projet

Ce projet est une plateforme de **pricing de produits structurés financiers**, développée dans le cadre d’un projet universitaire à Dauphine (Avril 2025).

L'objectif est de fournir un moteur de valorisation robuste et modulaire en **Python**, intégré dans une **application web** via le framework **Django**. Cette plateforme permet de calculer le prix et les sensibilités (grecques) de produits financiers complexes à partir de modèles stochastiques.

---

## ⚙️ Architecture générale

Le projet repose sur une architecture claire en deux parties principales :

### 🖥️ Backend — Moteur de pricing Python
- **Langage** : Python
- **Rôle** : Implémente les modèles financiers et les moteurs de calcul
- **Fonctionnalités principales** :
  - Simulation de trajectoires via modèles stochastiques (Black-Scholes, Heston, etc.)
  - Pricing par méthode de Monte Carlo
  - Calcul des sensibilités (Delta, Gamma, Vega, Rho, Theta)
  - Gestion des produits callables
  - Résultats structurés et agrégés

### 🌐 Frontend — Interface web (Django)
- **Langage** : Python (Django) + HTML/CSS/JavaScript
- **Rôle** : Fournir une interface utilisateur ergonomique accessible via un navigateur web
- **Fonctionnalités principales** :
  - Formulaires interactifs pour configurer les paramètres de pricing
  - Envoi des requêtes à l’API backend
  - Affichage des résultats (prix, bornes de confiance, grecques)

---

## ▶️ Lancement rapide

### Prérequis
- Python 3.x
- pip
- Django (`pip install django`)

### Installation et démarrage

```bash
git clone https://github.com/votre-utilisateur/pricing-produits-structures.git
cd pricing-produits-structures
pip install -r requirements.txt
python manage.py runserver

