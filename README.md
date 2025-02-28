# ml_tictactoe
三目並べのAIを重回帰分析で作る

[English](README.en.md) | [日本語](README.md)

## 概要
このプロジェクトは、三目並べ（Tic Tac Toe）のゲームをプレイするAIを重回帰分析を用いて作成するものです。AIは、ゲームの盤面状態を特徴ベクトルに変換し、重回帰モデルを使用して最適な手を選択します。

## ファイル構成
- `tictactoe.py`: 三目並べのゲームロジックを実装したファイル。
- `scoring.py`: ゲームのスコアリングとランダムなゲーム記録を扱うクラスを実装したファイル。
- `regression.py`: 重回帰分析モデルを使用して最適な手を選択するクラスを実装したファイル。
- `dataset.py`: ゲームの盤面パターンを管理し、データセットを生成するクラスを実装したファイル。
- `ml_tictactoe.py`: 重回帰分析モデルを使用して三目並べのゲームを開始するメインファイル。
- `README.md`: このプロジェクトの日本語版の説明書。
- `README.en.md`: このプロジェクトの英語版の説明書。

## 使い方
1. 必要なライブラリをインストールします。
    ```sh
    pip install pandas scikit-learn
    ```

2. 学習データを作成します（ランダムな打ち手から生成されます）。
    ```sh
    python dataset.py
    ```

3. `ml_tictactoe.py`を実行して、重回帰分析モデルを使用した三目並べのゲームを開始します。
    ```sh
    python ml_tictactoe.py
    ```

## リンク
詳細な解説は、以下の記事を参照してください。
https://qiita.com/y-tetsu/items/8fcacea73d58ab692196
