# ml_model.py
from typing import List, Optional

N_LAGS = 4  # how many recent points to use for the model

def predict_next_power(
    recent_power_values: List[float],
    current_time_iso: str,
    avg_temp_c: Optional[float],
    mode: Optional[str],
) -> float:
    """
    Stub model: for now just returns the last power value, or 0.0 if none.
    Person 3 will replace this logic with the real ML model.
    """
    if recent_power_values:
        return float(recent_power_values[-1])
    return 0.0
