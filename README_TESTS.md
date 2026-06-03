# Tests

Instructions pour exécuter la suite de tests unitaires pour ce projet.

Pré-requis:
- Python 3.8+
- pip

Exécuter les commandes:

```powershell
pip install -r requirements.txt
python -m unittest discover -v
```

Ou utiliser le script PowerShell fourni:

```powershell
./run_tests.ps1
```

Notes:
- Les tests utilisent des mocks pour certains services externes (`xmlrpc`, `fitz`).
- Si vous rencontrez des erreurs liées à des paquets manquants, installez-les via `pip`.
