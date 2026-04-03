"""Anomaly Detection Model using Isolation Forest.
Detects anomalous behavior in CPU, memory, latency, and error rate metrics."""
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pickle, os, logging

logger = logging.getLogger("kubesage.anomaly")

class AnomalyDetector:
    def __init__(self, contamination: float = 0.1):
        self.model = IsolationForest(contamination=contamination, random_state=42, n_estimators=100)
        self.scaler = StandardScaler()
        self.is_trained = False

    def train(self, data: np.ndarray):
        """Train on metrics array of shape (n_samples, 4): [cpu, memory, latency, error_rate]."""
        scaled = self.scaler.fit_transform(data)
        self.model.fit(scaled)
        self.is_trained = True
        logger.info(f"Anomaly detector trained on {len(data)} samples")

    def predict(self, sample: np.ndarray) -> dict:
        """Returns anomaly score and classification for a single sample [cpu, mem, lat, err]."""
        if not self.is_trained:
            return {"is_anomaly": False, "score": 0.0, "message": "Model not trained"}
        scaled = self.scaler.transform(sample.reshape(1, -1))
        score = self.model.score_samples(scaled)[0]
        prediction = self.model.predict(scaled)[0]
        is_anomaly = prediction == -1
        severity = "CRITICAL" if score < -0.5 else "HIGH" if score < -0.3 else "MEDIUM" if is_anomaly else "LOW"
        return {"is_anomaly": is_anomaly, "score": round(float(score), 4), "severity": severity,
                "message": f"Anomaly detected (score={score:.3f})" if is_anomaly else "Normal behavior"}

    def save(self, path: str = "models/anomaly_model.pkl"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f: pickle.dump({"model": self.model, "scaler": self.scaler}, f)

    def load(self, path: str = "models/anomaly_model.pkl"):
        with open(path, "rb") as f:
            data = pickle.load(f)
            self.model, self.scaler = data["model"], data["scaler"]
            self.is_trained = True

def generate_synthetic_data(n_normal: int = 1000, n_anomaly: int = 50) -> np.ndarray:
    """Generate synthetic training data with injected anomalies."""
    normal = np.column_stack([
        np.random.normal(45, 12, n_normal),   # CPU
        np.random.normal(55, 10, n_normal),   # Memory
        np.random.normal(120, 30, n_normal),  # Latency
        np.random.normal(0.5, 0.3, n_normal), # Error rate
    ])
    anomalies = np.column_stack([
        np.random.uniform(85, 100, n_anomaly),
        np.random.uniform(85, 100, n_anomaly),
        np.random.uniform(500, 2000, n_anomaly),
        np.random.uniform(5, 20, n_anomaly),
    ])
    return np.vstack([normal, anomalies])
