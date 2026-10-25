"""ETL quality pipeline for the repository's synthetic event dataset."""
from pathlib import Path
import json, logging, re
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
LOG_DIR=ROOT/"logs"; LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(filename=LOG_DIR/"pipeline_audit.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
EMAIL_RE=re.compile(r"^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+[.][A-Za-z0-9-.]+$")
def run_pipeline():
    df=pd.read_csv(ROOT/"data/dirty_raw_events.csv"); initial=len(df)
    required={"event_id","user_id","email","engagement_score","last_login","region"}
    missing=required-set(df.columns)
    if missing: raise ValueError(f"Input dataset missing columns: {sorted(missing)}")
    score=pd.to_numeric(df["engagement_score"],errors="coerce")
    checks={"missing_user_id":int(df["user_id"].isna().sum()+df["user_id"].astype(str).str.strip().eq("").sum()),"invalid_email":int((~df["email"].fillna("").astype(str).str.match(EMAIL_RE)).sum()),"missing_engagement_score":int(score.isna().sum()),"out_of_range_score":int((~score.between(0,100)).sum()),"invalid_last_login":int(pd.to_datetime(df["last_login"],errors="coerce").isna().sum()),"missing_region":int(df["region"].isna().sum()+df["region"].astype(str).str.strip().eq("").sum()),"duplicate_rows":int(df.duplicated().sum())}
    clean=df.copy(); clean["engagement_score"]=score; clean["last_login"]=pd.to_datetime(clean["last_login"],errors="coerce")
    valid=clean["user_id"].notna() & clean["user_id"].astype(str).str.strip().ne("") & clean["email"].fillna("").astype(str).str.match(EMAIL_RE) & clean["engagement_score"].between(0,100) & clean["last_login"].notna()
    clean=clean.loc[valid].drop_duplicates().copy()
    clean["region"]=clean["region"].fillna("").astype(str).str.strip().replace("", "Unknown")
    clean["last_login"]=clean["last_login"].dt.strftime("%Y-%m-%d")
    clean.to_csv(ROOT/"data/clean_events_warehouse.csv",index=False); clean.to_csv(ROOT/"dashboards/clean_events_warehouse.csv",index=False)
    metrics={"ingested":int(initial),"passed":int(len(clean)),"pass_rate_pct":round(len(clean)/initial*100,2) if initial else 0,**checks,"data_note":"Metrics computed from synthetic demonstration data."}
    (ROOT/"dashboards/quality_metrics.json").write_text(json.dumps(metrics,indent=2)+"\n",encoding="utf-8")
    labels={"missing_user_id":"Missing user ID","invalid_email":"Invalid email","missing_engagement_score":"Missing engagement score","out_of_range_score":"Out-of-range engagement score","invalid_last_login":"Invalid last-login date","missing_region":"Missing region","duplicate_rows":"Duplicate rows"}
    report=["# Data Quality Audit — Pipeline Run",""," > **Data note:** This audit is computed from synthetic demonstration data, not a production assessment.","",f"- Records ingested: {initial}",f"- Records passing core validation: {len(clean)}",f"- Pass rate: {metrics['pass_rate_pct']:.2f}%","","## Validation findings",""]
    report += [f"- {labels[k]}: {v}" for k,v in checks.items()]
    report += ["","## Cleaning policy","Rows missing a user ID, with invalid email, invalid/missing score, or invalid login date are excluded. Blank regions are retained as Unknown; exact duplicate rows are removed.",""]
    (ROOT/"reports/data_quality_audit.md").write_text("\n".join(report),encoding="utf-8")
    logging.info("ETL complete: ingested=%s passed=%s pass_rate_pct=%.2f",initial,len(clean),metrics["pass_rate_pct"])
    print(f"ETL complete: {initial} ingested, {len(clean)} passed ({metrics['pass_rate_pct']:.2f}%).")
    return metrics
if __name__=="__main__": run_pipeline()
