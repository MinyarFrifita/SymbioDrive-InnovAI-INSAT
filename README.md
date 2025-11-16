# SymbioDrive-InnovAI-INSAT
Système d’Analyse et de Prédiction du Comportement de Conduite

**Version :** 1.0.0

## Table des matières


1. [Présentation du projet](#présentation-du-projet)
2. [Architecture & Stack technologique](#architecture--stack-technologique)
3. [État actuel (Phase 1)](#état-actuel-phase-1)
4. [Phase 2 : Application mobile & Intégration temps réel](#phase-2--application-mobile--intégration-temps-réel)
5. [Phase 3 : Analytique avancée & Améliorations IA](#phase-3--analytique-avancée--améliorations-ia)
6. [Roadmap](#roadmap)

---

## Présentation du projet

### Vision

Créer un système complet d’analyse et de prédiction du comportement de conduite permettant de surveiller, analyser et prédire les comportements de conduite en temps réel. Le système utilise l’apprentissage automatique pour identifier les comportements dangereux et fournir des recommandations personnalisées afin d’améliorer la sécurité routière.

### Objectifs clés

- Surveiller les événements de conduite en temps réel via les capteurs mobiles
- Classifier et prédire les styles de conduite (agressif, normal, sûr)
- Détecter les comportements dangereux avant qu'ils ne surviennent
- Fournir des feedbacks et recommandations personnalisées
- Permettre la gestion de flottes et la surveillance des conducteurs pour les entreprises
- Contribuer à la sécurité routière et à la prévention des accidents

### Utilisateurs cibles

- Conducteurs individuels souhaitant améliorer leurs habitudes
- Gestionnaires de flottes surveillant plusieurs conducteurs
- Compagnies d'assurance évaluant le risque des conducteurs

## Architecture & Stack technologique

### Architecture du système
```text
┌─────────────────────────────────────────────────────────┐
│                  Couche Client (Flutter)                │
│      Application mobile pour conducteurs & flottes      │
└────────────────────┬────────────────────────────────────┘
                     │
              (REST API / WebSocket)
                     │
┌────────────────────▼────────────────────────────────────┐
│                  Couche Backend (FastAPI)               │
│  ├─ Authentification & Autorisation                     │
│  ├─ Traitement de données en temps réel                 │
│  ├─ Servir les modèles ML & prédictions                 │
│  └─ Gestion et stockage des données                     │
└────────────────────┬────────────────────────────────────┘
                     │
       ┌─────────────┼────────────┐
       |             │            │
 ┌─────▼────┐  ┌─────▼────┐  ┌────▼─────┐
 │PostgreSQL│  │ Modèles  │  │  Cache   │
 │ Base de  │  │ ML (.pkl)│  │ (Redis)  │
 │ données  │  │          │  │          │
 └──────────┘  └──────────┘  └──────────┘

```
### Stack technologique

- Framework : FastAPI (Python)
- Base de données : PostgreSQL
- Authentification : JWT
- ML : scikit-learn, pickle
- Asynchrone : asyncio, Uvicorn
- Validation : Pydantic

#### Frontend (Phase 2)

- Framework : Flutter (Dart)
- Gestion d'état : Riverpod / Bloc
- Temps réel : WebSocket
- Capteurs : GPS, accéléromètre, gyroscope

#### ML & Traitement des données

- Formats modèles : scikit-learn (.pkl)
- Prétraitement et ingénierie des features : Pandas, NumPy
- Évaluation : métriques scikit-learn

#### DevOps & Déploiement

- Contrôle de version : Git/GitHub
- Déploiement : Docker, Vercel/AWS/GCP

#### Base de données

- Neon PostgreSQL
- Cache : Redis (Phase 2)

## État actuel (Phase 1)


### Infrastructure backend

- Application FastAPI avec structure complète
- Base PostgreSQL configurée avec SQLAlchemy
- Authentification JWT (inscription, login, refresh)
- Middleware CORS pour communication client
- Gestion des erreurs et logs


### Modèles de données

- Utilisateur (authentification, profil)
- Événement de conduite
- Style de conduite
- Gestion des relations entre entités

### Endpoints API

- Auth : inscription, login, refresh token
- Événements de conduite : création, lecture, liste paginée
- Prédiction : classification d'événements et de styles
- Tableau de bord utilisateur

### Intégration ML

- Chargement des modèles .pkl
- Extraction des features et prétraitement
- Prédiction via API

### Documentation

- Swagger UI
- Guide de structure et setup
- Schéma base de données

 *En cours :

+Application Flutter :

Design UI/UX

+Intégration capteurs

+Pipeline de collecte de données temps réel

+Connexion à l'API backend

4/ Phase 2 : Application mobile & Intégration temps réel

### En cours

- Application Flutter : Design UI/UX
- Intégration capteurs
- Pipeline de collecte de données temps réel
- Connexion à l'API backend

## Phase 2 : Application mobile & Intégration temps réel

### Objectifs

- Développer l'application Flutter complète
- Collecter les données en temps réel
- Intégrer avec le backend
- Mettre en place un système de récompense par points pour les conducteurs : chaque utilisateur accumule des points en fonction de son comportement de conduite responsable. Ces points peuvent être échangés contre des offres ou avantages partenaires.

### Fonctionnalités clés

- Collecte de données GPS, accéléromètre, gyroscope
- Streaming en temps réel via WebSocket
- Mode hors-ligne avec synchronisation
- Notifications de sécurité
- Visualisation des trajets sur carte
- Ajouter modèles ML plus avancés
- Système de points et récompenses : suivi des points, classement des conducteurs et attribution automatique d'offres en fonction du score accumulé

### Backend

- Endpoint WebSocket prêt
- Prédiction en temps réel
- Gestion des sessions et alertes (en cours)

### Nouveaux modèles

- Analyse des conditions de la route
- Surveillance de l'état du véhicule
- Évaluation de l'état météorologique

### Critères de réussite Phase 2

- Connexion API réussie
- Transmission et affichage temps réel
- Fiabilité 99%
- Tests API et validation utilisateur

## Phase 3 : Analytique avancée & Améliorations IA

### Objectifs

- Analytique prédictive
- Recommandations personnalisées
*Pipeline d'apprentissage continu :

+Collecte mensuelle de données

+Réentraînement automatique

+Versioning et suivi de performance

+Monitoring de dérive des modèles

### Pipeline d'apprentissage continu

- Collecte mensuelle de données
- Réentraînement automatique
- Versioning et suivi de performance
- Monitoring de dérive des modèles

*Dashboard analytique :

+Score de conduite en temps réel

+Statistiques historiques

+Prévisions et recommandations

+Fonctionnalités sociales (classements, badges)

### Dashboard analytique

- Score de conduite en temps réel
- Statistiques historiques
- Prévisions et recommandations
- Fonctionnalités sociales (classements, badges)

### Intégration

- Assurance
- Constructeurs véhicules connectés
- Gestion de flotte

### Améliorations prévues

- Ajout features dérivées (jerk, TTC)
- LSTM pour données haute fréquence
- Crowdsourcing & augmentation des données
- Personnalisation plus précise par utilisateur
- Contexte (route, météo, trafic)
- Explicabilité via SHAP / LIME

## Roadmap

- Q1 : App Flutter v1.0, prédiction temps réel
- Q2 : ML avancé, intégrations assurance
- Q3 : Pipeline apprentissage continu, multi-langues

- Q4 : Marketplace ML, API tierces, flotte entreprise

