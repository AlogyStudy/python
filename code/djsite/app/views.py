from django.shortcuts import render, redirect, HttpResponse
# from app.models import Press, Book, Author
import json

# Create your views here.

def login(request):
    print(dir(request))
    # return HttpResponse('ok')
    # print(request.POST, 'post')
    # print(request.Method, 'method')
    # print(request.GET, 'get')
    return render(request, 'login.html', {'ret': 'aaaa'})

# def press_list(request):
#     press_list = Press.objects.all().order_by('id')

#     return render(request, 'press_list.html', {'press_list': press_list})

# def add_list(request):
#     if request.method == 'POST':
#         press_name = request.POST.get('name')
#         Press.objects.create(name=press_name)
#         return redirect('/press_list/')

#     return render(request, 'add_list.html')

# def del_list(request):
#     del_id = request.GET.get('id')
#     Press.objects.filter(id=del_id).delete()

#     return redirect('/press_list/')

# def edit_press(request):
#     edit_id = request.POST.get('id')
#     edit_press = Press.objects.get(id=edit_id)
#     if request.method == 'POST':
#         new_name = request.POST.get('name')
#         edit_press.name = new_name
#         edit_press.save() # 注意保存
#         return redirect('/press_list/')
        
#     return render(request, 'edit_list.html', {'edit_item', edit_press})


# def book_list(request):
#     ret = Book.objects.all()

#     render(request, 'book_list.html', {'data': ret})

# def author_list(request):
#     author_data = Author.objects.all()

#     # for item in author_data:
#     #     print(item.books.all()) # 连表查询，使用all()查询出数据来
#     return render(request, 'author_list.html', {'author_data': author_data})

# def upload(request):
#     if request.method == 'POST':
#         # print(request.FILES) # 文件接收
#         f_dict = request.FILES.get('name') # 文件字典
#         print(f_dict)
#         with open(f_dict, 'wb') as f:
#             for chunk in f_dict.chunk():
#                 f.write(chunk)

#     return render(request, 'upload.html')


from django.http import JsonResponse
def json_data(request):
    ret = {'name': 'su', 'age': 30}
    # return HttpResponse(json.dumps(ret))
    return JsonResponse(ret)

