#!/bin/bash
# ضع التوكن الخاص بك هنا
TOKEN="YOUR_GITHUB_TOKEN_HERE"
git add -A
git commit -m "Nova Soft update"
git push https://essambassiounii-create:${TOKEN}@github.com/essambassiounii-create/Essam-software.git HEAD:main --force
