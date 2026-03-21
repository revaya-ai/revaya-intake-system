#!/bin/bash

# Revaya AI - Secure Cloud Run Deployment Script
# Uses Google Cloud Secret Manager for credentials

set -e

PROJECT_ID="nth-bucksaw-484111-m5"
SERVICE_NAME="revaya-intake"
REGION="us-central1"
IMAGE_NAME="us-central1-docker.pkg.dev/${PROJECT_ID}/cloud-run-source-deploy/${SERVICE_NAME}"

echo "🔐 Deploying Revaya Intake System with Secret Manager..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found"
    echo "Please create .env from .env.example and add your credentials"
    exit 1
fi

# Load environment variables from .env (skip comments and blank lines)
export $(grep -v '^\s*#' .env | grep -v '^\s*$' | xargs)

# Create secrets if they don't exist
echo "📝 Creating/updating secrets in Secret Manager..."

echo -n "$GOOGLE_API_KEY" | gcloud secrets create google-api-key --data-file=- --replication-policy=automatic 2>/dev/null || \
echo -n "$GOOGLE_API_KEY" | gcloud secrets versions add google-api-key --data-file=-

echo -n "$RESEND_API_KEY" | gcloud secrets create resend-api-key --data-file=- --replication-policy=automatic 2>/dev/null || \
echo -n "$RESEND_API_KEY" | gcloud secrets versions add resend-api-key --data-file=-

echo -n "$SLACK_WEBHOOK_URL" | gcloud secrets create slack-webhook-url --data-file=- --replication-policy=automatic 2>/dev/null || \
echo -n "$SLACK_WEBHOOK_URL" | gcloud secrets versions add slack-webhook-url --data-file=-

# Set default email addresses
FROM_EMAIL=${FROM_EMAIL:-"system@revayaai.com"}
TO_EMAIL=${TO_EMAIL:-"shannon@revayaai.com"}

echo "📦 Building container image..."
gcloud builds submit --tag $IMAGE_NAME

echo "🌐 Deploying to Cloud Run with secrets..."
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-secrets GOOGLE_API_KEY=google-api-key:latest,RESEND_API_KEY=resend-api-key:latest,SLACK_WEBHOOK_URL=slack-webhook-url:latest \
  --set-env-vars FROM_EMAIL="$FROM_EMAIL",TO_EMAIL="$TO_EMAIL"

echo "✅ Deployment complete!"
echo "🔗 Service URL:"
gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)'
