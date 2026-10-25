CREATE TABLE IF NOT EXISTS staging_raw_events (
    raw_id SERIAL PRIMARY KEY,
    user_id VARCHAR(50),
    email VARCHAR(255),
    engagement_score NUMERIC,
    last_login VARCHAR(50),
    region VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS dim_clean_users (
    user_id VARCHAR(50) PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    engagement_score NUMERIC CHECK (engagement_score >= 0 AND engagement_score <= 100),
    last_login_date DATE,
    region VARCHAR(10)
);
