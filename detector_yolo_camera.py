import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
from datetime import datetime
import pandas as pd

# Inicializar YOLOv8 e DeepSort
model = YOLO('yolov8n.pt')
tracker = DeepSort(max_age=30)

cap = cv2.VideoCapture(0)
logs = []
ids_pessoas = set()
ids_celulares = set()

print("🔴 Pressione ESC para encerrar.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Rodar YOLO
    results = model(frame)[0]
    detections = []

    for box in results.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls]
        if label in ["person", "cell phone"] and conf > 0.3:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append(([x1, y1, x2 - x1, y2 - y1], conf, label))

    # Rastrear objetos com DeepSort
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, w, h = track.to_ltrb()

        objeto_detectado = track.get_det_class()
        color = (0, 255, 0) if objeto_detectado == "person" else (255, 0, 0)

        # Desenhar
        cv2.rectangle(frame, (int(l), int(t)), (int(l + w), int(t + h)), color, 2)
        cv2.putText(frame, f"{objeto_detectado} {track_id}", (int(l), int(t) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Registrar se for novo
        if objeto_detectado == "person" and track_id not in ids_pessoas:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logs.append({
                'hora_inicio': timestamp,
                'objeto': 'person',
                'pessoa_id': track_id,
                'total_pessoas': len(ids_pessoas) + 1
            })
            ids_pessoas.add(track_id)

        elif objeto_detectado == "cell phone" and track_id not in ids_celulares:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logs.append({
                'hora_inicio': timestamp,
                'objeto': 'cell phone',
                'pessoa_id': track_id,
                'total_pessoas': len(ids_celulares) + 1
            })
            ids_celulares.add(track_id)

    # Mostrar no terminal os totais em tempo real
    print(f"👤 Pessoas detectadas: {len(ids_pessoas)} | 📱 Celulares detectados: {len(ids_celulares)}", end="\r")

    cv2.imshow("Monitoramento com Rastreio", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

# Linha final no relatório
logs.append({
    'hora_inicio': 'FIM',
    'objeto': 'TOTAL',
    'pessoa_id': '',
    'total_pessoas': len(ids_pessoas) + len(ids_celulares)
})

# Salvar CSV
df = pd.DataFrame(logs)
df.to_csv("relatorio_movimentos.csv", index=False)

print("\n✅ Relatório salvo em relatorio_movimentos.csv")
print(f"👤 Total de pessoas únicas: {len(ids_pessoas)}")
print(f"📱 Total de celulares únicos: {len(ids_celulares)}")
