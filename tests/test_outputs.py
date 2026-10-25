from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_pipeline_outputs_are_present_and_consistent():
    clean_path = ROOT / "data" / "clean_events_warehouse.csv"
    metrics_path = ROOT / "dashboards" / "quality_metrics.json"
    assert clean_path.exists() and metrics_path.exists()
    clean = pd.read_csv(clean_path)
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    assert len(clean) == metrics["passed"]
    assert metrics["ingested"] >= metrics["passed"]
    assert clean["user_id"].notna().all()
    assert clean["engagement_score"].between(0, 100).all()
