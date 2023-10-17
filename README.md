# Deep Learning実践開発講座（DL4US）公開用リポジトリ
- [概要](#概要)
- [全体像](#全体像)
- [演習の進め方](#演習の進め方)
- [オンライン公開講座との違い](#オンライン公開講座との違い)
- [パッケージのインストール](#パッケージのインストール)
- [Google Colaboratoryでの実行上の諸注意](#google-colaboratory実行上の諸注意)
- [利用規約](#利用規約)
- [リンク](#リンク)

## 概要
本講座は主にエンジニアの方に向けた深層学習の入門教材です。
本教材では、Deep LearningのフレームワークTensorflowの高レベルAPIであるKerasを用いています。

ご利用に際しては、[利用規約](#利用規約)ご確認の上、遵守していただきますようお願いいたします。

## 全体像
本講座は全7Lessonの演習マテリアルからなっています。各Lessonは次のような構成になっています。

- Lesson 0: 機械学習・Deep Learningのキソ
  - 機械学習概観
- Lesson 1: 手書き文字認識をしよう
  - Keras入門、MNIST、MLP、前処理、勾配に関するテクニック、過学習に関する手法、Fashion MNIST
- Lesson 2: 畳み込みニューラルネットワーク
  - CNN基礎、Data Augmentation、画像データの正規化、Batch Normalization、Skip Connection
- Lesson 3: 系列データで予測させてみよう
  - RNN、BPTT、Gradient Clipping、LSTM、GRU
- Lesson 4: ニューラル翻訳モデルをつくってみよう
  - 言語モデル、分散表現、Seq2Seq、Keras Functional API、Attention
- Lesson 5: 画像からキャプションを生成してみよう
  - MSCOCO、学習済みモデルの利用、キャプション生成、Attention
- Lesson 6: ニューラルネットに画像を生成させよう
  - 生成モデル入門、GAN、Conditional GAN、VAE
- Lesson 7: ニューラルネットでゲームを攻略するAIをつくろう
  - 強化学習入門、Q学習、DQN、OpenAI Gym、Double DQN、Dueling Network
  
## 演習の進め方
各LessonにはそのLessonで学ぶトピックの説明及びPythonでの実装がJupyter Notebook形式でまとめられています。 各Lessonは4つのSectionから構成されており、

- Section 1: そのLessonで学ぶトピックの概要
- Section 2: Section 1の実装
- Section 3: 精度を向上させるための発展的テクニック
- Section 4: Section 3の実装

という構成になっています。Section 1、3の最後にはそのSectionで学んだことの確認問題があるので解いてみてください。正解はその次のSection 2、4の頭に書いてあります。またLesson 0のみ実装部分はありません。各Lessonはそれ以前のLessonの知識を前提としているので、Lesson 0から順にすすめてください。

## オンライン公開講座との違い
今回、オンライン公開講座DL4USの教材公開にあたり、次の点を変更しています。
* オンライン講座では、コードがすべて書かれているnotebookの他に、学習効果を高めるため、同一の内容でコードがすべて空白のnotebookも用意していましたが、本公開教材では前者のみを公開しています。ですので、各Lessonのnotebookは、上から順に実行していくことで一通りの処理の流れを確認できます。
* 各Lessonの最後の宿題を削除しました。
* オンライン講座では実行環境としてiLectを提供していましたが、今回は教材公開のみです（以下のインストール方法を参考に、各自で準備してください）。

## パッケージのインストール
オンライン講座での環境と同じパッケージをインストールする場合は、以下のコマンドを実行してください。

```$ pip install -r requirements.txt```

ただし、こちらのインストール方法は必ずしもお使いの環境での動作をサポートするものではないので、注意してください。

また、本教材はGoogle Colaboratoryでも実行することができます。ただし、各LessonでColabにないパッケージを利用することがあるので、その場合は最初に該当パッケージをインストールしてください。その他、[Google Colaboratoryでの実行上の諸注意](#google-colaboratory実行上の諸注意) もご覧ください。

## Google Colaboratory実行上の諸注意

### ダウンロードしたファイルの利用

演習ではご自身でダウンロードしたファイルをnotebookから参照する箇所があります。ここでは、Google Colaboratoryのnotebook上からGoogle Driveのファイルを参照する方法を説明します。

例えば、Lesson3のsection2では以下のようにファイルを参照する箇所がありますが、このままではGoogle Driveにファイルをアップロードしてもアクセスはできません。
(`No Such File or Directory`のエラーになります。)

```python
dataset, meta = arff.loadarff('ECG5000.arff')
```

そこで、以下の手順でGoogle Driveをマウントし、作業領域に対象ファイルをダウンロードします。
以下をnotebook上で実行して下さい。

まず、以下を実行してGoogle Driveをマウントします。

```python
from google.colab import drive
drive.mount('/content/gdrive')
```

実行するとURLとフォームが出力されるので、URLを踏んでログインし、認証コードを取得して下さい。それをnotebook上のフォームに入力します。

次にダウンロードコマンドを使えるようにします。
以下を実行して下さい。

```pythhon
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# check authority
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
```

これも先程と同様にURLとフォームが出力されるので、認証コードを取得し、フォームに入力して下さい。

あとは以下を実行することで作業領域にファイルをダウンロードできます。

```python
# hogeはファイルのid
downloaded = drive.CreateFile({'id':hoge})

# Download the file to a local disk
downloaded.GetContentFile('ECG5000.arff')
```

ここまでできれば、以下の読み込みを行うことができるようになります。

```python
dataset, meta = arff.loadarff('ECG5000.arff')
```

### 学習時間について

Google Colaboratoryでは一定時間経過するとインスタンスがリセットされます。具体的にはnotebookのセッションが切れてから90分経過または新しいインスタンスを起動してから12時間経過でインスタンスがリセットされるようです。参考: [Google Colaboratoryの90分セッション切れ対策【自動接続】](https://qiita.com/enmaru/items/2770df602dd7778d4ce6)

講座ではiLect環境を前提にしており、Lessonによっては長時間の学習が必要になるものもあります。Google Colaboratoryでの学習には制限があることは予めご了承ください。ただし、学習回数を小さくして試すなど工夫することで学習を進めることは可能です。

### Google Driveの容量

学習を行うときに使用するデータはご自身のGoogle Driveにアップロードすることになりますが、使用するデータには大きな容量を必要するものもあります。アップロードの前にGoogle Driveの容量を確認して問題ないか確認してください。例えば、Lesson5のSection1では13GBのzipファイルを扱うので注意が必要です。

## 利用規約
- 本コンテンツは**個人で学習**する目的のみで利用可能です。
- **講習会・教室**での利用や**企業内での講習**など、**商用**での利用は**認められていません**。
- 本コンテンツには、クリエイティブコモンズのライセンス「[CC-BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.ja)（表示 - 改変 - 非営利 一般）」が適用されます。
- 本コンテンツに関する一切については、東京大学（[松尾研究室](https://weblab.t.u-tokyo.ac.jp/contact/)）までお問い合わせください。本コンテンツを用いた講義・講習会を実施されたい場合は、個別に許諾を得ていただく必要があります。
- 本コンテンツの**更新は2019年で停止**しております。最新の見解とは異なる文面がある可能性や、Python・ライブラリの更新に伴いそのままでは実行ができない可能性がございます。予めご了承ください。
- 著作権は東京大学に帰属します。
- [免責事項](https://weblab.t.u-tokyo.ac.jp/dl4us%E5%85%8D%E8%B2%AC/)を確認してください。

## リンク
コンテンツ公開ページ：https://weblab.t.u-tokyo.ac.jp/dl4us/
