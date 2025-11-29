from .linked_list import SinglyLinkedList

class _HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, capacity: int = 10):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self._capacity = capacity
        self._table = [SinglyLinkedList() for _ in range(capacity)]
        self._size = 0

    def __len__(self):
        return self._size

    def _hash(self, key):
        return hash(key) % self._capacity

    def _resize(self):
        old_table = self._table
        self._capacity = self._capacity * 2
        self._table = [SinglyLinkedList() for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_table:
            for entry in bucket:
                self.put(entry.key, entry.value)

    def put(self, key, value):
        if self._size > self._capacity * 0.75:
            self._resize()

        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        bucket.insert_at_head(_HashEntry(key, value))
        self._size += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value

        raise KeyError(f"Key not found: {key}")

    def delete(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                bucket.delete_by_value(entry)
                self._size -= 1
                return True

        return False

    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

class HashTableProbing:
    EMPTY = object()
    DELETED = object()

    class _HashEntry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity: int = 11, load_factor: float = 0.7):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self._capacity = capacity
        self._table = [self.EMPTY] * capacity
        self._size = 0
        self._load_factor = float(load_factor)

    def __len__(self) -> int:
        return self._size

    def _hash(self, key) -> int:
        return hash(key) % self._capacity

    def _find_slot(self, key, for_insert: bool):
        
        start = index = self._hash(key)
        first_tombstone = None

        while True:
            slot = self._table[index]

            if slot is self.EMPTY:

                if for_insert:

                    return (first_tombstone if first_tombstone is not None else index, None, first_tombstone)
                return (index, None, first_tombstone)

            if slot is self.DELETED:
                if first_tombstone is None:
                    first_tombstone = index

            else:
                # real entry
                if slot.key == key:
                    return (index, slot, first_tombstone)

            index = (index + 1) % self._capacity
            if index == start:
                # full cycle
                if for_insert:
                    return (first_tombstone if first_tombstone is not None else -1, None, first_tombstone)
                return (-1, None, first_tombstone)

    def _resize_and_rehash(self):
        old_table = self._table
        self._capacity = self._capacity * 2 + 1
        self._table = [self.EMPTY] * self._capacity
        self._size = 0

        for slot in old_table:
            if slot not in (self.EMPTY, self.DELETED):
                # re-insert active entries
                self.put(slot.key, slot.value)

    def put(self, key, value):
        if (self._size + 1) / self._capacity > self._load_factor:
            self._resize_and_rehash()

        index, entry_found, tombstone_index = self._find_slot(key, for_insert=True)

        if entry_found is not None:

            entry_found.value = value
            return

        if index == -1:
            self._resize_and_rehash()
            index, entry_found, tombstone_index = self._find_slot(key, for_insert=True)

        self._table[index] = self._HashEntry(key, value)
        self._size += 1

    def get(self, key):
        index, entry_found, _ = self._find_slot(key, for_insert=False)
        if entry_found is not None:
            return entry_found.value
        raise KeyError(f"Key not found: {key}")

    def delete(self, key):
        index, entry_found, _ = self._find_slot(key, for_insert=False)
        if entry_found is None:
            return False
        
        self._table[index] = self.DELETED
        self._size -= 1
        return True

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

class HashTableQuadratic:
    EMPTY = object()
    DELETED = object()

    class _HashEntry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity: int = 11, load_factor: float = 0.7, c1: int = 1, c2: int = 1):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self._capacity = capacity
        self._table = [self.EMPTY] * capacity
        self._size = 0
        self._load_factor = load_factor

        self._c1 = c1
        self._c2 = c2

    def __len__(self):
        return self._size

    def _hash(self, key):
        return hash(key) % self._capacity

    def _find_slot(self, key, for_insert: bool):
        """Return (index, entry_or_None, tombstone_index_or_None)."""

        start = self._hash(key)
        first_tombstone = None

        for i in range(self._capacity):
            index = (start + self._c1 * i + self._c2 * i * i) % self._capacity
            slot = self._table[index]

            if slot is self.EMPTY:
                if for_insert:
                    return (first_tombstone if first_tombstone is not None else index,
                            None,
                            first_tombstone)
                return (index, None, first_tombstone)

            if slot is self.DELETED:
                if first_tombstone is None:
                    first_tombstone = index
                continue

            if slot.key == key:
                return (index, slot, first_tombstone)

        # Table full
        return (-1, None, first_tombstone)

    def _resize_and_rehash(self):
        old_table = self._table
        self._capacity = self._capacity * 2 + 1
        self._table = [self.EMPTY] * self._capacity
        self._size = 0

        for entry in old_table:
            if entry not in (self.EMPTY, self.DELETED):
                self.put(entry.key, entry.value)

    def put(self, key, value):
        if (self._size + 1) / self._capacity > self._load_factor:
            self._resize_and_rehash()

        index, entry_found, tombstone_index = self._find_slot(key, for_insert=True)

        if entry_found is not None:
            entry_found.value = value
            return

        if index == -1:
            # should never happen because resize fixed it.
            self._resize_and_rehash()
            index, _, _ = self._find_slot(key, for_insert=True)

        self._table[index] = self._HashEntry(key, value)
        self._size += 1

    def get(self, key):
        index, entry_found, _ = self._find_slot(key, for_insert=False)
        if entry_found is not None:
            return entry_found.value
        raise KeyError(f"Key not found: {key}")

    def delete(self, key):
        index, entry_found, _ = self._find_slot(key, for_insert=False)
        if entry_found is None:
            return False
        self._table[index] = self.DELETED
        self._size -= 1
        return True

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)
