# Contributing

Merci pour votre intérêt à contribuer à ce projet. Pour lancer les tests localement:

```powershell
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m unittest discover -v
```

Ou utilisez `pytest` après avoir installé les dépendances de développement:

```powershell
pip install -r requirements-dev.txt
pytest
```

Avant de soumettre une PR, assurez-vous que tous les tests passent.
