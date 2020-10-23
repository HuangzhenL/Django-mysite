from django.shortcuts import render
import requests
import json


# 设置主页对应的页面 + 传到主页的数据内容
def home(request):
    # 使用requests模块得到对应api的json内容，然后使用json.loads获取其内容
    api_request = requests.get('https://api.github.com/users?since=0')
    api = json.loads(api_request.content)
    # 返回函数render中的参数包含request,''-要跳转的页面,{key:value}-传递到页面的数据
    return render(request, 'home.html', {'api': api})


def user(request):
    # 获取搜索框中输入的内容，前端搜索框文本的名称为input_content
    user_name = request.POST['input_content']
    if user_name:  # 输入内容不为空
        # 同home函数中获取api接口内容
        user_request = requests.get(url='https://api.github.com/users/' + user_name)
        user_info = json.loads(user_request.content)
        # 返回函数包含两个数据，分别是要搜索的用户名和对应的用户信息
        return render(request, 'user.html', {'input_contents': user_name, 'user_info': user_info})
    else:
        # 若搜索框内没有输入，则进行提示
        notfound = '请在搜索框中输入您需要查询的用户...'
        return render(request, 'user.html', {'notfound': notfound})

# def user(request):
#     # 判断是否使用了POST方法，只有在使用搜索按钮时，才会调用POST
#     if request.method == 'POST':
#         user_name = request.POST['input_content']  # 获取搜索框中输入的内容，前端搜索框文本的名称为input_content
#         # 同home函数中获取api接口内容
#         user_request = requests.get(url='https://api.github.com/users/' + user_name, verify=False)
#         user_info = json.loads(user_request.content)
#         # 返回函数包含两个数据，分别是要搜索的用户名和对应的用户信息
#         return render(request, 'user.html', {'input_contents': user_name, 'user_info': user_info})
#     else:
#         # 若搜索框内没有输入，则进行提示
#         notfound = '请在搜索框中输入您需要查询的用户...'
#         return render(request, 'user.html', {'notfound': notfound})
