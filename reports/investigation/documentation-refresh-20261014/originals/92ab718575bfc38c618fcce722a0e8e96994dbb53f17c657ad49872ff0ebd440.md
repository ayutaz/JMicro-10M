---
license: cc-by-4.0
language:
- ja
tags:
- japan
- pre-training
- continued-pretraining
- text-generation
- parquet
task_categories:
- text-generation
- fill-mask
- text-classification
pretty_name: OpenJA
size_categories:
- 100M<n<1B
---

# OpenJA

![image](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/QUvtJx_4Z_dq275lr13OG.png)

## 🇬🇧 English Description

**OpenJA** is a dataset of clean, officially published parliamentary transcripts of the Japanese language. It is characterized by high-quality text (without web noise, HTML, advertising) and reliable metadata, but it represents one narrow language register (official/parliamentary speech) and is better suited as an addition to more diverse corpora than as the only source for a general-purpose pretrain.

### 📊 Dataset Statistics
- **Total Records**: 3,244,877. 
- **Total Size**: ~679,496,535 tokens (tokenized with `Qwen/Qwen3.5-9B`).
- **Format**: Parquet.
- **Years of publication of records**: 2000-2026.

### 🏗️ Dataset Structure

| Field | Type | Description |
|---|---|---|
| `id` | `string` | Unique speech ID (`speechID` from the Kokkai API) |
| `issueID` | `string` | ID of the meeting this speech belongs to |
| `year` | `int` | Year of the meeting — **primary field for filtering** the dataset by period |
| `date` | `string` | Meeting date in `YYYY-MM-DD` format |
| `session` | `string` | Diet session number |
| `nameOfHouse` | `string` | Chamber: `衆議院` (House of Representatives) or `参議院` (House of Councillors) |
| `nameOfMeeting` | `string` | Name of the committee/meeting |
| `issue` | `string` | Transcript issue number |
| `closing` | `string` | Meeting-closing indicator |
| `speaker` | `string` | Speaker's name |
| `speakerYomi` | `string` | Speaker's name in furigana (reading) |
| `speakerGroup` | `string` | Speaker's party/faction |
| `speakerPosition` | `string` | Speaker's official position |
| `speakerRole` | `string` | Speaker's role in the meeting (e.g., chairperson) |
| `speechOrder` | `int` | Sequential order of the speech within the meeting |
| `text` | `string` | **Cleaned** speech text (no HTML, stenographer remarks, or boilerplate phrases) |
| `speechURL` | `string` | Link to the original record on the Kokkai website |

### 🛠️ Creation and Curation
1. **Source**: Texts were programmatically harvested from **Kokkai Kaigiroku** *(国会会議録)*.
2. **Cleaning**: Automated removal of HTML tags, footnotes, editorial tables, and navigation templates.

### ⚖️ License and Copyright
- **The Compilation/Curation**: Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to use, modify, and distribute this dataset commercially or non-commercially, provided you give appropriate credit.

### 💻 Usage Example
```python
from datasets import load_dataset

# Load Parquet file
dataset = load_dataset("maxzt/OpenJA", split="train")
```

### 🗺️ Roadmap & Future Expansions

This dataset is a living project. OpenJA-Max with an extended range of years (1947-2026) will be released soon. 

---

## 🇷🇺 Описание на русском языке

**OpenJA** — датасет чистых, официально изданных парламентских стенограмм японского языка. Отличается высоким качеством текста (без веб-шума, HTML, рекламы) и надёжной метадатой, но представляет собой один узкий языковой регистр (официальная/парламентская речь) и лучше подходит как дополнение к более разнообразным корпусам, чем как единственный источник для претрейна общего назначения.

### 📊 Статистика датасета
- **Всего записей**: 3,244,877.
- **Общий объем**: ~679,496,535 токенов (токенизированно с помощью `Qwen/Qwen3.5-9B`).
- **Формат**: Parquet.
- **Годы публикации записей**: 2000-2026.

### 🏗️ Структура данных

| Поле | Тип | Описание |
|---|---|---|
| `id` | `string` | Уникальный ID реплики (`speechID` из API Kokkai) |
| `issueID` | `string` | ID заседания, к которому относится реплика |
| `year` | `int` | Год заседания — **основное поле для фильтрации** датасета по периоду |
| `date` | `string` | Дата заседания в формате `YYYY-MM-DD` |
| `session` | `string` | Номер сессии парламента |
| `nameOfHouse` | `string` | Палата: `衆議院` (нижняя) или `参議院` (верхняя) |
| `nameOfMeeting` | `string` | Название комитета/заседания |
| `issue` | `string` | Номер выпуска стенограммы |
| `closing` | `string` | Признак закрытия заседания |
| `speaker` | `string` | Имя выступавшего |
| `speakerYomi` | `string` | Имя выступавшего в фуригане (чтение) |
| `speakerGroup` | `string` | Партийная фракция выступавшего |
| `speakerPosition` | `string` | Должность выступавшего |
| `speakerRole` | `string` | Роль в заседании (например, председатель) |
| `speechOrder` | `int` | Порядковый номер реплики внутри заседания |
| `text` | `string` | **Очищенный** текст реплики (без HTML, служебных ремарок, шаблонных фраз) |
| `speechURL` | `string` | Ссылка на оригинал на сайте Kokkai |

### 🛠️ Процесс создания и очистки
1. **Источник**: Тексты были собраны программным путем из **Kokkai Kaigiroku** *(国会会議録)*.
2. **Очистка**: Автоматическое удаление HTML-тегов, сносок, редакционных таблиц и навигационных шаблонов.

### ⚖️ Лицензия и авторские права
- **Сборка и курирование датасета**: Лицензия [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Вы можете свободно использовать, модифицировать и распространять этот датасет в коммерческих и некоммерческих целях при условии указания авторства коллекции.

### 💻 Пример использования
```python
from datasets import load_dataset

# Загрузка Parquet файла
dataset = load_dataset("maxzt/OpenJA", split="train")
```

### 🗺️ Планы на будущее и расширение датасета

Этот набор данных - действующий проект. Скоро будет выпущен OpenJA-Max с расширенным диапазоном лет (1947-2026).

### 🙏 Благодарности
Источником данных выступает Kokkai Kaigiroku (国会会議録).

---