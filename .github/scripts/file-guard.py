#!/usr/bin/env python3
"""
Проверяет, что автор PR меняет только разрешённые для него файлы.
Конфигурация — в .github/file-guard-mapping.json.
"""
import fnmatch
import json
import os
import subprocess
import sys

MAPPING_PATH = ".github/file-guard-mapping.json"


def load_mapping():
    with open(MAPPING_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_changed_files(base_ref):
    """Возвращает список изменённых файлов в формате (status, path)."""
    compare = f"origin/{base_ref}...HEAD"
    result = subprocess.run(
        ["git", "diff", "--name-status", compare],
        capture_output=True,
        text=True,
        check=True,
    )
    changes = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            status = parts[0][0].upper()
            path = parts[-1]
            changes.append((status, path))
    return changes


def is_allowed(path, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
        # поддержка двойной звёздочки для подпапок
        if "**" in pattern:
            norm = pattern.replace("**", "*")
            if fnmatch.fnmatch(path, norm):
                return True
    return False


def main():
    mapping = load_mapping()
    strict = mapping.get("strict", False)
    authors = mapping.get("authors", {})

    pr_author = os.environ.get("PR_AUTHOR") or os.environ.get("GITHUB_ACTOR", "")
    base_ref = os.environ.get("BASE_REF", "main")

    print(f"PR author: {pr_author}")
    print(f"Base ref: {base_ref}")

    if pr_author not in authors:
        msg = (
            f"Автор '{pr_author}' не найден в {MAPPING_PATH}. "
            "Добавьте его юзернейм и разрешённые файлы."
        )
        if strict:
            print(f"::error::{msg}")
            sys.exit(1)
        else:
            print(f"::warning::{msg} Проверка файлов отключена (strict=false).")
            sys.exit(0)

    author_cfg = authors[pr_author]
    allowed_patterns = author_cfg.get("allowed", [])
    prefix = author_cfg.get("prefix", pr_author)

    changes = get_changed_files(base_ref)
    if not changes:
        print("Нет изменённых файлов.")
        sys.exit(0)

    forbidden = []
    figure_prefix_violations = []

    for status, path in changes:
        print(f"  [{status}] {path}")
        if not is_allowed(path, allowed_patterns):
            forbidden.append(path)

        # Новые рисунки в figures/ должны иметь префикс автора или быть заменой своего
        if status == "A" and path.startswith("figures/"):
            filename = os.path.basename(path)
            if not filename.lower().startswith(prefix.lower() + "_"):
                figure_prefix_violations.append(path)

    exit_code = 0

    if forbidden:
        print("\n::error::Запрещённые изменения:")
        for p in forbidden:
            print(f"  - {p}")
        print(
            f"\nРазрешённые для {pr_author}: {allowed_patterns}\n"
            "Если нужно изменить список — отредактируйте .github/file-guard-mapping.json."
        )
        exit_code = 1

    if figure_prefix_violations:
        print("\n::error::Новые рисунки без префикса автора:")
        for p in figure_prefix_violations:
            print(f"  - {p}")
        print(f"Ожидаемый префикс: {prefix}_<смысл>.png")
        exit_code = 1

    if exit_code == 0:
        print("\nВсе изменённые файлы разрешены для этого автора.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
