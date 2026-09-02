# OSTIS-2026: доработка статьи «Neuro-symbolic control for pasteurization unit»

> **Цель:** поднять оригинальность статьи с текущих ~60 % до минимального порога **80 %** в системе проверки, сохранив научное содержание и формат IEEEtran.

---

## 1. Что это за «доклады»

Это **научная статья в формате LaTeX (IEEEtran)** для конференции ОСТИС-2026. Она описывает подход к управлению пастеризационной установкой с помощью **нейро-символического ИИ** на базе технологии OSTIS:

- обзор эволюции SCADA и промышленных стандартов;
- формализация стандартов ISA-88, ISA-95, ISA-5.1 в виде онтологий;
- нейроуправление и нейро-ПИД-регулятор;
- аппаратная платформа PLCnext (AXC F 2152);
- применение системы на предприятии «Савушкин продукт» и интеграция с EasyEPLANner.

Готовый PDF — файл `2026.pdf` в корне. Исходник — `main.tex`, разделы вынесены в `drafts/*.tex`, библиография — в `bib/links.bib`, рисунки — в `figures/`.

---

## 2. Как посмотреть / скомпилировать

### Быстрый способ
Откройте готовый PDF: `2026.pdf` любым PDF-ридером.

### Скомпилировать из LaTeX

На Windows рекомендуется **MiKTeX** (установлено в `C:\Users\kseni\AppData\Local\Programs\MiKTeX`). Если MiKTeX ещё не установлен:

```powershell
winget install --id MiKTeX.MiKTeX --silent --accept-package-agreements --accept-source-agreements
```

Компиляция в Git Bash / PowerShell из папки проекта:

