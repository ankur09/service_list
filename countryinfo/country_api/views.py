from django.db.models import Q

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter
	)

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	DestroyAPIView
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
	)


from countryinfo.models import Country
from .serializers import CountryCreateSerializer, CountryDetailSerializer,CountryListSerializer,CountryUpdateSerializer,CountryDeleteSerializer

class CountryCreateAPIView(CreateAPIView):
	queryset=Country.objects.all()
	serializer_class=CountryCreateSerializer
	permission_classes=[IsAdminUser]
	

	def perform_create(self, serializer):
		serializer.save(user= self.request.user)


class CountryDetailAPIView(RetrieveAPIView):
	queryset=Country.objects.all()
	serializer_class=CountryDetailSerializer
	permission_classes=[IsAdminUser,IsAuthenticated]


class CountryListAPIView(ListAPIView):
	queryset=Country.objects.all()
	serializer_class=CountryListSerializer
	permission_classes=[AllowAny]

	filter_backends=[SearchFilter,OrderingFilter]
	search_fields=['id','code','name','user__first_name']

	def get_queryset(self,*args,**kwargs):
		queryset_list=Country.objects.all()
		query=self.request.GET.get('q')
		if query:
			queryset_list=queryset_list.filter(
				Q(code__icontains=query)|
				Q(name__icontains=query)
				).distinct()
		return queryset_list

class CountryUpdateAPIView(UpdateAPIView):
	queryset=Country.objects.all()
	serializer_class=CountryUpdateSerializer
	permission_classes=[IsAdminUser]

	def perform_update(self,serializer):
		serializer.save(user=self.request.user)

class CountryDeleteAPIView(DestroyAPIView):
	queryset=Country.objects.all()
	serializer_class=CountryDeleteSerializer
	lookup_field='pk'
