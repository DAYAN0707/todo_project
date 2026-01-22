from django.http import HttpResponse, JsonResponse

# 1. シンプルなテキストを返す View関数
def hello_world_view(request):
    """
    ユーザーからのリクエストを受け取り、シンプルなテキストをHTTPレスポンスとして返します。
    """
    # <body>タグの中身に表示されるテキストを返しています
    return HttpResponse("<h1>Hello, Django View!</h1><p>これでViewが動いています！</p>")

# 2. JSONデータを返す View関数
def json_data_view(request):
    """
    JSONデータを返すView関数です。
    APIとしてデータを返却したい場合に利用します。
    """
    data = {
        'message': 'APIからデータが届きました。',
        'status': 'success',
        'items': ['Todoリスト1', 'Todoリスト2', 'Todoリスト3']
    }
    # Pythonの辞書（dictionary）をJSON形式に変換して返します
    return JsonResponse(data)