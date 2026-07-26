git add .
read -p "Message: " MESSAGE
echo
if [ -z "$MESSAGE" ]; then
    echo "provide message"
    exit 1
fi
git commit -m "$MESSAGE"
git push