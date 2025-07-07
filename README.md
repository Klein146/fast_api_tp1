## TP  1 : Première API FastAPI

**Objectif** : Créer une API FastAPI simple pour gérer une liste de tâches (TODO).

**Fonctionnalités requises** :

- Créer une nouvelle tâche
- Lister toutes les tâches
- Récupérer une tâche par ID
- Marquer une tâche comme terminée
- Supprimer une tâche
- Filtrer les tâches par statut

**Structure de données** :

```python
{
    "id": 1,
    "title": "Apprendre FastAPI",
    "description": "Suivre le cours complet sur FastAPI",
    "completed": false,
    "created_at": "2025-07-03T10:30:00",
    "due_date": "2025-07-10T18:00:00"
}
```

**Instructions** :

1. Créez un nouveau projet FastAPI
2. Définissez les modèles Pydantic appropriés
3. Implémentez tous les endpoints requis
4. Ajoutez la validation des données
5. Gérez les erreurs appropriées
6. Testez votre API avec la documentation automatique

**Code de démarrage** :

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="TODO API", version="1.0.0")

# Stockage en mémoire (remplacer par une base de données en production)
todos = []
next_id = 1

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime
    due_date: Optional[datetime] = None

# Implémentez vos endpoints ici
```

**Critères d'évaluation** :

- Fonctionnalité complète de tous les endpoints
- Validation appropriée des données
- Gestion d'erreurs cohérente
- Documentation automatique claire
- Code propre et bien structuré