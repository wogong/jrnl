text=$*
TOKEN=""
#URL="http://localhost:8383/$TOKEN/append_jrnl"
URL="http://la.wogong.net:8383/$TOKEN/append_jrnl"

curl -H "Accept: application/json" -H "Content-type: application/json" -s -X POST $URL -d '{"text":"'"$text"'"}'
