from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0

        # key -> (value, frequency)
        self.key_to_val_freq = {}

        # frequency -> OrderedDict of keys
        # OrderedDict preserves LRU order among keys with same frequency
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        value, freq = self.key_to_val_freq[key]

        # Increase this key's frequency
        self._update_frequency(key, value, freq)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            _, freq = self.key_to_val_freq[key]
            self._update_frequency(key, value, freq)
            return

        # Evict if cache is full
        if len(self.key_to_val_freq) == self.capacity:
            # Remove least recently used key from the minimum frequency group
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]

        # Insert new key with frequency 1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    def _update_frequency(self, key: int, value: int, freq: int) -> None:
        # Remove key from current frequency group
        del self.freq_to_keys[freq][key]

        # If this was the only key in the minimum frequency group,
        # increase min_freq
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]

            if self.min_freq == freq:
                self.min_freq += 1

        # Add key to next frequency group as most recently used
        new_freq = freq + 1
        self.key_to_val_freq[key] = (value, new_freq)
        self.freq_to_keys[new_freq][key] = None