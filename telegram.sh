#!/bin/sh
#
#  This script sends whatever is piped to it as a message to the specified Telegram bot
#
message=$( cat )
# apiToken='5446625068:AAF3WJf9WbqKm71Gtx720FP2hSuPOvgll3s'
apiToken='5593884317:AAGY5-c4DZhNtUlOZyr09Wj75P2QiKBHoFI'
# example:
# apiToken=123456789:AbCdEfgijk1LmPQRSTu234v5Wx-yZA67BCD
# userChatId=5054064843
userChatId=1385755393
# example:
# userChatId=123456789

sendTelegram() {
        curl -s \
        -X POST \
        https://api.telegram.org/bot$apiToken/sendMessage \
        -d text="$message" \
        -d chat_id=$userChatId
}

if  [[ -z "$message" ]]; then
        echo "Please pipe a message to me!"
else
        sendTelegram
fi