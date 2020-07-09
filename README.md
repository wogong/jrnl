# jrnl

A journal system including:
1. Add journal from terminal, using `jrnl.sh anything_you_want_journal`.
2. Add journal using Alfred Workflow.
3. Add journal by messaging to Telegram bot.
4. Gather the journal added in different ways to Day One. 
 

## note
1. You need a server to run API server using `jrnl_api_server.py`, so you can gather the journal from terminal and Alfred.
2. You need to register a telegram bot and update bot token in `jrnl_telegram_bot.py`, so you can gather the journal from messaging to Telegram bot,
3. You need set up a cron job to run `jrnl2dayone.py`, so a item contain all the journal you added will be
   created in Ddy One at the end of the day.