```bash
pdflatex -interaction=nonstopmode -synctex=1 main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Если `pdflatex` не найден, используйте полный путь:

```bash
/c/Users/kseni/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdflatex -interaction=nonstopmode main.tex
```

> **Важно:** не коммитьте сгенерированные PDF/вспомогательные файлы (`.aux`, `.log`, `.out`, `.synctex.gz`). Они уже исключены в `.gitignore`.

---

## 3. Распределение участников

| Участник | GitHub | Файл черновика | Секции / задачи |
|----------|--------|----------------|-----------------|
| **Глеб** (координатор) | `@gleb7499` | `drafts/gleb_intro_scada.tex` | Introduction + History and background: from SCADA to AI-aided control systems; предложить версию Abstract/keywords. |
| **Юра** | `@Yura-108` | `drafts/yura_standards.tex` | AI and standards + Problems and state of the art + описания ISA-88/95/5.1. |
| **Дима** | `@DmitryRekun` | `drafts/dima_neuro.tex` | Neurocontrol + Neuro-symbolic control + Examples (Kaspersky MLAD, Amazon, Unitree G1). |
| **Женя** | `@EuZireael` | `drafts/zhenya_plcnext_pid.tex` | PLCnext and AXC F 2152 + Developed Neuro-PID controller. |
| **Давид** | `@Bidway` | `drafts/david_final.tex` | Завершающие секции: Examples of system operation, Integration, Use in control systems, Future development, Conclusion, Acknowledgment, русский abstract; **сборка/сверка библиографии** `bib/links.bib`. |

**Давиду выделена самая маленькая текстовая часть** — основная его нагрузка это финальная редакция, перекрёстные ссылки и библиография.

---

## 4. Общие правила работы

### 4.1. Что можно менять
- **Только свой файл** в `drafts/<имя>.tex`.
- **Рисунки** — общая папка `figures/`. Новые файлы называйте `<автор>_<смысл>.png` (например, `gleb_scada_evolution.png`), чтобы не конфликтовать.
- **Библиографию** физически редактирует только **Давид** (`bib/links.bib`). Остальные присылают новые источники в комментариях своего черновика, в issue или координатору.

### 4.2. Что трогать запрещено
- Чужие файлы в `drafts/`.
- Корневой `main.tex`, преамбула, стили `.cls`/`.sty`, `.github/` — только координатор (Глеб).
- Не переименовывай существующие метки (`\label`, `\ref`, `\cite`) без согласования.
- Не меняй шрифты, поля и класс `IEEEtran`.
- Не коммить собранный PDF и вспомогательные файлы.

### 4.3. Единый стиль письма

Чтобы статья не превратилась в сборник разных голосов, все правят текст в рамках одного стиля:

- [`STYLEGUIDE.md`](./STYLEGUIDE.md) — правила терминологии, структуры предложений, цитирования, рисунков и повышения оригинальности.

Кратко: лаконичный научный тон, одинаковые термины, одна мысль в предложении, авторитетные источники, рисунки с префиксом автора.

### 4.4. Нейросети / ИИ-агенты

Все участники пользуются Claude, Глеб — Kimi Code. Для нейросетей в репозитории есть два файла:

- [`AGENTS.md`](./AGENTS.md) — правила для ИИ-агентов.
- [`STYLEGUIDE.md`](./STYLEGUIDE.md) — единый стиль, который агент должен применять к правкам.

**Приоритет за человеком.** Если правила агента противоречат здравому смыслу или инструкции автора — делай так, как сказал человек. Нейросеть — вспомогательный инструмент, не главный редактор.

---

## 5. Рекомендуемый рабочий процесс

### Вариант A — через GitHub (рекомендуется)

1. Клонируйте репозиторий:

```bash
git clone https://github.com/gleb7499/OSTIS-2026-neuro-symbolic-rework.git
cd OSTIS-2026-neuro-symbolic-rework
```

2. Создайте ветку с именем `<github-username>/<краткое-назначение>`:

```bash
git checkout -b gleb7499/rewrite-intro
```

3. Работайте **только в своём `drafts/*.tex` и в `figures/`** (своими рисунками).

4. Коммитьте понятно:

```bash
git add drafts/gleb_intro_scada.tex figures/gleb_scada_evolution.png
git commit -m "gleb: rewrite intro, add new SCADA evolution figure"
```

5. Запушьте ветку и создайте Pull Request через GitHub CLI:

```bash
git push -u origin gleb7499/rewrite-intro
gh pr create --title "[Юра] rewrite standards section" --body "- переформулирован раздел AI and standards\n- добавлены 2 новых источника 2024-2025"
```

6. Другой участник (не автор PR) делает **Review**. После approve Глеб сливает (merge) PR.

### Вариант B — без GitHub (резервный)

Если кто-то не умеет работать с Git:

1. Работайте в своём черновике локально или в любом текстовом редакторе.
2. Присылайте изменённый `.tex` и новые рисунки координатору (Глебу).
3. Глеб вручную вносит правки в основной `main.tex` и собирает PDF.

> **Совет:** даже если вы не знаете Git, используйте Вариант A: в GitHub можно редактировать файл прямо в браузере, а Pull Request создаётся автоматически.

---

## 6. GitHub-ограничения: работа только в своих файлах

Включены два уровня защиты:

1. **Branch protection** для `main`:
   - прямые пуши в `main` запрещены;
   - любые изменения только через Pull Request;
   - требуется **минимум 1 approving review** перед merge.

2. **CODEOWNERS + `file-guard.yml`**:
   - В `.github/CODEOWNERS` каждый файл `drafts/*.tex` закреплён за конкретным участником.
   - GitHub Actions workflow `.github/workflows/file-guard.yml` проверяет PR: если автор меняет чужой файл, проверка падает и merge блокируется.
   - Папка `figures/` — общая; в ней можно работать всем, но новые файлы должны иметь префикс автора.

> **GitHub-юзернеймы всех участников заполнены, жёсткая проверка включена.** Если кто-то откроет PR с изменениями в чужом файле, workflow `file-guard` не пропустит merge.

---

## 7. Чек-лист участника перед сдачей

- [ ] Я редактировал только свой `drafts/*.tex` (и свои рисунки в `figures/`).
- [ ] Я не менял `main.tex`, `.cls`, `.sty`, `.github/`, чужие черновики.
- [ ] Новые источники передал Давиду/координатору, а не вставлял сам в `bib/links.bib`.
- [ ] Новые рисунки имеют уникальные имена и не перезаписывают чужие.
- [ ] Текст переформулирован, убраны длинные списки «из Википедии».
- [ ] Добавлены свежие источники 2024–2026 по теме (если есть).
- [ ] Проверил, что файл компилируется в `main.tex` без ошибок.

---

## 8. Ссылки и контакты

- **Координатор:** Глеб (@gleb7499).
- **Репозиторий:** `https://github.com/gleb7499/OSTIS-2026-neuro-symbolic-rework`
- **Полная защита файлов уже включена** — см. `.github/CODEOWNERS` и `.github/workflows/file-guard.yml`.

Если что-то непонятно — пишите в issues репозитория или координатору.
