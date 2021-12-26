# python_study
ツイッターAPIを使用して呟きを取得・加工・表示するプログラム群  
APIキーはconfig.pyに記入  
①Get_twitter.pyで、任意のアカウントから呟き本文をinput_data.txtに出力（ソースコード内でアカウント名指定  
②disp_image.pyでinput_data.txt内のデータを加工してワードクラウド形式で表示  
メモ：実行時>python3 disp_image.py input_data.txt remove_word.txtで起動  
  
③無意味な頻出単語についてはremove_word.txtに頻出単語を書き込む事で除外できる（手入力  
④disp_image.py実行　
③④繰り返し  
  
メモ：ReadMe.mdは改行が半角スペース二個らしい
