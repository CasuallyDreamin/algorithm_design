from data_structures.core.hash_table import HashTable, HashTableProbing, HashTableQuadratic
import pytest


class TestHashTable:

    def test_init_and_empty(self):
        ht = HashTable(capacity=5)
        assert len(ht) == 0
        assert ht._capacity == 5

    def test_put_and_get_simple(self):
        ht = HashTable(capacity=5)
        ht.put("key1", "value1")
        ht.put(10, 100)

        assert len(ht) == 2
        assert ht.get("key1") == "value1"
        assert ht.get(10) == 100

    def test_update_existing_key(self):
        ht = HashTable(capacity=5)
        ht.put("test", "old_value")
        ht.put("test", "new_value")

        assert len(ht) == 1
        assert ht.get("test") == "new_value"

    def test_key_not_found(self):
        ht = HashTable(capacity=5)
        ht.put("a", 1)

        with pytest.raises(KeyError, match="missing"):
            ht.get("missing")

    def test_delete_existing_key(self):
        ht = HashTable(capacity=5)
        ht.put("k1", 10)
        ht.put("k2", 20)

        assert ht.delete("k1") is True
        assert len(ht) == 1
        assert ht.get("k2") == 20

        with pytest.raises(KeyError):
            ht.get("k1")

    def test_delete_non_existent_key(self):
        ht = HashTable(capacity=5)
        ht.put("a", 1)

        assert ht.delete("missing") is False
        assert len(ht) == 1

    def test_collision_resolution(self):
        ht = HashTable(capacity=5)

        ht.put(0, 100)
        ht.put(5, 200)  # same hash slot

        assert ht._hash(0) == ht._hash(5)
        assert ht.get(0) == 100
        assert ht.get(5) == 200

        # delete a real key, not a fantasy key
        ht.delete(5)
        assert len(ht) == 1

        with pytest.raises(KeyError):
            ht.get(5)

        assert ht.get(0) == 100


class TestHashTableProbing:

    def test_put_and_get_simple(self):
        ht = HashTableProbing(capacity=11)
        ht.put("apple", 5)
        ht.put("banana", 10)

        assert len(ht) == 2
        assert ht.get("apple") == 5
        assert ht.get("banana") == 10

    def test_update_existing_key(self):
        ht = HashTableProbing(capacity=5)
        ht.put("test", "old_value")
        ht.put("test", "new_value")

        assert len(ht) == 1
        assert ht.get("test") == "new_value"

    def test_linear_probing_and_collision(self):
        ht = HashTableProbing(capacity=3)

        ht.put("k1", 10)
        ht.put("k2_probe", 20)

        assert len(ht) == 2
        assert ht.get("k2_probe") == 20

    def test_deletion_and_tombstones(self):
        ht = HashTableProbing(capacity=5)

        ht.put("a", 10)
        ht.put("b", 20)
        ht.put("c", 30)

        assert ht.delete("b") is True
        assert len(ht) == 2

        # Tombstone reuse
        ht.put("d", 40)

        assert ht.get("a") == 10
        assert ht.get("c") == 30
        assert ht.get("d") == 40
        assert len(ht) == 3

    def test_resize_and_rehash(self):
        ht = HashTableProbing(capacity=5)
        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)

        assert ht._capacity == 5

        ht.put("d", 4)  # triggers resize

        assert ht._capacity > 5
        assert len(ht) == 4

        ht.put("e", 5)

        assert len(ht) == 5
        assert ht.get("a") == 1
        assert ht.get("d") == 4
        assert ht.get("e") == 5




class TestHashTableQuadratic:

    def test_put_and_get_simple(self):
        ht = HashTableQuadratic(capacity=11)
        ht.put("apple", 5)
        ht.put("banana", 10)

        assert len(ht) == 2
        assert ht.get("apple") == 5
        assert ht.get("banana") == 10

    def test_update_existing_key(self):
        ht = HashTableQuadratic(capacity=5)
        ht.put("test", "old_value")
        ht.put("test", "new_value")

        assert len(ht) == 1
        assert ht.get("test") == "new_value"

    def test_quadratic_probing_and_collision(self):
        ht = HashTableQuadratic(capacity=3)

        ht.put("k1", 10)
        ht.put("k2", 20)  # same hash slot triggers quadratic probing

        assert len(ht) == 2
        assert ht.get("k1") == 10
        assert ht.get("k2") == 20

    def test_deletion_and_tombstones(self):
        ht = HashTableQuadratic(capacity=5)

        ht.put("a", 10)
        ht.put("b", 20)
        ht.put("c", 30)

        assert ht.delete("b") is True
        assert len(ht) == 2

        # Tombstone reuse
        ht.put("d", 40)

        assert ht.get("a") == 10
        assert ht.get("c") == 30
        assert ht.get("d") == 40
        assert len(ht) == 3

    def test_resize_and_rehash(self):
        ht = HashTableQuadratic(capacity=5)
        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)

        assert ht._capacity == 5

        ht.put("d", 4)  # triggers resize

        assert ht._capacity > 5
        assert len(ht) == 4

        ht.put("e", 5)

        assert len(ht) == 5
        assert ht.get("a") == 1
        assert ht.get("d") == 4
        assert ht.get("e") == 5

    def test_key_not_found(self):
        ht = HashTableQuadratic(capacity=5)
        ht.put("x", 100)

        with pytest.raises(KeyError, match="missing"):
            ht.get("missing")

    def test_delete_non_existent_key(self):
        ht = HashTableQuadratic(capacity=5)
        ht.put("a", 1)

        assert ht.delete("missing") is False
        assert len(ht) == 1
