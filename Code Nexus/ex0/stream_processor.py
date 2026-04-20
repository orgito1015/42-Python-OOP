from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class for data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Default implementation for output formatting."""
        return result


class NumericProcessor(DataProcessor):
    """Processor for numeric data types."""

    def process(self, data: Any) -> str:
        """Process numeric data and return formatted result."""
        try:
            if self.validate(data):
                return self.format_output(data)
            return "Invalid numeric data"
        except Exception as e:
            return f"Error processing numeric data: {e}"

    def validate(self, data: Any) -> bool:
        """Validate that data contains only numeric values."""
        print("Validation: Numeric data verified")
        try:
            if not isinstance(data, (list, tuple)):
                return False
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        except Exception:
            return False

    def format_output(self, data: Any) -> str:
        """Format numeric data with sum and average."""
        total = sum(data)
        avg = total / len(data) if len(data) > 0 else 0
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Processor for text data types."""

    def process(self, data: Any) -> str:
        """Process text data and return formatted result."""
        try:
            if self.validate(data):
                return self.format_output(data)
            return "Invalid text data"
        except Exception as e:
            return f"Error processing text data: {e}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a string."""
        print("Validation: Text data verified")
        try:
            return isinstance(data, str)
        except Exception:
            return False

    def format_output(self, data: Any) -> str:
        """Format text data with character and word count."""
        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    """Processor for log entry data types."""

    def process(self, data: Any) -> str:
        """Process log data and return formatted result."""
        try:
            if self.validate(data):
                return self.format_output(data)
            return "Invalid log data"
        except Exception as e:
            return f"Error processing log data: {e}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a log entry string."""
        print("Validation: Log entry verified")
        try:
            return isinstance(data, str) and ":" in data
        except Exception:
            return False

    def format_output(self, data: Any) -> str:
        """Format log data with severity level detection."""
        parts = data.split(":", 1)
        if len(parts) >= 2:
            level = parts[0].strip().upper()
            message = parts[1].strip()

            if level in ["ERROR", "CRITICAL", "FATAL"]:
                return f"[ALERT] {level} level detected: {message}"
            elif level in ["WARNING", "WARN"]:
                return f"[WARNING] {level} level detected: {message}"
            else:
                return f"[{level}] {level} level detected: {message}"
        return data


def main():
    """Demonstrate polymorphic data processing."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric = NumericProcessor()
    print("Processing data: [1, 2, 3, 4, 5]")
    result = numeric.process([1, 2, 3, 4, 5])
    print(f"Output: {result}\n")

    print("Initializing Text Processor...")
    text = TextProcessor()
    print('Processing data: "Hello Nexus World"')
    result = text.process("Hello Nexus World")
    print(f"Output: {result}\n")

    print("Initializing Log Processor...")
    log = LogProcessor()
    print('Processing data: "ERROR: Connection timeout"')
    result = log.process("ERROR: Connection timeout")
    print(f"Output: {result}\n")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")

    processors = [
        (numeric, [1, 2, 3]),
        (text, "Hello Nexus"),
        (log, "INFO: System ready")
    ]

    for i, (processor, data) in enumerate(processors, 1):
        result = processor.process(data)
        print(f"Result {i}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
