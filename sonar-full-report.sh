#!/bin/bash

# source .env

# Variables
SONAR_TOKEN="5zxxxxxxxxxxxxxxxx"
PROJECT_KEY="Manav-Khandurie_fastapi-learning"
SONAR_API="https://sonarcloud.io/api"
REPORT_DIR="sonar-report"

# Create report directory
mkdir -p "$REPORT_DIR"

# Fetch issues
curl -s -u "${SONAR_TOKEN}:" \
     "${SONAR_API}/issues/search?componentKeys=${PROJECT_KEY}&ps=500" \
     -o "${REPORT_DIR}/issues.json"

# Fetch quality gate status
curl -s -u "${SONAR_TOKEN}:" \
     "${SONAR_API}/qualitygates/project_status?projectKey=${PROJECT_KEY}" \
     -o "${REPORT_DIR}/quality_gate.json"

# Fetch key metrics
curl -s -u "${SONAR_TOKEN}:" \
     "${SONAR_API}/measures/component?component=${PROJECT_KEY}&metricKeys=coverage,line_coverage,duplicated_lines_density,ncloc,complexity" \
     -o "${REPORT_DIR}/measures.json"

# Merge all into a single report
jq -s '{
      timestamp: now,
      issues: .[0].issues,
      quality_gate: .[1].projectStatus,
      metrics: .[2].component.measures
    }' "${REPORT_DIR}/issues.json" "${REPORT_DIR}/quality_gate.json" "${REPORT_DIR}/measures.json" > "${REPORT_DIR}/full-sonar-report.json"
