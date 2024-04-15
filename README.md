# low_office_app_new_dev
法律事務所の予約フォーム
# 主な内容
Flaskアプリケーションでのパス構成は、あなたのファイルとフォルダの配置に基づいています。以下に、提案したFlaskアプリケーション構成の主要な部分を示します。

Pythonファイル (app.py):

このファイルはFlaskアプリケーションの設定、ルート定義、モデル定義を含んでおり、アプリケーションのメインファイルとして機能します。
テンプレートフォルダ (templates):

Flaskでは、HTMLファイルは通常このフォルダに配置されます。このフォルダはFlaskによって自動的に認識され、render_template() 関数を使用してHTMLページをレンダリングする際にここからテンプレートを探します。
静的ファイルフォルダ (static):

静的ファイル（CSS、JavaScriptファイル、画像など）は、このフォルダに配置します。これらのファイルはウェブページのスタイリングや機能のために使用されます。

この構成では、app.py がアプリケーションの起動点であり、templates および static フォルダはそれぞれHTMLテンプレートと静的ファイルを格納するために使用されます。各テンプレートはCSSファイルをリンクするために <link> タグ内で url_for('static', filename='css/該当するCSSファイル名') を使用して、CSSパスを指定します。

# ディレクトリ構造
 * /low_office_app
  *  /static
   *     /css
    *        base.css           # 基本スタイル
     *       form.css           # 予約フォーム専用スタイル
      *      confirmation.css   # 予約確認ページ専用スタイル
       *     users.css          # ユーザー一覧ページ専用スタイル
  *  /templates
   *     base.html              # 全ページ共通のベーステンプレート
    *    form.html              # 予約フォームテンプレート
     *   confirm.html           # 予約確認ページテンプレート
      *  users.html             # ユーザー一覧ページテンプレート
  * app.py                     # Flaskアプリケーションのメインファイル
  heroku git:remote -a git@github.com:manabutice/low_office_app_new_dev.git