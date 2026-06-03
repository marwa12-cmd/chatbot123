# Run project tests (PowerShell)
Write-Host "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

Write-Host "Running unit tests..."
python -m unittest discover -v
