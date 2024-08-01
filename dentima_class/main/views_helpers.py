import re

# Create your views here.

def extract_youtube_id(url):
    # Регулярное выражение для извлечения ID видео из URL
    pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
    match = pattern.search(url)
    return match.group(1) if match else None

def grouped(queryset, n):
    """Группирует объекты QuerySet по колонкам."""
    # Преобразуем QuerySet в список
    items = list(queryset)
    # Разбиваем список на группы по `n` элементов
    return [items[i::n] for i in range(n)]