from django import views
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('usuarios', views.UsuarioViewSet, basename='usuario')
router.register('clientes', views.ClienteViewSet, basename='cliente')
router.register('conta', views.ContaViewSet, basename='conta')
# router.register('cartao', views.CartaoViewSet, basename='cartao')
# router.register('movimentacao', views.MovimentacoesViewSet, basename='movimentacao')
# router.register('emprestimo', views.EmprestimoViewSet, basename='emprestimo')
# router.register('pagamento', views.PagamentoEmprestimosViewSet, basename='pagamento')
# router.register('extrato', views.ExtratoViewSet, basename='extrato')
# router.register('imagens', views.ImagemViewSet, basename='imagens')
router.register('login', views.LoginViewSet, basename='login')
urlpatterns = router.urls