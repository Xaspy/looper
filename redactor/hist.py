
class AudioHistory:
    def __init__(self, path: str, buffer_size: int) -> None:
        self._size = buffer_size
        self._iter = 1
        self._buffer = {self._iter: path}
        self._paths_to_del = []

    def get_current(self) -> str:
        return self._buffer[self._iter]

    def get_all_paths(self) -> list:
        return list(self._buffer.values())

    def get_iter(self) -> int:
        return self._iter

    def add(self, path: str) -> None:
        if self._iter < max(self._buffer.keys()):
            self._del_old_elems()
        self._iter += 1
        self._buffer[self._iter] = path
        if len(self._buffer) > 5:
            print('adding!!!')
            self._paths_to_del.append(self._buffer[min(self._buffer.keys())])
            print(self._paths_to_del)
            del self._buffer[min(self._buffer.keys())]

    def undo(self) -> None:
        if self._iter - 1 in self._buffer.keys():
            self._iter -= 1

    def redo(self) -> None:
        if self._iter + 1 in self._buffer.keys():
            self._iter += 1

    def get_paths_to_del(self) -> list:
        res = self._paths_to_del.copy()
        self._paths_to_del = []
        return res

    def _del_old_elems(self) -> None:
        print('iter-' + str(self._iter))
        for key in list(self._buffer.keys())[::-1]:
            print(key)
            if key > self._iter:
                print('+')
                self._paths_to_del.append(self._buffer[key])
                del self._buffer[key]
                print(self._paths_to_del)
                print(self._buffer)
