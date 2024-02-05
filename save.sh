#!/usr/bin/bash
git add .
# echo введите комментарий:
echo
read -p "введите комментарий:   "
echo
git commit -m "$REPLY"
git push
