from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import Profile, Posts
from .forms import PostsForm


def edit_post(request, pk):
    post = Posts.objects.get(id=pk)

    if request.method != 'POST':
        form = PostsForm(instance=post)

    else:
        form = PostsForm(instance=post, data=request.POST)

        post.status = 'edited'
        post.save()

        if form.is_valid():
            form.save()
            return redirect('ice_age:dashboard')

    context = {'post': post, 'form': form}
    return render(request, 'ice_age/edit_post.html', context)


def dashboard(request):
    if request.method == "POST":
        form = PostsForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("ice_age:dashboard")

    form = PostsForm()

    if request.user.is_authenticated:
        followed_users = Posts.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by(
            "-created_at")

        return render(request, "ice_age/dashboard.html",
                      {'form': form, 'posts': followed_users})
    else:
        return redirect("log:logout")


class DeletePost(DeleteView):
    model = Posts
    success_url = "/"
    template_name = "ice_age/delete_post.html"


# отражение всех профилей кроме своего
class ProfileList(ListView):
    model = Profile
    template_name = "ice_age/profile_list.html"
    context_object_name = 'profiles'

    def get_queryset(self):
        result = Profile.objects.exclude(user=self.request.user)
        return result


def profile(request, pk):
    # проверка профиля
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "ice_age/profile.html", {"profile": profile})
