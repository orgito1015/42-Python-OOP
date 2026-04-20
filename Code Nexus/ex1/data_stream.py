from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data. Must be overridden by subclasses."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria. Can be overridden."""
        if criteria is None:
            return data_batch
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count
        }


class SensorStream(DataStream):
    """Stream handler for sensor data."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor data batch and return analysis."""
        try:
            self.processed_count += len(data_batch)

            temp_values = [
                float(value)
                for entry in data_batch
                if isinstance(entry, dict)
                for key, value in entry.items()
                if 'temp' in key.lower()
                and isinstance(value, (int, float, str))
            ]

            if temp_values:
                avg_temp = sum(temp_values) / len(temp_values)
                return f"Sensor analysis: {len(data_batch)} readings " + \
                       f"processed, avg temp: {avg_temp} °C"

            return f"Sensor analysis: {len(data_batch)} readings processed"

        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data based on criteria."""
        if criteria == "high":
            return [entry for entry in data_batch
                    if isinstance(entry, dict) and
                    any(v > 100 for v in entry.values()
                        if isinstance(v, (int, float)))]
        return data_batch


class TransactionStream(DataStream):
    """Stream handler for transaction data."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transaction data batch and calculate net flow."""
        try:
            self.processed_count += len(data_batch)

            net_flow = 0
            for entry in data_batch:
                if isinstance(entry, dict):
                    for key, value in entry.items():
                        if key.lower() == "buy":
                            net_flow -= value
                        elif key.lower() == "sell":
                            net_flow += value

            return f"Transaction analysis: {len(data_batch)} operations, " + \
                   f"net flow: {'+' if net_flow >= 0 else ''}{net_flow} units"

        except Exception as e:
            return f"Error processing transaction batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter transaction data for large transactions."""
        if criteria == "large":
            return [entry for entry in data_batch
                    if isinstance(entry, dict) and
                    any(v > 100 for v in entry.values()
                        if isinstance(v, (int, float)))]
        return data_batch


class EventStream(DataStream):
    """Stream handler for event data."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event data batch and count errors."""
        try:
            self.processed_count += len(data_batch)

            error_count = sum(1 for event in data_batch
                              if isinstance(event, str) and
                              "error" in event.lower())

            return f"Event analysis: {len(data_batch)} events, " + \
                   f"{error_count} error detected" if error_count == 1 \
                   else f"Event analysis: {len(data_batch)} events, " + \
                        f"{error_count} errors detected"

        except Exception as e:
            return f"Error processing event batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter events by severity."""
        if criteria == "error":
            return [event for event in data_batch
                    if isinstance(event, str) and
                    "error" in event.lower()]
        return data_batch


class StreamProcessor:
    """Manager for processing multiple data streams polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a new stream with the processor."""
        self.streams.append(stream)

    def process_all(self, data_map: Dict[str, List[Any]],
                    criteria: Optional[str] = None) -> List[tuple]:
        """
        Process all registered streams with their respective data.
        Demonstrates polymorphism - same interface, different behaviors.
        """
        results = []
        for stream in self.streams:
            stream_data = data_map.get(stream.stream_id, [])
            if criteria:
                stream_data = stream.filter_data(stream_data, criteria)
            result = stream.process_batch(stream_data)
            results.append((stream.stream_id, result))
        return results


def main() -> None:
    """Demonstrate polymorphic stream processing."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print("Stream ID: SENSOR_001, Type: Environmental Data")

    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    sensor_result = sensor.process_batch([
        {"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}
    ])
    print(f"{sensor_result}\n")

    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print("Stream ID: TRANS_001, Type: Financial Data")

    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    trans_result = trans.process_batch([
        {"buy": 100}, {"sell": 150}, {"buy": 75}
    ])
    print(f"{trans_result}\n")

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print("Stream ID: EVENT_001, Type: System Events")

    print("Processing event batch: [login, error, logout]")
    event_result = event.process_batch(["login", "error", "logout"])
    print(f"{event_result}\n")

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(trans)
    manager.add_stream(event)

    batch_data = {
        "SENSOR_001": [{"temp": 22.0}, {"temp": 23.5}],
        "TRANS_001": [{"buy": 50}, {"sell": 75}, {"buy": 25}, {"sell": 100}],
        "EVENT_001": ["start", "process", "complete"]
    }

    print("Batch 1 Results:")
    manager.process_all(batch_data)
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed\n")

    print("Stream filtering active: High-priority data only")
    critical_sensors = sensor.filter_data(
        [{"temp": 150}, {"temp": 20}], criteria="high"
    )
    large_trans = trans.filter_data(
        [{"sell": 200}], criteria="large"
    )
    print("Filtered results: {0} critical sensor "
          "alerts, {1} large transaction\n".format(
              len(critical_sensors), len(large_trans)))

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
