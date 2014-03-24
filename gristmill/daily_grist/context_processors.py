from daily_grist.models import Entry

def get_recent_entries(request):
    recent_news_list = Entry.objects.order_by("-pub_date")[:1]  
    return {'ENTRY_LIST': recent_news_list}