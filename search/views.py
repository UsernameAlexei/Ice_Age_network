from django.views.generic import ListView
from ice_age.models import Profile, Posts
from django.contrib.auth.models import User
from django.db.models import Q


class SearchView(ListView):
    model = Profile
    template_name = 'search/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')

        if query:

            user_result = User.objects.filter(
                Q(first_name__iregex=query) | Q(last_name__iregex=query) | Q(username__iregex=query))
            user_id = [user.id for user in user_result]

            profile_result = Profile.objects.filter(user_id__in=user_id)

            result = profile_result

        else:
            result = None
        return result
