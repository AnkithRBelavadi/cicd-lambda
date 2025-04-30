#!/bin/bash
echo "Fetching secrets from AWS SSM..."

VAR_A=$(aws ssm get-parameter --name "$PARAM_VAR_A" --with-decryption --query "Parameter.Value" --output text)
VAR_B=$(aws ssm get-parameter --name "$PARAM_VAR_B" --with-decryption --query "Parameter.Value" --output text)

echo "Creating .env file..."
cat > .env <<EOF
VAR_A=$VAR_A
VAR_B=$VAR_B
EOF

echo ".env created!"
