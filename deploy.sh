#!/bin/bash

# Revaya AI - Cloud Run Deployment Script
# Deploys the intake system to Google Cloud Run

set -e

PROJECT_ID="revaya-ai-systems"
SERVICE_NAME="revaya-intake"
REGION="us-central1"
IMAGE_NAME="gcr.io/${PROJECT_ID}/${SERVICE_NAME}"

echo "🚀 Deploying Revaya Intake System to Cloud Run..."

# Check if required environment variables are set
if [ -z "$GOOGLE_API_KEY" ] || [ -z "$SENDGRID_API_KEY" ] || [ -z "$SLACK_WEBHOOK_URL" ]; then
    echo "❌ Error: Missing required environment variables"
    echo "Please set: GOOGLE_API_KEY, SENDGRID_API_KEY, SLACK_WEBHOOK_URL"
    exit 1
fi

# Set default email addresses if not provided
FROM_EMAIL=${FROM_EMAIL:-"system@revayaai.com"}
TO_EMAIL=${TO_EMAIL:-"shannon@revayaai.com"}

echo "📦 Building container image..."
gcloud builds submit --tag $IMAGE_NAME

echo "🌐 Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY="$GOOGLE_API_KEY",SENDGRID_API_KEY="$SENDGRID_API_KEY",SLACK_WEBHOOK_URL="$SLACK_WEBHOOK_URL",FROM_EMAIL="$FROM_EMAIL",TO_EMAIL="$TO_EMAIL"

echo "✅ Deployment complete!"
echo "🔗 Service URL:"
gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)'
