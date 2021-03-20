# LINE オウム返しボット

[LINE Messaging API](https://developers.line.biz/ja/docs/messaging-api/overview/)でのオウム返しを実演する小さなウェブアプリケーションです。

## デプロイ方法

### Herokuボタンを使ってターミナルを使わずにアプリをデプロイする

以下の手順に従うと、HerokuボタンとPython(Flask)を使ってオウム返しボットを簡単にデプロイできます。

#### 必要なもの

| 項目 | 説明 |
| ---- | ----------- |
| LINE Messaging API チャネル | LINE Messaging API が提供する機能をアプリで利用するための通信路。 チャネルは、[LINE Developers コンソール](https://developers.line.biz/console/register/messaging-api/channel/)で作成できます。 |
| Heroku アカウント | [Heroku](https://www.heroku.com)は、Webアプリをデプロイできるクラウドサービスです。|

#### 「Deploy to Heroku」ボタンを使ってアプリをデプロイする

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Alma-field/line-parrot)

1. 上記の**Deploy to Heroku** ボタンをクリックします。
2. Herokuの「Create New App」ページで、必要事項を入力します。
3. **Deploy app**をクリックします。
4. **View**をクリックしてアプリのデプロイが成功したことを確認します。「You have not assigned any value for LINE_BOT_CHANNEL_TOKEN and LINE_BOT_CHANNEL_SECRET」のメッセージが画面に表示されていたらデプロイができています。
5. HerokuアプリのURL（`https://{Herokuアプリ名}.herokuapp.com`）をメモしておいてください。 Messaging APIにコールバックを追加する際に必要になります。
6. 「[Messaging APIを始めよう - 4. チャネルを作成する](https://developers.line.biz/ja/docs/messaging-api/getting-started/#_4-%E3%83%81%E3%83%A3%E3%83%8D%E3%83%AB%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B)」の手順に従ってLIFFアプリをチャネルに追加してください。
7. チャネルのステータスが「非公開」の場合、「非公開」ボタンをクリックしチャネルを公開します。
8. 「[Echoサンプルボットをデプロイする](https://developers.line.biz/ja/docs/messaging-api/building-sample-bot-with-heroku/#echo%E3%82%B5%E3%83%B3%E3%83%95%E3%82%9A%E3%83%AB%E3%83%9B%E3%82%99%E3%83%83%E3%83%88%E3%82%92%E3%83%86%E3%82%99%E3%83%95%E3%82%9A%E3%83%AD%E3%82%A4%E3%81%99%E3%82%8B)」の手順(2番以外)に従ってMessaging APIの設定を行ってください。
9. エンドポイントURL（`https://{Herokuアプリ名}.herokuapp.com`）にWebブラウザーからアクセスし、アプリが正しく動作していることを確かめてください。<br>正しく動作していれば、**OK**と表示されます。


[heroku-cli]: https://devcenter.heroku.com/articles/heroku-cli
[liff-api-ref]: https://developers.line.biz/ja/reference/liff/
[calling-liff-api]: https://developers.line.biz/ja/docs/liff/developing-liff-apps#calling-liff-api
