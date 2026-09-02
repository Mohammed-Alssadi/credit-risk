from fastapi import FastAPI, HTTPException
from src.credit_risk_predictor import CreditRiskPredictor
from src.anomaly_detector import AnomalyDetector

app = FastAPI(
    title="منظومة تقييم المخاطر الائتمانية وكشف الشذوذ",
    description="واجهات برمجية كلاسيكية ومستقلة لتقييم الائتمان وكشف الشذوذ",
    version="3.1.0"
)


# تحميل النموذجين بشكل مستقل في الذاكرة
credit_risk_model = CreditRiskPredictor()
anomaly_detector_model = AnomalyDetector()


@app.get("/")



@app.post("/api/credit-risk/predict")
def predict_credit_risk(data: dict):

    try:
        result = credit_risk_model.predict(data)
        return result
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"حدث خطأ أثناء تقييم مخاطر الائتمان: {str(error)}")


@app.post("/api/anomaly/detect")
def detect_anomaly(data: dict):

    try:
        result = anomaly_detector_model.detect(data)
        return result
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"حدث خطأ أثناء كشف الشذوذ: {str(error)}")
