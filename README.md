# 📹 Sistema de Monitoramento com IA | YOLOv8 + DeepSort + OpenCV

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-✅-orange.svg)](https://github.com/ultralytics/ultralytics)
[![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)]()

Sistema inteligente de monitoramento que detecta e rastreia **pessoas, celulares e placas de veículos** em tempo real usando **YOLOv8** e **DeepSort**.  

---

## 🚀 Funcionalidades

✅ Detecção de objetos com YOLOv8 (`person`, `cell phone`, `car`)  
✅ Rastreio com DeepSort e IDs únicos  
✅ Geração automática de relatórios CSV com data/hora  
✅ Contagem em tempo real exibida no terminal  
✅ Compatível com câmeras IP (RTSP/ONVIF) e USB  
✅ Painel web (em desenvolvimento)  


---

## 📷 Pré-requisitos

- **Python 3.10+**
- **Git**
- Câmera compatível com RTSP/ONVIF (ex: Tapo C320WS, Hikvision, Dahua) ou webcam USB
- Dependências Python:
  - ultralytics
  - opencv-python
  - pandas
  - deep_sort_realtime
  - scikit-learn

---

## 💻 Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/projeto-monitoramento-ia.git
    cd projeto-monitoramento-ia
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv .venv
    ```

3. Ative o ambiente virtual:
    - Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - Linux/macOS:
        ```bash
        source .venv/bin/activate
        ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚦 Uso

Execute o sistema principal:

```bash
python detector_yolo_camera.py
