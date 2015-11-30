from django_medusa.renderers import StaticSiteRenderer
from submissions.models import Submission

class HomeRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/",
            "/donate/",
        ])

class ImagesRenderer(StaticSiteRenderer):
    def get_paths(self):
        submissions = Submission.objects.filter(accepted_at__isnull=False).order_by('-accepted_at')
        paths = reduce(lambda x,y: x+y, [[image.file.url for image in submission.current_files] for submission in submissions], [])
        print paths
        return frozenset(paths)


renderers = [HomeRenderer, ImagesRenderer]
