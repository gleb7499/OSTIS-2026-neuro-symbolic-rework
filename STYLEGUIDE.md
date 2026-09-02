# Единый стиль статьи OSTIS-2026

> Этот файл — для людей и для ИИ-агентов (Claude, Kimi Code, Copilot и др.).  
> Перед правкой своего черновика прочитайте его. Если возникает конфликт между этим гайдом и здравым смыслом/заданием автора — приоритет у автора.

---

## 1. Общий тон

- **Формально-научный, технический.** Статья для конференции OSTIS / IEEE.
- **Лаконичность.** Убирайте слова, без которых предложение не теряет смысла.
- **Конкретика.** Каждый раз, когда можно, привязывайте утверждение к пастеризационной установке, ISA-88, PLCnext или OSTIS.
- **Не маркетинг.** Избегайте эпитетов: «revolutionary», «cutting-edge», «unprecedented», «best-in-class» без конкретных доказательств.

### Примеры

| Плохо | Хорошо |
|-------|--------|
| SCADA systems are very important and have a long history. | SCADA systems evolved from monolithic mainframes in the 1960s into networked platforms that now integrate IoT and cloud computing. |
| This is a very big problem for many companies. | The heterogeneity of legacy protocols complicates integration with modern MES/ERP systems. |

---

## 2. Структура предложений и абзацев

- **Одна мысль — одно предложение.** Не пишите цепочки через `, and`, `, but`, `, so`.
- **Длина:** в среднем 15–25 слов. Допустимы короткие (5–10 слов) для акцента и длинные (до 35) — только если без них нельзя.
- **Абзац:** 3–5 предложений. Первое — тезис абзаца.
- **Переходы:** используйте `However`, `Therefore`, `Thus`, `Consequently`, `In contrast`, `For instance`.
- **Избегайте:** «It is interesting to note that...», «It should be mentioned that...», «As is known...».

### Примеры

| Плохо | Хорошо |
|-------|--------|
| SCADA systems are used in many areas and they collect data and they help operators and they also have problems. | SCADA systems collect real-time data and present it to operators. However, legacy deployments often rely on proprietary protocols, which complicates integration. |

---

## 3. Терминология

Используйте **один и тот же термин** на протяжении всей статьи. Не меняйте его ради "разнообразия".

| Правильно | Неправильно (не использовать) |
|-----------|-------------------------------|
| neuro-symbolic AI / neuro-symbolic control | neurosymbolic intelligence, AI mix, hybrid neural-symbolic approach |
| OSTIS Technology | OSTIS system, OSTIS platform |
| pasteurization unit / pasteurizer | pasteurization machine, device |
| PLCnext Control / AXC F 2152 | PLCnext controller, Phoenix controller |
| ISA-88, ISA-95, ISA-5.1 | S88, S95, ANSI/ISA-5.1 (если только не пояснено) |
| programmable logic controller (PLC) | PLC unit, logic controller |
| neural network (NN) | NN net, neuronet |

**Сокращения:**
- Впервые — полное название + аббревиатура в скобках: `Supervisory Control and Data Acquisition (SCADA)`.
- Далее — только аббревиатура.
- Не вводите новые сокращения без согласования с координатором.

---

## 4. Грамматика и орфография

- **Глаголы действия.** Предпочитайте активный залог: `The controller executes...` вместо `It is executed by the controller...`.
- **Пассив допустим** в разделах Methods/Implementation, когда объект важнее субъекта: `The model was trained on telemetry data`.
- **Без сокращений:** don't → do not, can't → cannot, isn't → is not.
- **Числа:**
  - Технические значения — цифрами: `24 V DC`, `800 MHz`, `20 neurons`.
  - От 1 до 10 в общем тексте — словами: `three layers`, `five detectors`.
  - Единицы измерения — через пробел: `500 mA`, `55 °C`, `4 GB eMMC`.
- **Запятые:** используйте Oxford comma в перечислениях из трёх и более элементов: `inputs, outputs, and control modules`.

---

## 5. Цитирование и источники

- **Каждое нетривиальное утверждение** должно иметь источник: `SCADA systems evolved from monolithic architectures \cite{boyer2004scada}`.
- **Стандарты и факты** — только авторитетные источники (ISA, IEC, IEEE, статьи, книги). Не используйте Википедию.
- **Цитата ставится после утверждения**, перед точкой: `...industrial standards \cite{Golenkov2019}.`
- **Не копируйте** формулировки из источников. Переформулируйте и укажите ссылку.
- **Новые источники** — через Давида (`bib/links.bib`), не вставляйте сами.

---

## 6. Рисунки и таблицы

- **Подписи к рисункам** — под рисунком (IEEE): `\caption{...} \label{fig:...}`.
- **Подписи к таблицам** — над таблицей: `\caption{...} \label{tab:...}`.
- **Ссылки:** `Fig.~\ref{fig:...}`, `Table~\ref{tab:...}`, `Eq.~\ref{eq:...}`. Неразрывный пробел `~` обязателен.
- **Новые рисунки** — в `figures/` с префиксом автора: `gleb_scada_timeline.png`.
- **TikZ:** используйте единую цветовую схему (синий/зелёный/оранжевый как в ISA-диаграммах) и одинаковые размеры узлов.

---

## 7. LaTeX-специфика

- **Курсив и жирный:** `\emph` для терминов при первом упоминании, `\textbf` — только для ключевых акцентов.
- **Метки:** не переименовывайте существующие `\label`, `\ref`, `\cite`.
- **Пробелы:** `~` перед `\ref`, `\cite`, `\citep`, `Fig.`, `Table`, `Eq.`.
- **Код:** для команд и запросов используйте `lstlisting` с `\small`.
- **Размер:** статья в формате `IEEEtran` conference; не меняйте шрифты и поля.

---

## 8. Работа с оригинальностью

Цель — поднять оригинальность за счёт **переформулировок**, а не удаления смысла.

- **Сокращайте шаблонные списки.** Например, историю SCADA не нужно описывать по десятилетиям с кучей маркеров.
- **Заменяйте общие примеры** на пастеризационную установку.
- **Переписывайте длинные цитаты** из источников своими словами + ссылка.
- **Добавляйте новые источники 2024–2026**, если они релевантны.

### Пример рерайта

| Исходное (низкая оригинальность) | Переформулированное |
|-----------------------------------|---------------------|
| SCADA is a system for supervisory control and data acquisition that is widely used in industry. | SCADA combines data acquisition and supervisory control to monitor geographically distributed industrial processes. |

---

## 9. Русский abstract

- Должен точно отражать содержание английского abstract.
- Тон — научный, без разговорных оборотов.
- Используйте термины: нейро-символическое управление, онтологический подход, Технология OSTIS, стандарты ISA-88/ISA-95/ISA-5.1.

---

## 10. Чек-лист перед коммитом

- [ ] Я прочитал этот `STYLEGUIDE.md`.
- [ ] Текст написан единым техническим тоном, без маркетинговых слов.
- [ ] Предложения не длиннее 35 слов, абзацы — 3–5 предложений.
- [ ] Терминология согласована с таблицей выше.
- [ ] Сокращения введены при первом упоминании.
- [ ] Цитаты стоят после утверждений, источники — авторитетные.
- [ ] Рисунки подписаны корректно, ссылки через `~\ref`.
- [ ] Я не менял чужие файлы, `main.tex` и служебные файлы.
