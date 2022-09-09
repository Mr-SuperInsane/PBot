# 概要
notify.pyまたはbot.pyの実行にはline-bot-sdkをインストールする必要があります。  

    $ pip install line-bot-sdk

## LINE Notify バージョン
「notify.py」は自身で発行したLINE Notifyのトークンをコピペして自分専用Botとしてお使いください。ソースコードはHeroku用に作られているので「Herokuの説明」を参考にデプロイしてください。

## LINE Messaging API (Bot) バージョン
「bot.py」はLINE Messaging APIのチャンネルアクセストークンおよびユーザーIDをコピペしてお使いください。  ソースコードは自由に変更していただいて構いません。またソースコードを利用して作成したLINE Botの配布も自由にしていただいて構いません。ソースコードはHeroku用に作られているので「Herokuの説明」を参考にデプロイしてください。

## Herokuの説明

P-Botの稼働にはHerokuの利用を推奨します。  

使い方はこちら
https://github.com/Naokun-Pavilion/Development_Memo/blob/main/Heroku.md
