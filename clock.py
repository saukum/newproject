"""Выводит текущее время в терминале.

Запуск:
    python clock.py          # обновляется каждую секунду, выход — Ctrl+C
    python clock.py --once   # вывести время один раз и выйти
"""

import argparse
import time
from datetime import datetime


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main() -> None:
    parser = argparse.ArgumentParser(description="Текущее время в терминале")
    parser.add_argument("--once", action="store_true", help="вывести время один раз и выйти")
    args = parser.parse_args()

    if args.once:
        print(now_str())
        return

    try:
        while True:
            print(f"\r{now_str()}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
