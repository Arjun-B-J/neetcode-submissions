# HashTable using open addressing (linear probing) + tombstones
class _Tombstone:
    """Marker for a deleted slot."""
    pass

TOMBSTONE = _Tombstone()

class HashTable:
    def __init__(self, capacity: int):
        if capacity <= 1:
            raise ValueError("capacity must be > 1")
        self.capacity = capacity
        self.table = [None] * self.capacity  # slot: None | TOMBSTONE | (key, value, hash)
        self.size = 0         # number of live key/value pairs
        self.tombstones = 0   # number of tombstone slots

    def _hash(self, key: int) -> int:
        # stable non-negative hash
        return (hash(key) & 0x7FFFFFFF) % self.capacity

    def _probe_indices(self, start):
        i = start
        while True:
            yield i
            i = (i + 1) % self.capacity

    def _find_slot(self, key):
        """
        Find a slot for this key.
        Returns (found, index)
         - found=True  => slot contains the key
         - found=False => slot is where we should insert (first tombstone seen or first empty)
        """
        h = hash(key) & 0x7FFFFFFF
        start = h % self.capacity
        first_tombstone = None

        for i in self._probe_indices(start):
            slot = self.table[i]
            if slot is None:
                # empty slot: key not present. If we saw a tombstone earlier, return that for insertion.
                return (False, first_tombstone if first_tombstone is not None else i)
            if slot is TOMBSTONE:
                if first_tombstone is None:
                    first_tombstone = i
                # continue searching
                continue
            k, v, stored_hash = slot
            if stored_hash == h and k == key:
                return (True, i)
            # otherwise continue probing

    def get(self, key: int) -> int:
        found, idx = self._find_slot(key)
        if not found:
            return -1
        k, v, _ = self.table[idx]
        return v

    def insert(self, key: int, value: int) -> None:
        # If this insertion would make load factor >= 0.5, resize first
        # (we test using size + 1 because this insert may be new)
        if (self.size + 1) * 1.0 / self.capacity >= 0.5:
            self.resize()

        found, idx = self._find_slot(key)
        if found:
            # replace value
            k, _, stored_hash = self.table[idx]
            self.table[idx] = (k, value, stored_hash)
            return

        # we'll insert at idx (could be first tombstone or empty)
        if self.table[idx] is TOMBSTONE:
            self.tombstones -= 1
        self.table[idx] = (key, value, hash(key) & 0x7FFFFFFF)
        self.size += 1

    def remove(self, key: int) -> bool:
        found, idx = self._find_slot(key)
        if not found:
            return False
        # mark tombstone
        self.table[idx] = TOMBSTONE
        self.size -= 1
        self.tombstones += 1

        # optional maintenance: if tombstones accumulate, rehash to clean them
        # heuristic: rehash into same capacity when tombstones > capacity//4
        if self.tombstones > (self.capacity // 4):
            self._rehash(self.capacity)
        return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        """Double capacity and rehash all live entries."""
        new_capacity = max(2, self.capacity * 2)
        self._rehash(new_capacity)

    def _rehash(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.table = [None] * self.capacity
        self.size = 0
        self.tombstones = 0

        for slot in old_table:
            if slot is None or slot is TOMBSTONE:
                continue
            k, v, stored_hash = slot
            # insert into new table (linear probe, no resize checks)
            start = stored_hash % self.capacity
            for i in self._probe_indices(start):
                if self.table[i] is None:
                    self.table[i] = (k, v, stored_hash)
                    self.size += 1
                    break

    def __repr__(self):
        parts = []
        for i, slot in enumerate(self.table):
            if slot is None:
                parts.append(f"{i}: None")
            elif slot is TOMBSTONE:
                parts.append(f"{i}: TOMBSTONE")
            else:
                k, v, h = slot
                parts.append(f"{i}: ({k}->{v}, h={h})")
        return "<HashTable " + ", ".join(parts) + ">"
