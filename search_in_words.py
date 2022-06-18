class WordFilter:
    def __init__(self, words: list[str]):
        self.res=list(map(lambda x: list(x), words)) #split ["apple"]

    def f(self, prefix: str, suffix: str) -> int:
        result=[]
        for i in self.res[0]:
            result.append(i)
        if prefix in result and suffix in result:
            if result.index(prefix) > result.index(suffix):
                return result.index(prefix)
            else:
                return result.index(suffix)
        elif prefix in result:
            return result.index(prefix)
        elif suffix in result:
            return result.index(suffix)
        else:
            return False
obj = WordFilter(["apple"])
param_1 = obj.f("a", "e")
print(param_1)