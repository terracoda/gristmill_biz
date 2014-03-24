from homepage.models import PageIntro

def get_page_intros(request):
    page_intros = PageIntro.objects.filter(status=1)  
    return {'PAGE_INTROS': page_intros}