# Когда будет большое колличесвто handlers
#  ставим точку потому что файл находится в этой папке
# Важно не забывать подтягивать новые файлы в Handlers в этот файл
from .start import dp
from .help import dp
from .text import dp

from .all import dp

# С помощью all мы можем обращаться к нашему пакету handler и импортировать dp
# Теперь в main нам не нужно прописывать все handlers
__all__ = ['dp']
