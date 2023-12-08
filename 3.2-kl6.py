from pprint import pprint
class LongestKeyDict(dict):
    def longest_key(self):
        # zwracac najdluzzysz klucz w slowniku
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


art = LongestKeyDict()

art['tomasz'] =12
art["ignacy"] =13
art["siedem"] =14
art["dupa"] =17
art['zen'] =1

print(art.longest_key())

pprint(art)
pprint(art.longest_key())