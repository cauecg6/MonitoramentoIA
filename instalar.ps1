Write-Host "🔧 Ativando ambiente virtual..." -ForegroundColor Cyan
& "$PSScriptRoot\.venv\Scripts\Activate.ps1"

Write-Host "📦 Instalando pacotes (ultralytics, opencv-python, pandas)..." -ForegroundColor Cyan
python -m pip install --upgrade pip
python -m pip install ultralytics opencv-python pandas

Write-Host "`n✅ Tudo pronto! Agora você pode rodar o detector com: python detector_yolo_camera.py" -ForegroundColor Green
