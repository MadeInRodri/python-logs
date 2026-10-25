import re
from datetime import datetime
from pathlib import Path


def analyze_log(log_file):
    stats = {
        "total_events": 0,
        "info": 0,
        "warning": 0,
        "error": 0,
        "invalid_severity": 0,
        "correct_dates": 0,
        "incorrect_dates": 0,
        "missing_messages": 0,
        "invalid_events": 0,
    }
    severity_pattern = re.compile(r"\[(INFO|WARNING|ERROR)\]", re.IGNORECASE)
    date_pattern = re.compile(r"(?:[0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{2}/[0-9]{2}/[0-9]{4})")

    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            stats["total_events"] += 1
            parts = line.split()
            event_is_invalid = False

            # Valida la severidad y cuenta únicamente los niveles reconocidos.
            if parts and severity_pattern.fullmatch(parts[0]):
                level = parts[0][1:-1].lower()
                stats[level] += 1
            else:
                stats["invalid_severity"] += 1
                event_is_invalid = True

            # Valida la estructura y la existencia de la fecha.
            if len(parts) >= 2 and date_pattern.fullmatch(parts[1]):
                date_format = "%Y-%m-%d" if "-" in parts[1] else "%d/%m/%Y"
                try:
                    datetime.strptime(parts[1], date_format)
                except ValueError:
                    stats["incorrect_dates"] += 1
                    event_is_invalid = True
                else:
                    stats["correct_dates"] += 1
            else:
                stats["incorrect_dates"] += 1
                event_is_invalid = True

            # El mensaje debe contener al menos una palabra después de la fecha.
            if len(parts) < 3:
                stats["missing_messages"] += 1
                event_is_invalid = True

            # Cada línea se cuenta como inválida una sola vez.
            if event_is_invalid:
                stats["invalid_events"] += 1

    return stats


def main():
    # Busca archivos de log en la carpeta desde la que se ejecuta el script.
    log_files = sorted(
        (path for path in Path.cwd().iterdir() if path.is_file() and path.suffix.lower() in {".log", ".txt"}),
        key=lambda path: path.name.lower(),
    )

    if not log_files:
        print("No se encontraron archivos .log o .txt en la carpeta actual.")
        return

    print("Elija el archivo log a leer:")
    for number, path in enumerate(log_files, start=1):
        print(f"[{number}] {path.name}")

    while True:
        selection = input("\nIngrese el número del archivo: ").strip()
        if selection.isdigit() and 1 <= int(selection) <= len(log_files):
            selected_file = log_files[int(selection) - 1]
            break
        print(f"Selección inválida. Ingrese un número entre 1 y {len(log_files)}.")

    stats = analyze_log(selected_file)
    valid_events = stats["total_events"] - stats["invalid_events"]

    print("\n" + "=" * 46)
    print("               REPORTE DE LOGS")
    print("=" * 46)
    print(f"Archivo analizado  : {selected_file.name}")
    print(f"Total de eventos   : {stats['total_events']}")
    print(f"Eventos válidos    : {valid_events}")
    print(f"Eventos inválidos  : {stats['invalid_events']}")
    print("-" * 46)
    print("Niveles de severidad")
    print(f"  Información      : {stats['info']}")
    print(f"  Advertencias     : {stats['warning']}")
    print(f"  Errores          : {stats['error']}")
    print(f"  Severidad inválida: {stats['invalid_severity']}")
    print("-" * 46)
    print("Validación de eventos")
    print(f"  Fechas correctas : {stats['correct_dates']}")
    print(f"  Fechas incorrectas: {stats['incorrect_dates']}")
    print(f"  Mensajes faltantes: {stats['missing_messages']}")
    print("=" * 46)


if __name__ == "__main__":
    main()
