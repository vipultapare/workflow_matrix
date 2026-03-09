import sys
import json
from typing import List, Dict, Optional


class DataProcessor:
    """A simple class to process and manage data."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.data: List[Dict] = []

    def add_item(self, item: Dict) -> None:
        if not isinstance(item, dict):
            raise TypeError("Item must be a dictionary")
        self.data.append(item)

    def get_items(self) -> List[Dict]:
        return self.data.copy()

    def filter_by_name(self, name: str) -> List[Dict]:
        return [item for item in self.data if item.get("name") == name]

    def clear_data(self) -> None:
        self.data.clear()

    def __str__(self) -> str:
        return f"DataProcessor(name='{self.name}', items={len(self.data)})"


def calculate_sum(numbers: List[int]) -> int:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    return sum(numbers)


def calculate_average(numbers: List[int]) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def read_file(filepath: str) -> Optional[str]:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None


def save_json(data: Dict, filepath: str) -> bool:
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        return True
    except (IOError, TypeError) as e:
        print(f"Error saving JSON: {e}")
        return False


def main() -> int:
    processor = DataProcessor("MyProcessor")

    sample_items = [
        {"name": "Item1", "value": 100},
        {"name": "Item2", "value": 200},
        {"name": "Item1", "value": 150},
    ]

    for item in sample_items:
        processor.add_item(item)

    print(f"Processor: {processor}")
    print(f"All items: {processor.get_items()}")

    filtered = processor.filter_by_name("Item1")
    print(f"Items named 'Item1': {filtered}")

    numbers = [10, 20, 30, 40, 50]
    total = calculate_sum(numbers)
    average = calculate_average(numbers)

    print(f"\nNumbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average}")

    results = {
        "processor": str(processor),
        "total": total,
        "average": average,
        "items": processor.get_items(),
    }

    if save_json(results, "/tmp/results.json"):
        print("\nResults saved to /tmp/results.json")
    else:
        print("\nFailed to save results")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())