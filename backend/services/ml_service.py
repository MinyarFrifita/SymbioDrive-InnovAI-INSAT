import joblib
import numpy as np
from config import settings
import os

class MLService:
    def __init__(self):
        """Initialize ML service and load pre-trained models."""
        self.models_path = settings.ML_MODELS_PATH
        self.driving_event_model = None
        self.driving_style_model = None
        self._load_models()
    
    def _load_models(self):
        """Load pickled ML models from disk."""
        try:
            event_model_path = os.path.join(self.models_path, "driving_event_model.pkl")
            style_model_path = os.path.join(self.models_path, "driving_style_model.pkl")
            
            if os.path.exists(event_model_path):
                self.driving_event_model = joblib.load(event_model_path)
                print(f"Loaded driving event model from {event_model_path}")
            
            if os.path.exists(style_model_path):
                self.driving_style_model = joblib.load(style_model_path)
                print(f"Loaded driving style model from {style_model_path}")
        except Exception as e:
            print(f"Error loading ML models: {e}")
    
    def predict_driving_event(self, features: list[float]) -> dict:
        """
        Predict driving event type and severity.
        Args:
            features: List of numerical features from driving telemetry
        Returns:
            Dictionary with prediction and confidence
        """
        if self.driving_event_model is None:
            return {"error": "Model not loaded"}
        
        try:
            features_array = np.array([features])
            prediction = self.driving_event_model.predict(features_array)[0]
            
            # Try to get probability if available
            confidence = 0.0
            if hasattr(self.driving_event_model, 'predict_proba'):
                proba = self.driving_event_model.predict_proba(features_array)[0]
                confidence = float(np.max(proba))
            
            return {
                "prediction": str(prediction),
                "confidence": confidence,
                "model_type": "driving_event"
            }
        except Exception as e:
            return {"error": f"Prediction failed: {str(e)}"}
    
    def predict_driving_style(self, features: list[float]) -> dict:
        """
        Predict driving style category.
        Args:
            features: List of numerical features (aggregated metrics)
        Returns:
            Dictionary with style prediction and confidence
        """
        if self.driving_style_model is None:
            return {"error": "Model not loaded"}
        
        try:
            features_array = np.array([features])
            prediction = self.driving_style_model.predict(features_array)[0]
            
            # Try to get probability if available
            confidence = 0.0
            if hasattr(self.driving_style_model, 'predict_proba'):
                proba = self.driving_style_model.predict_proba(features_array)[0]
                confidence = float(np.max(proba))
            
            return {
                "prediction": str(prediction),
                "confidence": confidence,
                "model_type": "driving_style"
            }
        except Exception as e:
            return {"error": f"Prediction failed: {str(e)}"}

# Singleton instance
ml_service = MLService()
