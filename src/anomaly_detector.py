import joblib
import pandas as pd


class AnomalyDetector:

    FEATURE_NAMES = [

    ]

    def __init__(self, model_path: str = "models/anomaly_detector.joblib"):
        self.model = joblib.load(model_path)

    def detect(self, data: dict) -> dict:

        # تجهيز البيانات كـ DataFrame للنموذج
        df = pd.DataFrame([data])[self.FEATURE_NAMES]

        # التنبؤ بالشذوذ: 1 = طبيعي، -1 = شاذ
        pred = int(self.model.predict(df)[0])
        score = float(self.model.decision_function(df)[0])

        is_anomaly = (pred == -1)

        return {
            "customer_id": data.get("customer_id",""),
            "is_anomaly": is_anomaly,
            "score": round(score, 4),
            "label": "سلوك مالي مريب" if is_anomaly else "سلوك طبيعي"
        }
