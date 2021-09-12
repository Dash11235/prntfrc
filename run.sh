while true; do
    pkill firefox
    url=$(python3 prntfrc.py)
    firefox $url
done
