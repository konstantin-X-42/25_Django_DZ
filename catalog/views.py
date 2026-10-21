from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from catalog.models import Product, ContactInfo
from catalog.forms import ProductForm


class ProductListView(ListView):
    """Контроллер главной страницы"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Получаем все товары
        queryset = super().get_queryset()

        # Сохраняем твой вывод в консоль для проверки первых 5 товаров
        print("\n--- ПОСЛЕДНИЕ ПРОДУКТЫ В КОНСОЛИ ---")
        for product in queryset[:5]:
            print(f"ID: {product.id} | {product.name} | Цена: {product.price} руб.")
        print("---------------------------------------\n")

        return queryset


class CategoriesListView(ListView):
    """Контроллер для страницы категорий"""
    model = Product
    template_name = 'catalog/21-2_home2.html'
    context_object_name = 'products'


class OrdersTemplateView(TemplateView):
    """Контроллер для страницы заказов"""
    template_name = 'catalog/21-2_home3.html'


class ContactsTemplateView(TemplateView):
    """Контроллер страницы контактов"""
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем данные контактов
        try:
            context['contact_data'] = ContactInfo.objects.first()
        except Exception:
            context['contact_data'] = None
        return context

    def post(self, request, *args, **kwargs):
        # Обработка отправки формы обратной связи
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Новое сообщение!")
        print(f"Имя: {name} | Email: {email}")
        print(f"Текст: {message}")
        print("-" * 20)

        # Рендерим страницу обратно с сообщением об успехе
        context = self.get_context_data()
        context['success_message'] = 'Спасибо! Ваше сообщение успешно отправлено.'
        return self.render_to_response(context)


class ProductDetailView(DetailView):
    """Контроллер страницы с подробной информацией о товаре"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    """Контроллер формы для создания нового товара с защитой и валидацией"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:21-2_home1')  # Перенаправление на главную после создания
