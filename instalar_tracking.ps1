Write-Host "🔧 Ativando ambiente virtual..." -ForegroundColor Cyan
& "$PSScriptRoot\.venv\Scripts\Activate.ps1"

Write-Host "📦 Instalando pacotes necessários para YOLO + DeepSort..." -ForegroundColor Cyan
python -m pip install --upgrade pip
pip install ultralytics opencv-python pandas deep_sort_realtime

Write-Host "`n✅ Tudo pronto! Agora você pode rodar o detector com: python detector_yolo_camera.py" -ForegroundColor Green
