import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

class Twitter:
    def __init__(self):
        CK = config.CONSUMER_KEY
        CS = config.CONSUMER_SECRET
        AT = config.ACCESS_TOKEN
        ATS = config.ACCESS_TOKEN_SECRET
        self.twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

    def user_timeline(self, tweet_num=5):
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント
        params ={'count' : tweet_num} #取得数
        res = self.twitter.get(url, params = params)
        if res.status_code == 200: #正常通信出来た場合
            timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
            for line in timelines: #タイムラインリストをループ処理
                print(line['user']['name']+'::'+line['text'])
                print(line['created_at'])
                print('*******************************************')
        else: #正常通信出来なかった場合
            print("Failed: %d" % res.status_code)
        return timelines

    def post_tweet(self):
        url = "https://api.twitter.com/1.1/statuses/update.json" #ツイートポストエンドポイント
        print("内容を入力してください。")
        tweet = input('>> ') #キーボード入力の取得
        print('*******************************************')
        params = {"status" : tweet}
        res = self.twitter.post(url, params = params) #post送信
        if res.status_code == 200: #正常投稿出来た場合
            print("Success.")
        else: #正常投稿出来なかった場合
            print("Failed. : %d"% res.status_code)

    def search_tweet(self, tweet_num=5):
        print("検索する文字列を入力してください。")
        search = input('>> ') #キーボード入力の取得
        print('*******************************************')
        url = "https://api.twitter.com/1.1/search/tweets.json?q={}".format(search) #ツイートポストエンドポイント
        params = {}
        res = self.twitter.get(url) #post送信
        if res.status_code == 200: #正常投稿出来た場合
            timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
            for line in timelines['statuses']: #タイムラインリストをループ処理
                print(line['user']['name']+'::'+line['text'])
                print(line['created_at'])
                print('*******************************************')
        else: #正常通信出来なかった場合
            print("Failed: %d" % res.status_code)
        return timelines
