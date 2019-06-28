from django.urls import path
from status.api.views import (
    StatusListSearchAPIView, 
   
    )

urlpatterns = [
    path('', StatusListSearchAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    # path('<int:status_id>', StatusDetailAPIView.as_view()),
    # path('<int:status_id>', StatusUpdateAPIView.as_view()),
    # path('<int:status_id>', StatusDeleteAPIView.as_view()),
   
]

# Start with
#   /api/status ->List
#   /api/status/create -> Create
#   /api/status/12/ -> Detail
#   /api/status/12/update/ -> Update
#   /api/status/12/delete/ -> Delete

# End with
#   /api/status/ -> CRUD
#   /api/status/1/ -> CRUD

# Final
#   /api/status/ -> CRUD & LS


