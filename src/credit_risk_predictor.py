import joblib
import pandas as pd


class CreditRiskPredictor:

    FEATURE_NAMES = [
    
    ]

    def __init__(self, model_path: str = "models/credit_risk_model.joblib"):
        self.model = joblib.load(model_path)

    def predict(self, data: dict) -> dict:

        # تجهيز البيانات كـ DataFrame للنموذج
        df = pd.DataFrame([data])[self.FEATURE_NAMES]

        # التنبؤ باحتمالية التعثر
        prob = float(self.model.predict_proba(df)[0][1])
        score = round(prob * 100, 2)

        # تحديد مستوى الخطر والإجراء الموصى به
        if prob >= 0.15:
            risk_level = "HIGH"
            action = "BLOCK_CREDIT"
            message = "عميل عالي الخطورة، يُمنع البيع الآجل ويُلزم بالدفع نقداً."
        elif prob >= 0.10:
            risk_level = "MEDIUM"
            action = "WARNING"
            message = "العميل لديه مؤشرات تأخير، يُرجى توخي الحذر قبل منح الآجل."
        else:
            risk_level = "LOW"
            action = "APPROVE"
            message = "عميل ممتاز وسجله آمن، مسموح بالبيع الآجل."

        return {
            "customer_id": data.get("customer_id", ""),
            "score": score,
            "risk_level": risk_level,
            "action": action,
            "message": message
        }
