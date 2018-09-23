from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Shop, Review
from .forms import ReviewForm

index = ListView.as_view(model=Category)

category_detail = DetailView.as_view(model=Category)

shop_detail = DetailView.as_view(model=Shop)


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        self.shop = get_object_or_404(Shop, pk=self.kwargs['pk'])
        
        review = form.save(commit=False)
        review.shop = self.shop
        review.creator = self.request.user # 현재 유저를 creator에 대응
        
        return super().form_valid(form)

    def get_success_url(self):
        return self.shop.get_absolute_url()

review_new = CreateView.as_view(model=Review, form_class=ReviewForm)