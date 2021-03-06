from typing import Any, MutableSet, TypeVar, Sequence, Union, Tuple, List, Iterator, Dict, Set, Iterable


def is_iterable(obj: Any) -> bool: ...


T = TypeVar('T')


class OrderedSet(MutableSet[T], Sequence[T]):
    def __init__(self, iterable: Iterable[T] = None) -> None:
        self.map: Dict[T, int] = {}
        self.items: List[T] = []

    def __len__(self) -> int: ...
    def __getitem__(self, index: Union[int, slice, Sequence[int]]) -> OrderedSet[T]: ...
    def copy(self) -> OrderedSet[T]: ...
    def __getstate__(self) -> Union[Tuple[None], List[T]]: ...
    def __setstate__(self, state: Union[Tuple[None], List[T]]) -> None: ...
    def __contains__(self, key: T) -> bool: ...
    def add(self, key: T) -> int: ...
    append = add
    def update(self, sequence: Sequence[T]) -> int: ...
    def index(self, key: Union[T, Sequence[T]]) -> int: ...
    def pop(self) -> T: ...
    def discard(self, key: T) -> None: ...
    def clear(self) -> None: ...
    def __iter__(self) -> Iterator[T]: ...
    def __reversed__(self) -> List[T]: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Sequence[T]) -> bool: ...
    def union(self, *sets: Sequence[T]) -> OrderedSet[T]: ...
    def __and__(self, other: Sequence[T]) -> OrderedSet[T]: ...
    def intersection(self, *sets: Sequence[T]) -> OrderedSet[T]: ...
    def difference(self, *sets: Sequence[T]) -> OrderedSet[T]: ...
    def issubset(self, other: Union[Set[T], Sequence[T]]) -> bool: ...
    def issuperset(self, other: Union[Set[T], Sequence[T]]) -> bool: ...
    def symmetric_difference(self, other: Sequence[T]) -> OrderedSet[T]: ...
    def difference_update(self, *sets: Sequence[T]) -> None: ...
    def intersection_update(self, other: Sequence[T]) -> None: ...
    def symmetric_difference_update(self, other: Sequence[T]) -> None: ...
