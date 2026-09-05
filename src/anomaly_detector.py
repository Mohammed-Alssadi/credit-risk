import joblib
import pandas as pd


class AnomalyDetector:

    FEATURE_NAMES = [
        "invoice_amount",
        "discount_ratio",
        "paid_ratio",
        "due_ratio",
        "invoice_vs_customer_avg",
        "invoice_vs_customer_max",
        "customer_invoice_frequency",
        "days_since_last_invoice",
        "customer_discount_avg",
        "discount_vs_normal",
        "credit_utilization_ratio",
        "items_count",
        "average_item_price",
    ]

    def __init__(self, model_path: str = "models/anomaly_detector.joblib"):
        self.model = joblib.load(model_path)

    def detect(self, data: dict) -> dict:

        # Prepare input data as a DataFrame with model feature schema
        df = pd.DataFrame([data])[self.FEATURE_NAMES]

        # Anomaly prediction: 1 = Normal, -1 = Anomaly
        pred = int(self.model.predict(df)[0])
        score = float(self.model.decision_function(df)[0])

        is_anomaly = (pred == -1)

        return {
            "customer_id": data.get("customer_id", ""),
            "is_anomaly": is_anomaly,
            "score": round(score, 4),
            "label": "Suspicious Transaction" if is_anomaly else "Normal Transaction"
        }
