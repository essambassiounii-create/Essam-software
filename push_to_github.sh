#!/bin/bash
TOKEN="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"
REPO="https://essambassiounii-create:${TOKEN}@github.com/essambassiounii-create/Essam-software.git"

git add -A
git commit -m "NexaCode website - full project upload"
git push "$REPO" HEAD:main --force
echo "✅ Done! Check your GitHub repo."
